# Blogs API
Async api for creating blogs

## Testing

Create blog
```curl
curl --location 'localhost:8000/blogs' \
--header 'Content-Type: application/json' \
--data '{
    "blog_title": "My first blog",
    "blog_text": "This blog will test create blog api",
    "user_id": "vin"   
}'
```

List all blogs
```curl
curl --location 'http://localhost:8000/blogs'
```

Search blogs
```curl
curl --location 'localhost:8000/blogs/search?query=%22Haskell%22'
