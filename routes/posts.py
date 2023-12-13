from fastapi import APIRouter , HTTPException , status
from models.models import Post, UpdatePost
from dbjson import DBJson

posts = APIRouter()

@posts.get("/", status_code=status.HTTP_200_OK)
def index():
    return {"message": "Hello, world to my API!"}

@posts.get("/posts", response_model=list[Post], status_code=status.HTTP_200_OK)
def get_posts() -> list[Post]:
        posts = DBJson().get_all()
        if not posts:
            raise HTTPException(status_code=404, detail='No posts found')
    
        return posts


@posts.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post: Post) -> dict:
    return DBJson().create(post)


@posts.get('/posts/{post_id}', response_model=dict, status_code=status.HTTP_200_OK)
def get_post(post_id: str) -> dict:
    post_by_id = DBJson().get_by_id(post_id)
    if not post_by_id:
        raise HTTPException(status_code=404, detail='Post not found')
    
    return post_by_id

@posts.put('/posts/{post_id}', status_code=status.HTTP_200_OK)
def update_post(post_id: str, post: UpdatePost) -> dict:
    return DBJson().update_post(post_id, post)


@posts.delete('/posts/{post_id}')
def delete_post(post_id: str) -> dict:
    for index, post in enumerate(posts):
        if post['id'] == post_id:
            posts.pop(index)
            return {"message": "Post deleted successfully"}
    raise HTTPException(status_code=404, detail='Post not found')

