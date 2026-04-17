from fastapi import FastAPI

from app.routes import health, user


def create_app():
    app = FastAPI()

    # including routes
    app.include_router(health.router)
    app.include_router(user.router)

    return app
