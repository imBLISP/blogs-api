import os
from elasticsearch import Elasticsearch

def format_search_results(search_result):
    hits = search_result['hits']['hits']
    return [obj['_source'] for obj in hits]

def get_elasticsearch_connection():
    url = os.environ.get("ELASTICSEARCH_URL")
    username = os.environ.get("ELASTICSEARCH_USERNAME")
    password = os.environ.get("ELASTICSEARCH_PASSWORD")

    return Elasticsearch(
        [url],
        basic_auth=(username, password)
    )
    
