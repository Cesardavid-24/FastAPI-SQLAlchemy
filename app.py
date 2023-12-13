from fastapi import FastAPI 
from routes.posts import posts

app = FastAPI()

app.include_router(posts)


