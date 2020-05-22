from starlette.applications import Starlette
from view import routes
from models import db


def get_app():
    app = Starlette(routes=routes)
    db.init_app(app)
    return app
