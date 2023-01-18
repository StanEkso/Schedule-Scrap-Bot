from shared.types.exam import Exam


class ExamAdapter:

    @staticmethod
    def convertExamsToMessage(exams: list[Exam]) -> str:
        return "\n\n".join([ExamAdapter.convertExamToMessage(exam) for exam in exams])

    @staticmethod
    def convertExamToMessage(exam: Exam) -> str:
        return f"{exam['subject']} {exam['teacher']}\nЭкзамен: {exam['examDate']} {exam['examTime']} {exam['examRoom']}\nКонсультация: {exam['consultationDate']} {exam['consultationTime']} {exam['consultationRoom']}"
