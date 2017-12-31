'''
Visualize Topics
'''
import argparse

from utils import *

parser = argparse.ArgumentParser()
parser.add_argument('--corpus_file', default='data/doc_term_mat.txt', help='term document matrix file')
parser.add_argument('--vocab_file', default='data/vocab.txt', help='vocab file')
parser.add_argument('--par_file', default='seanmf_results/W.txt', help='model results file')
opt = parser.parse_args()

docs = read_docs(opt.corpus_file)
vocab = read_vocab(opt.vocab_file)
n_docs = len(docs)
n_terms = len(vocab)
print 'n_docs={0}, n_terms={1}'.format(n_docs, n_terms)

dt_mat = np.zeros([n_terms, n_terms])
cnt = 0
for itm in docs:
    cnt += 1
    for kk in itm:
        for jj in itm:
            if kk != jj:
                dt_mat[int(kk), int(jj)] += 1.0
print 'co-occur done'
        
W = np.loadtxt(opt.par_file, dtype=float)
n_topic = W.shape[1]
print 'n_topic={0}'.format(n_topic)

PMI_arr = []
n_topKeyword = 10
for k in range(n_topic):
    topKeywordsIndex = W[:,k].argsort()[::-1][:n_topKeyword]
    PMI_arr.append(calculate_PMI(dt_mat, topKeywordsIndex))
    
print 'Average PMI={0}'.format(np.average(np.array(PMI_arr)))

index = np.argsort(PMI_arr)
print index
    
term_z = W
print n_terms, n_topic
for k in index:
    print 'Topic ' + str(k+1) + ': ',
    print PMI_arr[k],
    for w in np.argsort(-term_z[:,k])[:n_topKeyword]:
        print vocab[w],
    print
