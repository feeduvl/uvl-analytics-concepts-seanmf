# uvl-analytics-concepts-seanmf [![badge](https://img.shields.io/badge/License-GPL%203.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.de.html)

## About

This is a microservice that can run in a docker container and perform SeaNMF topic detection when queried by a REST call.

## REST API

See [swagger.yaml](../master/swagger.yaml) for details. The tool at https://editor.swagger.io/ can be used to render the swagger file.

## Method Parameter

**alpha** - Factorization weight for word-semantic correlations, higher alpha may increase coherence, but reduce interpretability of topics. Can be in (0,1] range. Default: 0.1

**beta** - Sparsity factor, increase beta (eg. 0.1) for SparseSeaNMF (SSeaNMF), for normal SeaNMF this parameter is not needed (=0). Can be in [0,1] range. Default: 0

**n_topics** - The number of topics that shall be detected. Higher topic coherence indicates a better n_topics. Can be any number > 0. Default: 10

**max_iter** - Maximum number of iterations that will be performed. Default: 500

**max_err** - Error threshold. The processing will stop when the error is smaller than `max_err` or `max_iter` is reached. Default: 0.1

**fix_random** -  Set to `true` to fix random seed to `0`. This will make the results reproducible. Default: false

**vocab_min_count** - Only words that occur more than `vocab_min_count` times will be added to vocabulary, if the dataset is small and the `vocab_min_count` to high, the processing will fail. Default: 3

## Source

This repository is based on the SeaNMF implementation of the paper
- [Tian Shi](http://life-tp.com/Tian_Shi/), Kyeongpil Kang, [Jaegul Choo](https://sites.google.com/site/jaegulchoo/) and [Chandan K. Reddy](http://people.cs.vt.edu/~reddy/), "Short-Text Topic Modeling via Non-negative Matrix Factorization Enriched with Local Word-Context Correlations", In Proceedings of the International Conference on World Wide Web (WWW), Lyon, France, April 2018. [PDF](http://dmkd.cs.vt.edu/papers/WWW18.pdf)

Original Repository: (https://github.com/tshi04/SeaNMF)

The code has been modified to be dockerized and to offer a REST API via Flask.

## License
Free use of this software is granted under the terms of the [GPL version 3](https://www.gnu.org/licenses/gpl-3.0.de.html) (GPL 3.0).
