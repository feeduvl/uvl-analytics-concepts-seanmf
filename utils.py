import os
import re
import numpy as np


def read_docs(file_name):
    print('read documents')
    print('-'*50)
    docs = []
    fp = open(file_name, 'r')
    for line in fp:
        arr = re.split('\s', line[:-1])
        arr = filter(None, arr)
        arr = [int(idx) for idx in arr]
        docs.append(arr)
    fp.close()
    
    return docs


def read_vocab(file_name):
    print('read vocabulary')
    print('-'*50)
    vocab = []
    fp = open(file_name, 'r')
    for line in fp:
        arr = re.split('\s', line[:-1])
        vocab.append(arr[0])
    fp.close()

    return vocab


def cleanup(file_suffix=""):
    text_file = "data/data_" + file_suffix + ".txt"
    corpus_file = "data/doc_term_mat_" + file_suffix + ".txt"
    vocab_file = "data/vocab_" + file_suffix + ".txt"
    W1file = 'seanmf_results/W_' + file_suffix + '.txt'
    W2file = 'seanmf_results/Wc_' + file_suffix + '.txt'
    Hfile = 'seanmf_results/H_' + file_suffix + '.txt'

    files = [text_file, corpus_file, vocab_file, W1file, W2file, Hfile]

    for file in files:
        os.remove(file)


def calculate_PMI(AA, topKeywordsIndex):
    '''
    Reference:
    Short and Sparse Text Topic Modeling via Self-Aggregation
    '''
    D1 = np.sum(AA)
    n_tp = len(topKeywordsIndex)
    PMI = []
    for index1 in topKeywordsIndex:
        for index2 in topKeywordsIndex:
            if index2 < index1:
                if AA[index1, index2] == 0:
                    PMI.append(0.0)
                else:
                    C1 = np.sum(AA[index1])
                    C2 = np.sum(AA[index2])
                    PMI.append(np.log(AA[index1,index2]*D1/C1/C2))
    avg_PMI = 2.0*np.sum(PMI)/float(n_tp)/(float(n_tp)-1.0)

    return avg_PMI
