'''
Visualize Topics
'''
import argparse

from utils import *
from gensim.parsing import preprocessing as pp


def preprocess(text_file):
    print('perform preprocessing')
    arr = []
    fp = open(text_file, 'r')
    for line in fp:
        s = pp.preprocess_string(line.lower(), filters=[pp.strip_tags, pp.strip_punctuation, pp.strip_non_alphanum,
                                                        pp.strip_multiple_whitespaces, pp.strip_numeric,
                                                        pp.remove_stopwords])
        arr.append(s)
    fp.close()

    fout = open(text_file, 'w')
    for itm in arr:
        fout.write(' '.join(itm) + '\n')
    fout.close()


def process(file_suffix="", vocab_max_size=10000, vocab_min_count=3):
    text_file = "data/data_" + file_suffix + ".txt"
    corpus_file = "data/doc_term_mat_" + file_suffix + ".txt"
    vocab_file = "data/vocab_" + file_suffix + ".txt"

    preprocess(text_file)

    # create vocabulary
    vocab = {}
    fp = open(text_file, 'r')
    for line in fp:
        arr = re.split('\s', line[:-1])
        for wd in arr:
            try:
                vocab[wd] += 1
            except:
                vocab[wd] = 1
    fp.close()
    vocab_arr = [[wd, vocab[wd]] for wd in vocab if vocab[wd] > vocab_min_count]
    vocab_arr = sorted(vocab_arr, key=lambda k: k[1])[::-1]
    vocab_arr = vocab_arr[:vocab_max_size]
    vocab_arr = sorted(vocab_arr)

    fout = open(vocab_file, 'w')
    for itm in vocab_arr:
        itm[1] = str(itm[1])
        fout.write(' '.join(itm) + '\n')
    fout.close()

    # vocabulary to id
    vocab2id = {itm[1][0]: itm[0] for itm in enumerate(vocab_arr)}
    print('create document term matrix')
    data_arr = []
    fp = open(text_file, 'r')
    fout = open(corpus_file, 'w')
    for line in fp:
        arr = re.split('\s', line[:-1])
        arr = [str(vocab2id[wd]) for wd in arr if wd in vocab2id]
        sen = ' '.join(arr)
        fout.write(sen + '\n')
    fp.close()
    fout.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--text_file', default='data/data.txt', help='input text file')
    parser.add_argument('--corpus_file', default='data/doc_term_mat.txt', help='term document matrix file')
    parser.add_argument('--vocab_file', default='data/vocab.txt', help='vocab file')
    parser.add_argument('--vocab_max_size', type=int, default=10000, help='maximum vocabulary size')
    parser.add_argument('--vocab_min_count', type=int, default=3, help='minimum frequency of the words')
    parser.add_argument('--preprocessing', type=bool, default=False, help='enable preprocessing')
    args = parser.parse_args()

    if args.preprocessing:
        preprocess(args.text_file)

    # create vocabulary
    print('create vocab')
    vocab = {}
    fp = open(args.text_file, 'r')
    for line in fp:
        arr = re.split('\s', line[:-1])
        for wd in arr:
            try:
                vocab[wd] += 1
            except:
                vocab[wd] = 1
    fp.close()
    vocab_arr = [[wd, vocab[wd]] for wd in vocab if vocab[wd] > args.vocab_min_count]
    vocab_arr = sorted(vocab_arr, key=lambda k: k[1])[::-1]
    vocab_arr = vocab_arr[:args.vocab_max_size]
    vocab_arr = sorted(vocab_arr)

    fout = open(args.vocab_file, 'w')
    for itm in vocab_arr:
        itm[1] = str(itm[1])
        fout.write(' '.join(itm) + '\n')
    fout.close()

    # vocabulary to id
    vocab2id = {itm[1][0]: itm[0] for itm in enumerate(vocab_arr)}
    print('create document term matrix')
    data_arr = []
    fp = open(args.text_file, 'r')
    fout = open(args.corpus_file, 'w')
    for line in fp:
        arr = re.split('\s', line[:-1])
        arr = [str(vocab2id[wd]) for wd in arr if wd in vocab2id]
        sen = ' '.join(arr)
        fout.write(sen + '\n')
    fp.close()
    fout.close()
