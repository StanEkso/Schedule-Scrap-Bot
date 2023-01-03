from telegram.services.parsing import parser

# Service for schedule.


class ScheduleService:
    # Current schedule.
    schedule: list[str]

    # Generation of schedule via update method.
    def __init__(self) -> None:
        self.update()
        pass

    # Method for updating schedule.
    def update(self) -> list[str]:
        self.schedule = parser.parseFromPage()

    # Method for getting schedule.
    def get(self) -> list[str]:
        return self.schedule

    # Method for getting schedule by day.
    def atDay(self, index: int) -> str:
        try:
            return self.schedule[index]
        except:
            return ""


scheduleService = ScheduleService()
