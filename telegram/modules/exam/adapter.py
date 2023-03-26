from shared.types.exam import Exam


class ExamAdapter:
    """
    The class that converts exam data to a message.
    """

    @staticmethod
    def convert_exams_to_str(exams: list[Exam]) -> str:
        return "\n\n".join([ExamAdapter.convert_exam_to_str(exam) for exam in exams])

    @staticmethod
    def convert_exam_to_str(exam: Exam) -> str:
        return f"{exam['subject']} {exam['teacher']}\nЭкзамен: {exam['examDate']} {exam['examTime']} {exam['examRoom']}\nКонсультация: {exam['consultationDate']} {exam['consultationTime']} {exam['consultationRoom']}"
