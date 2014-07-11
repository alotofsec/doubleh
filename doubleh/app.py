from flask import Flask

from frontend.views import frontend
from extensions import db
from cache import cache

__all__ = ['create_app']

DEFAULT_BLUEPRINTS = (
    frontend,
)

def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""


    app = Flask(__name__)


    # flask-cache
    #cache.init_app(app, config={'CACHE_TYPE': 'simple'})


    #flask-sqlalchemy
    db.init_app(app)


    for blueprint in DEFAULT_BLUEPRINTS:
        app.register_blueprint(blueprint)


    return app
