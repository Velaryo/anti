from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config

#todo ROUTES
from app.routes.index import index_router


# todo api
from app.routes.rickoso import rickoso_router


def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)

    #todo BLUEPRINT
    app.register_blueprint(index_router)
    app.register_blueprint(rickoso_router)

    return app
