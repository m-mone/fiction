from sanic import Blueprint

index_blue = Blueprint("news", url_prefix="")

from . import views
