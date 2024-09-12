import os
from celery.app import Celery
from app.utils.elasticsearch import get_elasticsearch_connection

broker = os.environ.get("CELERY_BROKER_URL")
backend = os.environ.get("CELERY_BACKEND_URL")
celery = Celery(__name__, broker=broker, backend=backend)

es = get_elasticsearch_connection()

@celery.task()
def create_blog_task(blog):
    print("inside create blog tasks")
    es.index(
        index="blogs",
        document=blog,
    )
