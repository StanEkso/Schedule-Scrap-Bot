from bs4 import BeautifulSoup
from ..decorators.cache import Cache
from ..decorators.invoke import InvokePerformance
from .parsing import parser
import requests


class SearchService:
    @Cache(timeout=600000)
    def grabLinks(self, pageUrl: str) -> list[str]:
        soup = BeautifulSoup(requests.get(pageUrl).text,
                             features="html.parser")
        contentArea = soup.find("section", {"class": "content"})
        links = contentArea.find_all("a")
        hrefs = [link.get("href") for link in links]
        return [href for href in hrefs if href.startswith(pageUrl)]

    @InvokePerformance
    @Cache(timeout=600000)
    def grabGroups(self, pageUrl: str) -> list[str]:
        courses = self.grabLinks(pageUrl)
        groups = [self.grabLinks(course) for course in courses]
        return [item for sublist in groups for item in sublist]

    @InvokePerformance
    @Cache(timeout=600000)
    def grabSchedule(self, pageLinks: list[str]):
        lessonList = [parser.parseFromPage(link) for link in pageLinks]
        return [item for sublist in lessonList for item in sublist]
    pass


searchService = SearchService()
