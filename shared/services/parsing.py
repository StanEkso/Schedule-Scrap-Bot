import requests
from bs4 import BeautifulSoup
from ..types.exam import Exam
from ..types.lesson import Lesson
from ..decorators.invoke import InvokePerformance, InvokePerformanceAsync
from ..decorators.cache import Cache
import aiohttp


class ParserService:
    @InvokePerformance
    @Cache(timeout=60000)
    def parse_lessons_sync(self, url: str) -> list[Lesson]:
        """
        Deprecated (Synchronous)
        @deprecated
        """
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")

        time = soup.find_all('td', {'class': 'time'})
        remarks = soup.find_all('td', {"class": "remarks"})
        subjectAndTeacher = soup.find_all('td', {"class": "subject-teachers"})
        lessonType = soup.find_all('td', {'class': 'lecture-practice'})
        room = soup.find_all('td', {'class': 'room'})
        weekday = soup.find_all('td', {'class': 'weekday'})

        return [self.map_tuple_to_lesson(i) for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday)]

    @InvokePerformanceAsync
    async def parse_lessons(self, url: str) -> list[Lesson]:
        course, group = ParserService.extract_course_group(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                soup = BeautifulSoup(text, features="html.parser")

                time = soup.find_all('td', {'class': 'time'})
                remarks = soup.find_all('td', {"class": "remarks"})
                subjectAndTeacher = soup.find_all(
                    'td', {"class": "subject-teachers"})
                lessonType = soup.find_all('td', {'class': 'lecture-practice'})
                room = soup.find_all('td', {'class': 'room'})
                weekday = soup.find_all('td', {'class': 'weekday'})

                result = [self.map_tuple_to_lesson(i, course, group) for i in zip(
                    time, remarks, subjectAndTeacher, lessonType, room, weekday)]
                return result

    @staticmethod
    def convert_lesson_type(lesson_type: str) -> str:
        if lesson_type == "л":
            return "Лекция"
        elif lesson_type == "п":
            return "Практика"
        elif lesson_type == "лаб":
            return "Практика (лаб.)"
        elif lesson_type == "с":
            return "Семинар"
        return ""

    @InvokePerformance
    def parse_exams(self, url: str) -> list[Exam]:
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")

        table = soup.find("table")
        table_rows = table.find_all("tr")
        exams: list[Exam] = []
        current_group = ""
        for row in table_rows:
            cells = row.find_all("td")
            headers = row.find_all("th")
            if (len(headers) > 0):
                current_group = self.tag_to_text(headers[0])
                continue
            if len(cells) == 0:
                continue
            else:
                TEXTS = [self.tag_to_text(CELL) for CELL in cells]
                exams.append({
                    "group": current_group,
                    "subject": TEXTS[0],
                    "teacher": TEXTS[1],
                    "consultation": {
                        "date": TEXTS[5],
                        "time": TEXTS[6],
                        "room": TEXTS[7],
                    },
                    "exam": {
                        "date": TEXTS[2],
                        "time": TEXTS[3],
                        "room": TEXTS[4],
                    }
                })
        return exams

    @staticmethod
    def tag_to_text(tag) -> str:
        return tag.text.replace("\n", "")

    @staticmethod
    def map_tuple_to_lesson(lesson_tuple: tuple, course: str = "", group: str = "") -> Lesson:
        time, remarks, subject_n_teacher, lesson_type, room, weekday = lesson_tuple
        for br in subject_n_teacher.find_all("br"):
            br.replace_with(" %s\n" % br.text)

        lesson_extras = subject_n_teacher.text.split("\n")

        time, remarks, subject_n_teacher, lesson_type, room, weekday = [
            ParserService.tag_to_text(item) for item in lesson_tuple]

        # Using lower() method for getting day in lower case.
        # Used for getting day from dictionary.
        weekday = weekday.lower()
        lesson: Lesson = {
            "time": time,
            "meta": remarks,
            "subject": subject_n_teacher.replace(lesson_extras[1] if len(lesson_extras) > 1 else "", "").strip(),
            "type": ParserService.convert_lesson_type(lesson_type),
            "room": room,
            "weekday": weekday,
            "teacher": lesson_extras[1] if len(lesson_extras) > 1 else "",
            "course": course,
            "group": group
        }
        return lesson

    @staticmethod
    def extract_course_group(url: str) -> tuple[str, str]:
        # TODO: Proper handle
        parts = url.split("/")
        course_str = parts[-3]
        group_str = parts[-2]
        return course_str.split("-")[0], group_str.split("-")[0]


parser_service = ParserService()
