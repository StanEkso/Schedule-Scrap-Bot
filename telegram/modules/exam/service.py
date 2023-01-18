from ....shared.types.exam import Exam
from shared.services.parsing import parser


class ExamsService:
    exams: list[Exam]

    def __init__(self):
        self.update()
        pass

    def update(self):
        self.exams = parser.parseExams()
        pass

    def get(self, group: str | int = '2'):
        return [exam for exam in self.exams if group in exam["group"]]


examsService = ExamsService()
