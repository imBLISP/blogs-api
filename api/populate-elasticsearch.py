import json
from elasticsearch.helpers import bulk
from app.utils.elasticsearch import get_elasticsearch_connection

print("Populating elasticsearch..")

# Connect to Elasticsearch
es = get_elasticsearch_connection()

# Define the index name
index_name = "blogs"

# Define the mapping
mapping = {
    "mappings": {
        "properties": {
            "blog_title": {"type": "text"},
            "blog_text": {"type": "text"},
            "user_id": {"type": "keyword"}
        }
    }
}

# Error handling incase index is already inserted
try:
    # Create the index with the mapping
    es.indices.create(index=index_name, body=mapping)
except Exception as e:
    print(f"Error while creating index: {e}")

# Insert sample data
try: 
    sample_data=[]
    with open("./data/sample-data.json", "r") as f:
        sample_data = json.load(f)

    # Index the sample data
    # es.index(index=index_name, body=sample_data)
    bulk(es, sample_data, index='blogs')
except Exception as e:
    print(f"Error while inserting sample data: {e}")
