from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import router as v1_router
from app.system.config.settings import settings
from app.system.errors.handlers import register_error_handlers
from app.system.middlewares.request_id import RequestIdMiddleware
from app.system.logging.logger import setup_logger



def create_app() -> FastAPI:
    logger = setup_logger()

    app = FastAPI(
        title=settings.app_name,
        version="1.0.0",
    )

    # system wiring
    register_error_handlers(app)
    app.add_middleware(RequestIdMiddleware)

    # routes
    app.include_router(v1_router, prefix="/api/v1")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    logger.info(f"Booted ✅ env={settings.env} host={settings.host} port={settings.port}")
    return app
