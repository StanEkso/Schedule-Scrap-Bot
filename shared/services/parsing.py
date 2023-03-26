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

                return [self.map_tuple_to_lesson(i) for i in zip(time, remarks, subjectAndTeacher, lessonType, room, weekday)]

    @staticmethod
    def convert_lesson_type(lessonType: str) -> str:
        if lessonType == "л":
            return "Лекция"
        elif lessonType == "п":
            return "Практика"
        else:
            return ""

    @InvokePerformance
    def parse_exams(self, url: str) -> list[Exam]:
        soup = BeautifulSoup(requests.get(url).text, features="html.parser")

        TABLE = soup.find("table")
        ROWS = TABLE.find_all("tr")
        exams: list[Exam] = []
        CURRENT_GROUP = ""
        for ROW in ROWS:
            CELLS = ROW.find_all("td")
            if (len(CELLS) == 1):
                CURRENT_GROUP = self.tag_to_text(CELLS[0])
                continue
            else:
                TEXTS = [self.tag_to_text(CELL) for CELL in CELLS]
                exams.append({
                    "group": CURRENT_GROUP,
                    "subject": TEXTS[0],
                    "teacher": TEXTS[1],
                    "examDate": TEXTS[2],
                    "examTime": TEXTS[3],
                    "examRoom": TEXTS[4],
                    "consultationDate": TEXTS[5],
                    "consultationTime": TEXTS[6],
                    "consultationRoom": TEXTS[7],
                })
        return exams

    @staticmethod
    def tag_to_text(tag) -> str:
        return tag.text.replace("\n", "")

    @staticmethod
    def map_tuple_to_lesson(lessonTuple: tuple) -> Lesson:
        time, remarks, subjectAndTeacher, lessonType, room, weekday = lessonTuple
        for br in subjectAndTeacher.find_all("br"):
            br.replace_with(" %s\n" % br.text)

        lessonExtraTuple = subjectAndTeacher.text.split("\n")

        time, remarks, subjectAndTeacher, lessonType, room, weekday = [
            ParserService.tag_to_text(item) for item in lessonTuple]

        # Using lower() method for getting day in lower case.
        # Used for getting day from dictionary.
        weekday = weekday.lower()
        lesson: Lesson = {
            "time": time,
            "meta": remarks,
            "subject": subjectAndTeacher,
            "type": ParserService.convert_lesson_type(lessonType),
            "room": room,
            "weekday": weekday,
            "teacher": lessonExtraTuple[1] if len(lessonExtraTuple) > 1 else ""
        }
        return lesson


parser_service = ParserService()
