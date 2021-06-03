"""This file starts the microservice"""

import datetime

from flask import Flask, json, jsonify, request

import data_process
import train
import results
import utils

with open('./config.json') as config_file:
    CONFIG = json.load(config_file)

app = Flask(__name__)


@app.route("/hitec/classify/concepts/seanmf/", methods=["POST"])
def post_classification_result():
    app.logger.debug('/hitec/classify/concepts/seanmf/ called')

    timestamp = '{:%Y-%m-%d %H%M%S-%f}'.format(datetime.datetime.now())

    # app.logger.debug(request.data.decode('utf-8'))
    content = json.loads(request.data.decode('utf-8'))

    # save content
    dataset = content["dataset"]["documents"]

    with open('data/data_' + timestamp + ".txt", 'w') as out_file:
        for doc in dataset:
            out_file.write(doc["text"])

    # start pre-processing
    data_process.process(timestamp)

    # start concept detection
    train.train(timestamp, content["method"], content["alpha"], content["beta"], content["n_topics"],
                content["max_iter"], content["max_err"], content["fix_random"])

    # prepare results
    topics, doc_topic = results.prepare_results(timestamp)

    res = dict()

    res.update({"topics": topics})
    res.update({"doc_topic": doc_topic})

    # cleanup
    utils.cleanup(timestamp)

    # send results back
    return jsonify(res)


@app.route("/hitec/classify/concepts/seanmf/status", methods=["GET"])
def get_status():
    status = {
        "status": "operational",
    }

    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=False, threaded=False, host=CONFIG['HOST'], port=CONFIG['PORT'])
