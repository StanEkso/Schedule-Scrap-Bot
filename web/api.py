from aiohttp import web
from shared.services.parsing import parser
import json
routes = web.RouteTableDef()


@routes.get("/endpoint")
async def endpoint(request: web.Request):
    return web.Response(text="Hello, world")


@routes.get("/schedule")
async def schedule(request: web.Request):
    scheduleObj = parser.parseFromPage()

    js = json.dumps(scheduleObj)
    return web.Response(body=js, content_type="application/json")


@routes.post("/gmail")
async def gmail(request: web.Request):
    print(request)
    return web.Response(text="OK", status=200)
