import datetime
from flask import Blueprint
from ..cache import cache


frontend = Blueprint('frontend', __name__)


@cache.cached(timeout=50)
@frontend.route("/")
def index():
    now = str(datetime.datetime.now())
    return now
