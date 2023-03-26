from shared.services.config import config_service
from shared.types.exam import Exam
from shared.services.parsing import parser_service
from .adapter import ExamAdapter
from shared.logger.logger import logger


class ExamsService:
    exams: list[Exam]
    url: str

    def __init__(self):
        self.url = config_service.get("examsUrl")
        logger.init("ExamsUrl: " + self.url)
        self.update()
        pass

    def update(self):
        self.exams = parser_service.parse_exams(self.url)
        pass

    def get(self):
        GROUP = config_service.get("GROUP")
        return ExamAdapter.convertExamsToMessage([exam for exam in self.exams if GROUP in exam["group"]])


examsService = ExamsService()
