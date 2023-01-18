import time
from shared.services.config import configService
from shared.localization.service import localization
from shared.services.parsing import parser
from .adapter import ScheduleAdapter

DATE = time.strptime("29.08.2022", "%d.%m.%Y")
print("First week of 2022-2023 school year: " +
      str(int(time.mktime(DATE) / 604800)))


def getCurrentWeekNum() -> int:
    currentTime = time.time()
    currentWeekNum = int(currentTime / 604800)
    firstWeekNum = int(time.mktime(DATE) / 604800)
    return 1 + (currentWeekNum - firstWeekNum) % 2


class ScheduleService:
    schedule: list[str]

    # Generation of schedule via update method.
    def __init__(self) -> None:
        self.update()
        pass

    # Method for updating schedule.
    def update(self) -> list[str]:
        self.schedule = (parser.parseFromPage())

    # Method for getting schedule.
    def get(self) -> list[str]:
        return self.schedule

    # Method for getting schedule by day.
    def atDay(self, index: int) -> str:
        FLAG = configService.get("SHOW_CURRENT_WEEK_ONLY", False)
        if not FLAG:
            return ScheduleAdapter.convertLessons(self.schedule)[index]

        mappedLessons = [
            lesson for lesson in self.schedule if self.metaToBool(lesson["meta"])]
        return localization.getRawExceptions()["ONLY_CURRENT_WEEK"] + ScheduleAdapter.convertLessons(mappedLessons)[index]

    @staticmethod
    def metaToBool(meta: str) -> bool:
        if ("н" in meta):
            CURRENT_WEEK = getCurrentWeekNum()
            print("Current week: " + str(CURRENT_WEEK))
            if (str(CURRENT_WEEK) in meta):
                return True
            return False

        return True


scheduleService = ScheduleService()
