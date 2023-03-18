import time
from shared.services.config import configService
from shared.localization.service import localization
from shared.services.parsing import parser
from shared.logger.logger import logger
from ...__run__ import FIRST_DAY
from .adapter import ScheduleAdapter
import asyncio
DATE = time.strptime(FIRST_DAY, "%d.%m.%Y")

EXCEPTIONS = localization.getRawExceptions()
MESSAGES = localization.getRawMessages()


def getCurrentWeekNum() -> int:
    currentTime = time.time()
    daysBetweenDates = int((currentTime - time.mktime(DATE)) / 86400)
    TOTAL_PASSED_WEEKS = int(daysBetweenDates / 7)
    return 1 + (TOTAL_PASSED_WEEKS) % 2


class ScheduleService:
    schedule: list[str]
    url: str

    def __init__(self) -> None:
        self.url = configService.get("scheduleUrl")
        logger.init("ScheduleUrl: " + self.url)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.update())
        pass

    async def update(self):
        self.schedule = await parser.parseAsync(self.url)

    def get(self) -> list[str]:
        return self.schedule

    def atDay(self, index: int) -> str:
        FLAG = configService.get("SHOW_CURRENT_WEEK_ONLY", False)
        if not FLAG:
            return MESSAGES["current_week_num"] + str(getCurrentWeekNum()) + "\n" + ScheduleAdapter.convertLessons(self.schedule)[index]

        mappedLessons = [
            lesson for lesson in self.schedule if self.metaToBool(lesson["meta"])]
        return EXCEPTIONS["ONLY_CURRENT_WEEK"] + ScheduleAdapter.convertLessons(mappedLessons)[index]

    @staticmethod
    def metaToBool(meta: str) -> bool:
        if ("н" in meta):
            CURRENT_WEEK = getCurrentWeekNum()
            if (str(CURRENT_WEEK) in meta):
                return True
            return False

        return True


scheduleService = ScheduleService()
