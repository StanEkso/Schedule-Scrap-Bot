import aiohttp_cors
from aiohttp import web
from shared.services.parsing import parser
from shared.services.config import configService
import json
routes = web.RouteTableDef()


def bootstrap():
    app = web.Application()
    app.add_routes(routes)
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*"
        )
    })
    for route in list(app.router.routes()):
        cors.add(route)
    return app


@routes.get("/schedule")
async def schedule(request: web.Request):
    SCHEDULE_URL = configService.get("scheduleUrl")
    scheduleObj = parser.parseFromPage(SCHEDULE_URL)
    query = request.rel_url.query
    responseList = scheduleObj
    if "day" in query:
        day = query["day"]
        responseList = [x for x in scheduleObj if x["weekday"] == day]

    js = json.dumps(responseList)
    return web.Response(body=js, content_type="application/json")

