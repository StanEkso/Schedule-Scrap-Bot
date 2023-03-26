from shared.types.lesson import Lesson, lessonToString
from shared.localization.service import localization_service


class ScheduleAdapter:
    def __init__() -> None:
        pass

    @staticmethod
    def convertLessons(lessons: list[Lesson]) -> list[str]:
        days = {
            "понедельник": localization_service.get_message("mon"),
            "вторник": localization_service.get_message("tue"),
            "среда": localization_service.get_message("wed"),
            "четверг": localization_service.get_message("thu"),
            "пятница": localization_service.get_message("fri"),
            "суббота": localization_service.get_message("sat"),
        }
        for lesson in lessons:
            days[lesson["weekday"]] += lessonToString(lesson) + "\n"
        return list(days.values())
