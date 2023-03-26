import asyncio
from bs4 import BeautifulSoup
from ..decorators.cache import Cache, CoroutineCache
from ..decorators.invoke import InvokePerformance, InvokePerformanceAsync
from .parsing import parser
import aiohttp


class SearchService:
    @CoroutineCache(timeout=600000)
    async def grabLinks(self, pageUrl: str) -> list[str]:
        async with aiohttp.ClientSession() as session:
            async with session.get(pageUrl) as response:
                text = await response.text()
                soup = BeautifulSoup(text, features="html.parser")
                contentArea = soup.find("section", {"class": "content"})
                links = contentArea.find_all("a")
                hrefs = [link.get("href") for link in links]
                return [href for href in hrefs if href.startswith(pageUrl)]

    @InvokePerformance
    @CoroutineCache(timeout=600000)
    async def grabGroups(self, pageUrl: str) -> list[str]:
        courses = await self.grabLinks(pageUrl)
        tasks = []
        for course in courses:
            tasks.append(asyncio.ensure_future(self.grabLinks(course)))
        groups = await asyncio.gather(*tasks)
        print(groups)
        return [item for sublist in groups for item in sublist]

    @InvokePerformanceAsync
    @CoroutineCache(timeout=600000)
    async def grabSchedule(self, pageLinks: list[str]):
        tasks = []
        for link in pageLinks:
            tasks.append(asyncio.ensure_future(parser.parseAsync(link)))
        schedules = await asyncio.gather(*tasks)
        return [item for sublist in schedules for item in sublist]
    pass


searchService = SearchService()
