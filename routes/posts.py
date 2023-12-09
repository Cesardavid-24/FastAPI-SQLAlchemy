from fastapi import APIRouter , HTTPException
from models.models import Post
from dbjson import DBJson
import asyncio
"""
    get_all_post
    get_post_by_id
    create_post
    update_post
    delete_post
    
"""
posts = APIRouter()

@posts.get("/")
def index():
    return {"message": "Hello, world to my API!"}

@posts.get("/posts")
async def get_posts():
        posts = await DBJson().get_all()
        if not posts:
            raise HTTPException(status_code=404, detail='No posts found')
        
        return posts



@posts.post("/posts")
def create_post(post: Post):
    posts.append(post.dict())
    return posts[-1]


@posts.get('/posts/{post_id}')
def get_post(post_id: str):
    for post in posts:
        if post['id'] == post_id:
            return post
    raise HTTPException(status_code=404, detail='Post not found')

@posts.put('/posts/{post_id}')
def update_post(post_id: str, post: Post):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            # post['title'] = post.title
            # post['author'] = post.author
            # post['content'] = post.content
            posts[index] = post
            return {"message": "Post updated successfully"}
    raise HTTPException(status_code=404, detail='Post not found')

@posts.delete('/posts/{post_id}')
def delete_post(post_id: str):
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail='Post not found')

