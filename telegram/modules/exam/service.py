from shared.services.config import configService
from shared.types.exam import Exam
from shared.services.parsing import parser
from .adapter import ExamAdapter


class ExamsService:
    exams: list[Exam]
    url: str

    def __init__(self):
        self.url = configService.get("examsUrl")
        print("[EXAMS] URL: " + self.url)
        self.update()
        pass

    def update(self):
        self.exams = parser.parseExams(self.url)
        pass

    def get(self):
        GROUP = configService.get("GROUP")
        return ExamAdapter.convertExamsToMessage([exam for exam in self.exams if GROUP in exam["group"]])


examsService = ExamsService()
