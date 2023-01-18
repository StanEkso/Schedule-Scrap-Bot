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
