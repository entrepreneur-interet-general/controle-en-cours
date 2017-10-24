from flask import Flask
from flask_restful import reqparse, Resource, Api
from flask.ext.cors import CORS
import requests
from . import config
import json

app = Flask(__name__)
CORS(app)
api = Api(app)

parser = reqparse.RequestParser()

class Search(Resource):

    def get(self):
        print("Call for GET /search")
        parser.add_argument('q')
        query_string = parser.parse_args()
        url = config.es_base_url['works']+'/_search'
        query = {
            "query": {
                "multi_match": {
                    "fields": ["report", "recipient", "team", "juridiction"],
                    "query": query_string['q'],
                    "type": "cross_fields",
                    "use_dis_max": False,
                }
            },
            "sort": { "date": { "order": "desc" }},
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        works = []
        for hit in data['hits']['hits']:
            work = hit['_source']
            work['id'] = hit['_id']
            works.append(work)
        return works

api.add_resource(Search, config.api_base_url+'/search')
