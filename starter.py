"""This file starts the microservice"""
import os

#!flask/bin/python
from flask import Flask, json, jsonify, logging, request

# import classification_facade

with open('./config.json') as config_file:
    CONFIG = json.load(config_file)

app = Flask(__name__)


@app.route("/hitec/classify/concepts/seanmf/", methods=["POST"])
def post_classification_result(lang):
    app.logger.debug('/hitec/classify/concepts/seanmf/ called'.format(lang))

    # app.logger.debug(request.data.decode('utf-8'))
    content = json.loads(request.data.decode('utf-8'))

    # process content

    # start concept detection
    # processed_tweets = classification_facade.process_tweets(tweets, lang)

    # app.logger.debug(classified_tweets)
    # return jsonify(processed_tweets)

    # for now we return the things we received
    return jsonify(content)


@app.route("/hitec/classify/concepts/seanmf/status", methods=["GET"])
def get_status():

    status = {
        "status": "operational",
    }

    return jsonify(status)


if __name__ == "__main__":
    app.run(debug=False, threaded=False, host=CONFIG['HOST'], port=CONFIG['PORT'])