from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from sanic_session import InMemorySessionInterface

from modules.index import index_blue

app = Sanic()
jinja = SanicJinja2(app)
session = InMemorySessionInterface(cookie_name=app.name, prefix=app.name)
app.blueprint(index_blue)


@app.middleware("request")
async def add_session_to_request(request):
    await session.open(request)


@app.middleware("response")
async def save_session(request, response):
    await session.save(request, response)


if __name__ == '__main__':
    app.run("0.0.0.0", 8000)
