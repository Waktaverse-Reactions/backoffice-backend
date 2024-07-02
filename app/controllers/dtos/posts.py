from pydantic import BaseModel
from app.services.posts import PostsListDto


class PostsResponseDto(BaseModel):
    data: PostsListDto


class SpecficPostResponseDto(BaseModel):
    data: dict
