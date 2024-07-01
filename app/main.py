from datetime import datetime
from dotenv import load_dotenv

from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from app.common.exceptions import error_code, APIException
from app.controllers import routers
from app.controllers.root import router as root

# Dotenv Loader
load_dotenv()


# Exception Loader
def init_exception_handler(app: FastAPI) -> bool:
    async def app_exception_handler(_: Request, ex: HTTPException) -> JSONResponse:
        return JSONResponse(
            status_code=ex.status_code,
            content={
                "code": error_code.get(str(ex.status_code)),
                "status": ex.status_code,
                "message": ex.detail,
                "responseAt": datetime.now().isoformat(),
            },
        )

    async def custom_exception_handler(_: Request, ex: APIException) -> JSONResponse:
        return JSONResponse(
            status_code=ex.status,
            content={
                "code": ex.code or error_code.get(str(ex.status)),
                "status": ex.status,
                "message": ex.message,
                "responseAt": datetime.now().isoformat(),
            },
        )

    async def validation_exception_handler(_: Request, ex: RequestValidationError) -> JSONResponse:
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content={
                "code": error_code.get(str(status.HTTP_422_UNPROCESSABLE_ENTITY)),
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "message": ex.errors(),
                "responseAt": datetime.now().isoformat(),
            },
        )

    app.add_exception_handler(RequestValidationError, validation_exception_handler)

    app.add_exception_handler(HTTPException, app_exception_handler)
    app.add_exception_handler(APIException, custom_exception_handler)

    return True


def init_middlewares(app: FastAPI) -> bool:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


# FastAPI Loader
def create_app() -> FastAPI:
    """Load and Create FastAPI Application"""

    app = FastAPI(
        title="Waktaverse Reactions - Backoffice API",
        version="1.0",
    )

    init_exception_handler(app)
    init_middlewares(app)

    app.include_router(root)  # for just / path support
    app.include_router(routers)

    return app


app = create_app()
