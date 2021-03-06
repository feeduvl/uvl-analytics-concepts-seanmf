"""
Prepare results
"""
import numpy as np
from utils import read_docs, read_vocab


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))


def normalize(x):
    return x / np.sum(x)


def prepare_results(file_suffix=""):
    docs = read_docs("data/doc_term_mat_" + file_suffix + ".txt")
    vocab = read_vocab("data/vocab_" + file_suffix + ".txt")
    n_docs = len(docs)
    W = np.loadtxt("seanmf_results/W_" + file_suffix + ".txt", dtype=float)
    H = np.loadtxt("seanmf_results/H_" + file_suffix + ".txt", dtype=float)
    n_topic = W.shape[1]

    n_topKeyword = 10

    topics = dict()

    # get top 10  topic words with their probabilities for each topic
    for k in range(n_topic):
        topKeywordsIndex = W[:, k].argsort()[::-1][:n_topKeyword]
        l = list()
        for kw in range(n_topKeyword):
            l.append(vocab[topKeywordsIndex[kw]])
        topics.update({str(k): l})

    doc_topic = dict()

    for k in range(n_docs):
        topTopicIndex = H[k, :].argsort()[::-1]
        # s = softmax(H[k, :])
        s = H[k, :]

        # normalize
        s = normalize(s)

        l = list()

        for t in topTopicIndex:
            l.append([int(t), float(s[t])])

        doc_topic.update({str(k): l})

    return topics, doc_topic
