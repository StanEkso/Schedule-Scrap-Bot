from services.parsing import parser
from services.message import messageService
from bs4 import BeautifulSoup


def formStringFromArray(arr: list) -> str:
    return " ".join(arr)


class ScheduleService:
    schedule: list[str]

    def __init__(self) -> None:
        self.update()
        pass

    def update(self) -> list[str]:
        self.schedule = parser.parseFromPage()

    def get(self) -> list[str]:
        return self.schedule

    def atDay(self, index: int) -> str:
        return self.schedule[index]


scheduleService = ScheduleService()
