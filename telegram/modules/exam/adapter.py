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
        header_parts = [exam['subject'], f"({exam['teacher']})"]
        exam_parts = ["Экзамен", exam['exam']['date'], exam['exam']['time'], exam['exam']['room']]
        consult_parts = ["Консультация", exam['consultation']['date'], exam['consultation']['time'], exam['consultation']['room']]

        return "\n".join([" ".join(element) for element in [header_parts, exam_parts, consult_parts]])
