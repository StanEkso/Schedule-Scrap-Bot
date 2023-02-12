class TimeService:
    @staticmethod
    def isBelongsToPeriod(time: str, period: str) -> bool:
        # time is string in format "hh:mm"
        # period is string in format "hh:mm-hh:mm"
        try:
            start, end = period.split("–")
            startTime = TimeService.timeToMinutes(start)
            endTime = TimeService.timeToMinutes(end)
            currentTime = TimeService.timeToMinutes(time)

            return startTime <= currentTime <= endTime
        except Exception as e:
            return True

    @staticmethod
    def timeToMinutes(time: str) -> int:
        # time is string in format "hh:mm"
        hours, minutes = time.split(":")
        return int(hours) * 60 + int(minutes)

    @staticmethod
    def minutesToTime(minutes: int) -> str:
        # minutes is integer
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours}:{minutes}"
