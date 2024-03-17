import asyncio
from bs4 import BeautifulSoup

from shared.helpers.helpers import flatten, split_execution
from ..decorators.cache import CoroutineCache
from .parsing import parser_service
import aiohttp


class SearchService:
    @CoroutineCache(timeout=600000)
    async def grab_links(self, url: str) -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                soup = BeautifulSoup(text, features="html.parser")
                content_area = soup.find("section", {"class": "content"})
                links = content_area.find_all("a")
                href_list: list[str] = [link.get("href") for link in links]
                return [href for href in href_list if href.startswith(url)]

    @CoroutineCache(timeout=600000)
    async def grab_groups(self, page_url: str) -> list[str]:
        courses = await self.grab_links(page_url)
        groups = await split_execution([lambda link=link: asyncio.ensure_future(
            self.grab_links(link)) for link in courses])

        return flatten(groups)

    @CoroutineCache(timeout=600000)
    async def grab_schedule(self, page_links: list[str]):
        schedules = await split_execution([lambda link=link: asyncio.ensure_future(
            parser_service.parse_lessons(link)) for link in page_links], packet_size=10)

        return flatten(schedules)
    pass


search_service = SearchService()
