# Create an exam typing inherits from TypedDict includes all fields from the exam table

from typing import TypedDict


Exam = TypedDict('Exam', {
    'group': str,
    'subject': str,
    'teacher': str,
    'examDate': str,
    'examTime': str,
    'examRoom': str,
    'consultationDate': str,
    'consultationTime': str,
    'consultationRoom': str,
})
