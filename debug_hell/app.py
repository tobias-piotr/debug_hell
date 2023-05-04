from fastapi import FastAPI

from debug_hell.api.routes import router
from debug_hell.config import settings


def create_app() -> FastAPI:
    """Create and start app."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url=f"{settings.API_PREFIX}/api/docs",
        openapi_url=f"{settings.API_PREFIX}/api/openapi.json",
    )
    app.include_router(router, prefix=settings.API_PREFIX)
    return app


app = create_app()
