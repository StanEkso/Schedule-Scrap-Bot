from aiohttp import web
from shared.services.parsing import parser
import json
routes = web.RouteTableDef()


def bootstrap():
    app = web.Application()
    app.add_routes(routes)
    return app


@routes.get("/schedule")
async def schedule(request: web.Request):
    scheduleObj = parser.parseFromPage()
    query = request.rel_url.query
    responseList = scheduleObj
    if "day" in query:
        day = query["day"]
        responseList = [x for x in scheduleObj if x["weekday"] == day]

    js = json.dumps(responseList)
    return web.Response(body=js, content_type="application/json")
