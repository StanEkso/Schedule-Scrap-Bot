import time
from shared.services.config import config_service
from shared.localization.service import localization_service
from shared.services.parsing import parser_service
from shared.logger.logger import logger
from ...__run__ import FIRST_DAY
from .adapter import ScheduleAdapter
import asyncio
import datetime

DATE_TIME = datetime.datetime.strptime(FIRST_DAY, "%d.%m.%Y")

EXCEPTIONS = localization_service.get_exceptions_dict()
MESSAGES = localization_service.get_messages_dict()


def to_current_week_num() -> int:
    currentTime = datetime.datetime.now()
    week_between_dates = currentTime.isocalendar().week - DATE_TIME.isocalendar().week
    return week_between_dates % 2 + 1


class ScheduleService:
    schedule: list[str]
    url: str

    def __init__(self) -> None:
        self.url = config_service.get("scheduleUrl")
        logger.init("ScheduleUrl: " + self.url)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.update())
        pass

    async def update(self):
        self.schedule = await parser_service.parse_lessons(self.url)

    def get(self) -> list[str]:
        return self.schedule

    def at_day(self, index: int) -> str:
        show_current_week_only = config_service.get(
            "SHOW_CURRENT_WEEK_ONLY", False)
        if not show_current_week_only:
            return MESSAGES["current_week_num"] + str(to_current_week_num()) + "\n" + ScheduleAdapter.convert_lessons(self.schedule)[index]

        mappedLessons = [
            lesson for lesson in self.schedule if self.meta_to_bool(lesson["meta"])]
        return EXCEPTIONS["ONLY_CURRENT_WEEK"] + ScheduleAdapter.convert_lessons(mappedLessons)[index]

    @staticmethod
    def meta_to_bool(meta: str) -> bool:
        if ("н" in meta):
            current_week = to_current_week_num()

            return str(current_week) in meta

        return True


scheduleService = ScheduleService()
