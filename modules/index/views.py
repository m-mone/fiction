from config import Config
from main import jinja
from . import index_blue

index_blue.static("/static/news", Config.BASE_DIR + "/static/news")


@index_blue.route("/")
async def index(request):
    return jinja.render("news/index.html", request)
