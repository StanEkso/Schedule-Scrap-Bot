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


def getCurrentWeekNum() -> int:
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

    def atDay(self, index: int) -> str:
        FLAG = config_service.get("SHOW_CURRENT_WEEK_ONLY", False)
        if not FLAG:
            return MESSAGES["current_week_num"] + str(getCurrentWeekNum()) + "\n" + ScheduleAdapter.convert_lessons(self.schedule)[index]

        mappedLessons = [
            lesson for lesson in self.schedule if self.metaToBool(lesson["meta"])]
        return EXCEPTIONS["ONLY_CURRENT_WEEK"] + ScheduleAdapter.convert_lessons(mappedLessons)[index]

    @staticmethod
    def metaToBool(meta: str) -> bool:
        if ("н" in meta):
            CURRENT_WEEK = getCurrentWeekNum()
            if (str(CURRENT_WEEK) in meta):
                return True
            return False

        return True


scheduleService = ScheduleService()
