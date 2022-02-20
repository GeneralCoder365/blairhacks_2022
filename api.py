import sys
import logging

from flask import Flask, render_template
from flask import request
from flask_restful import Resource, Api, reqparse

import web_scraper

app = Flask(__name__)
api = Api(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

# import json
@app.route('/search', methods=["GET"])
# @profile # marks function to be tracked for memory usage
def search():
    tags = request.args.get('tags')
    # print("tags: ", tags)
    # data = dict(json.loads(tags))
    data = web_scraper.master_output(tags)
    # print(data)
    return {'data':data}, 200

app.debug = True

if __name__ == '__main__':
    app.run()