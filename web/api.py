from aiohttp import web
from shared.services.parsing import parser
routes = web.RouteTableDef()


@routes.get("/endpoint")
async def endpoint(request: web.Request):
    return web.Response(text="Hello, world")

@routes.get("/schedule")
async def schedule(request: web.Request):
    scheduleObj = parser.parseFromPage();
    return web.Response(body=scheduleObj, content_type="application/json")