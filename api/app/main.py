from typing import Union
from fastapi import FastAPI
from app.models.blogs import Blog
from app.worker import create_blog_task
from app.utils.elasticsearch import format_search_results, get_elasticsearch_connection

es = get_elasticsearch_connection()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Server is running"}

@app.get("/blogs")
async def get_blogs():
    search_result = es.search(
            size=100,
            query={
                'match_all': {}
                }
            )
    return format_search_results(search_result)

@app.post("/blogs")
async def create_blog(blog: Blog):
    t = create_blog_task.delay(blog.dict())
    return t.status
    
@app.get("/blogs/search")
async def root(query: Union[str, None] = None):
    result = es.search(index="blogs", query={
        "multi_match": {
            "fields": ["blog_title", "blog_text"],
            "query": query,
            }
        })
    return format_search_results(result)
