from typing import TypedDict


class EventInfo(TypedDict):
    date: str
    time: str
    room: str

class Exam(TypedDict):
    """
    The object representing an exam.
    """

    group: str
    subject: str
    teacher: str
    exam: EventInfo
    consultation: EventInfo
