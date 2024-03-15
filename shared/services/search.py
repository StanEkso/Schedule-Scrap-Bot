import asyncio
from bs4 import BeautifulSoup

from shared.helpers.helpers import flatten, split_execution
from ..decorators.cache import CoroutineCache
from .parsing import parser_service
import aiohttp


class SearchService:
    @CoroutineCache(timeout=600000)
    async def grab_links(self, pageUrl: str) -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(pageUrl) as response:
                text = await response.text()
                soup = BeautifulSoup(text, features="html.parser")
                content_area = soup.find("section", {"class": "content"})
                links = content_area.find_all("a")
                href_list: list[str] = [link.get("href") for link in links]
                return [href for href in href_list if href.startswith(pageUrl)]

    @CoroutineCache(timeout=600000)
    async def grab_groups(self, pageUrl: str) -> list[str]:
        courses = await self.grab_links(pageUrl)
        groups = await split_execution([lambda link=link: asyncio.ensure_future(
                self.grab_links(link)) for link in courses])
        
        return flatten(groups)

    @CoroutineCache(timeout=600000)
    async def grab_schedule(self, pageLinks: list[str]):
        schedules = await split_execution([lambda link=link: asyncio.ensure_future(
                parser_service.parse_lessons(link)) for link in pageLinks], packet_size=10)

        return flatten(schedules)
    pass


search_service = SearchService()
