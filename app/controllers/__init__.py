from fastapi import APIRouter

from .root import router as root_controller
from .auth import router as auth_controller
from .posts import router as posts_controller
from .config import router as config_controller

routers = APIRouter(prefix="/v2", dependencies=[])
routers.include_router(root_controller)
routers.include_router(auth_controller)
routers.include_router(posts_controller)
routers.include_router(config_controller)
