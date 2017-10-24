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

class WorkList(Resource):

    def get(self):
        print("Call for: GET /works")
        url = config.es_base_url['works']+'/_search'
        query = {
            "query": {
                "match_all": {}
            },
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

    def post(self):
        print("Call for: POST /works")
        parser.add_argument('report')
        parser.add_argument('recipient')
        parser.add_argument('date')
        parser.add_argument('team')
        parser.add_argument('juridiction', action='append')
        work = parser.parse_args()
        print(work)
        url = config.es_base_url['works']
        resp = requests.post(url, data=json.dumps(work))
        data = resp.json()
        return data

class Work(Resource):

    def get(self, work_id):
        print("Call for: GET /works/%s" % work_id)
        url = config.es_base_url['works']+'/'+work_id
        resp = requests.get(url)
        data = resp.json()
        work = data['_source']
        return work

    def put(self, work_id):
        """TODO: update functionality not implemented yet."""
        pass

    def delete(self, work_id):
        print("Call for: DELETE /works/%s" % work_id)
        url = config.es_base_url['works']+'/'+work_id
        resp = requests.delete(url)
        data = resp.json()
        return data

class Style(Resource):
    pass

class StyleList(Resource):

    def get(self):
        print("Call for /juridiction")
        url = config.es_base_url['juridiction']+'/_search'
        query = {
            "query": {
                "match_all": {}
            },
            "size": 100
        }
        resp = requests.post(url, data=json.dumps(query))
        data = resp.json()
        juridiction = []
        for hit in data['hits']['hits']:
            style = hit['_source']
            style['id'] = hit['_id']
            juridiction.append(style)
        return juridiction

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

api.add_resource(Work, config.api_base_url+'/works/<work_id>')
api.add_resource(WorkList, config.api_base_url+'/works')
api.add_resource(StyleList, config.api_base_url+'/juridiction')
api.add_resource(Search, config.api_base_url+'/search')
