from enum import Enum


class CallbackData(Enum):
    SHOW_SCHEDULE = "show"
    CLOSE_SCHEDULE = "close"
    HIDE_DETAILS = "ok"
    NEXT_DAY = "next"
    PREV_DAY = "prev"
    DAY_PREFIX = "day_"
