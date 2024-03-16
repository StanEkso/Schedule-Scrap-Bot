from enum import Enum
from typing import Optional


class CallbackData(Enum):
    """
    The object representing a callback data.
    """

    ShowSchedule = "show_schedule"
    DayPrefix = "day_"
    NextDay = "next_day"
    PrevDay = "prev_day"
    HideDetails = "hide_details"
    CloseSchedule = "close_schedule"
    CloseExam = "close_exam"

    @staticmethod
    def from_string(value: str) -> Optional["CallbackData"]:
        for item in CallbackData:
            if item.value == value:
                return item
        return None
