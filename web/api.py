import aiohttp_cors
from aiohttp import web
from shared.services.parsing import parser_service
from shared.services.config import ConfigService, config_service
from shared.services.search import search_service
import json
from shared.services.time import TimeService

from shared.types.lesson import Lesson
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
    query = request.rel_url.query

    SCHEDULE_URL = ""

    if 'group' in query and 'course' in query:
        SCHEDULE_URL = ConfigService.construct_schedule_uri(query['course'], query['group'])
    else:
        SCHEDULE_URL = config_service.get("scheduleUrl")
        
    schedule_object = await parser_service.parse_lessons(SCHEDULE_URL)
    response_list = schedule_object
    if "day" in query:
        day = query["day"]

        def is_selected_day(x: Lesson):
            return x["weekday"] == day
        
        response_list = [x for x in response_list if is_selected_day(x)]

    js = json.dumps(response_list)
    return web.Response(body=js, content_type="application/json")


@routes.get("/lessons")
async def lessons(request: web.Request):
    SCHEDULE_URL = config_service.get("SCHEDULE_BASE_LINK")
    scheduleObj = await search_service.grab_groups(SCHEDULE_URL)
    print(scheduleObj)
    lessons = await search_service.grab_schedule(scheduleObj)
    query = request.rel_url.query
    responseList = appendQuery(lessons, query)
    resultObject = {
        "lessons": responseList,
        "count": len(responseList)
    }
    js = json.dumps(resultObject)
    return web.Response(body=js, content_type="application/json")


def distinct(lessons: list[Lesson]) -> list[Lesson]:
    result = []
    for lesson in lessons:
        if lesson not in result:
            result.append(lesson)
    return result


def appendQuery(lessons: list[Lesson], query: dict) -> list[Lesson]:
    if "teacher" in query:
        def isOkay(x: Lesson):
            return query["teacher"] in x["teacher"]
        lessons = [x for x in lessons if isOkay(x)]

    if "day" in query:
        day = query["day"]

        def isSelectedDay(x: Lesson):
            return x["weekday"] == day
        lessons = [x for x in lessons if isSelectedDay(x)]

    if "time" in query:
        time = query["time"]

        def isSelectedTime(x: Lesson):
            return TimeService.isBelongsToPeriod(time, x["time"])
        lessons = [x for x in lessons if isSelectedTime(x)]

    if query.get("distinct", "") != "false":
        lessons = distinct(lessons)
    return lessons
