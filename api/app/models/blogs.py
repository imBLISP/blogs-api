from pydantic import BaseModel

class Blog(BaseModel):
    blog_title: str
    blog_text: str
    user_id: str
