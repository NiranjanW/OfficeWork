from gc import __loader__
from pathlib import Path
import json
import os
import pprint
import requests
from elasticsearch import Elasticsearch
import logging

logger = logging.getLogger('activesprint')


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
# res = requests.get('http://qa.internal.api2.lcbo.com/octane/activesprints?sharedspace=71038')
# # pprint.pprint(res.content)
# struct= {}
# if res.status_code ==200:
#     logger.info(type(res.content))
#     response = res.content.decode('utf-8')
#     struct = json.loads(response)
#
#
#     es.index(index='ev4', doc_type='events', id=1, body=struct)
#     print('pass')


def connect_elasticsearch():
    _es = None
    _es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    if _es.ping():
        print('Yay Connect')
    else:
        print('Arrr it could not connect!')
    return _es
if __name__ == '__main__':
  logging.basicConfig(level=logging.ERROR)


def create_index(es_object, index_name='recipes'):
    created = False
    # index settings
    settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "members": {
                "dynamic": "strict",
                "properties": {
                    "title": {
                        "type": "text"
                    },
                    "submitter": {
                        "type": "text"
                    },
                    "description": {
                        "type": "text"
                    },
                    "calories": {
                        "type": "integer"
                    },
                }
            }
        }
    }
    try:
            if not es_object.indices.exists(index_name):
                # Ignore 400 means to ignore "Index Already Exist" error.
                es_object.indices.create(index=index_name, ignore=400, body=settings)
                print('Created Index')
            created = True
    except Exception as ex:
            print(str(ex))
    finally:
            return created


def store_record(elastic_object, index_name, record):
    try:
        outcome = elastic_object.index(index=index_name, doc_type='salads', body=record)
    except Exception as ex:
        print('Error in indexing data')
        print(str(ex))


dirname = Path.cwd().joinpath('data')

as_filename='activesprintNull'
ph_filename='projecthealth.json'
suffix ='.json'
activesprint_file = (Path(dirname,as_filename).with_suffix(suffix))
projecthealth_file = (Path(dirname,ph_filename).with_suffix(suffix))

defects = {}

def load_es(file):

    with open(file ,'r') as fh:
        es.index(index='as', doc_type='events', id=1, body=json.load(fh))

# data = json.loads(filename)
# print(type(data))
# print(data['defects'])
# [ print(item['id'],item['name'])for item in data['workspaces']]
events={}
file = (Path(dirname,ph_filename).with_suffix(suffix))
with open(file ,'r') as fh:
    data = json.load(fh)
    for workspace in  data['workspaces']:
        work = workspace['id']
        if work == '15001':
            events = workspace.get('events')

# [print(event) for event in events]




    # print(item.get('defects'))
#     events = (item.get('events'))
#
# [print(event) for event in events]

es.index(index='ev4' ,doc_type='events',id=1, body=json.dumps(data))
# es.index(index='ev' ,doc_type='events',id=i, body=events)
i =1

# for event in events:
#     es.index(index='ev3' ,doc_type='events',id=1, body=json.dumps(event))
#     i=i+1
# print(i)
# print(es.get(index='ev3' ,doc_type='events',id =1))

# for i in range(2):
#        result = es.get(index='ev' ,doc_type='events',id =i)
#        print(result)

# for d in data:
#     print(d)
#     if d['defects']:
#         print(d['defects'])

# pprint.pprint(data)

if __name__ == '__main__':
    load_es(activesprint_file)