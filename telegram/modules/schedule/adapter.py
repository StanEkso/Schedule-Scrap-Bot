from shared.types.lesson import Lesson, lessonToString
from shared.localization.service import localization


class ScheduleAdapter:
    def __init__() -> None:
        pass

    @staticmethod
    def convertLessons(lessons: list[Lesson]) -> list[str]:
        days = {
            "понедельник": localization.getMessage("mon"),
            "вторник": localization.getMessage("tue"),
            "среда": localization.getMessage("wed"),
            "четверг": localization.getMessage("thu"),
            "пятница": localization.getMessage("fri"),
            "суббота": localization.getMessage("sat"),
        }
        for lesson in lessons:
            days[lesson["weekday"]] += lessonToString(lesson) + "\n"
        return list(days.values())
