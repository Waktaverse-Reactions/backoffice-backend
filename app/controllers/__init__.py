from fastapi import APIRouter

from .root import router as root_controller
from .auth import router as auth_controller

routers = APIRouter(prefix="/v2", dependencies=[])
routers.include_router(root_controller)
routers.include_router(auth_controller)
