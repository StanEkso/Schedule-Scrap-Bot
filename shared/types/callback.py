from enum import Enum
from typing import Optional


class CallbackData(Enum):
    SHOW_SCHEDULE = "show_schedule"
    DAY_PREFIX = "day_"
    NEXT_DAY = "next_day"
    PREV_DAY = "prev_day"
    HIDE_DETAILS = "hide_details"
    CLOSE_SCHEDULE = "close_schedule"

    CLOSE_EXAM = "close_exam"

    @staticmethod
    def fromString(value: str) -> Optional["CallbackData"]:
        for item in CallbackData:
            if item.value == value:
                return item
        return None
