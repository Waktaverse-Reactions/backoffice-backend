from fastapi import status
from pydantic import BaseModel

from app.common.dtos.base import BasePaginationDto
from app.common.exceptions import error_code, APIException
from app.plugins.repository import _Collections, RepositoryPlugin


class PostsListDto(BaseModel):
    posts: list[dict]
    pagination: BasePaginationDto


class PostsService:
    def __init__(self):
        self.repository = RepositoryPlugin().getDB(_Collections.POSTS)

    def getMany(self, page: int = 1, count: int = 12) -> PostsListDto:
        if page < 1:
            raise APIException(
                status=status.HTTP_400_BAD_REQUEST,
                code=error_code.get(str(status.HTTP_400_BAD_REQUEST)),
                message="페이지 번호는 0보다 커야합니다.",
            )

        posts = self.repository.find().skip((page - 1) * count).limit(count)
        posts_count = self.repository.count_documents({})

        return PostsListDto(
            posts=posts,
            pagination=BasePaginationDto(
                currentPage=page,
                totalPage=posts_count // count + 1,
                hasNextPage=posts_count > page * count,
            ),
        )

    def get(self, id: str):
        post = self.repository.find_one({"id": id})

        if post is None:
            raise APIException(
                status=status.HTTP_404_NOT_FOUND,
                code=error_code.get(str(status.HTTP_404_NOT_FOUND)),
                message="해당 게시글을 찾을 수 없습니다.",
            )

        return post
