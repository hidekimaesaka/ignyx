from fastapi import FastAPI

from app.routes import health, token, user


def create_app():
    app = FastAPI()

    # including routes
    app.include_router(health.router)
    app.include_router(user.router)
    app.include_router(token.router)

    return app
