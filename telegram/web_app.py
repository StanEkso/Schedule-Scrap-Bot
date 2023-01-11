from aiohttp import web

from aiohttp.web_fileresponse import FileResponse

routes = web.RouteTableDef()


@routes.get("/endpoint")
async def endpoint(request: web.Request):
    return web.Response(text="Hello, world")
