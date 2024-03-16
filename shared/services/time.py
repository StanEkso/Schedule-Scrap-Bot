class TimeService:
    @staticmethod
    def isBelongsToPeriod(time: str, period: str) -> bool:
        # time is string in format "hh:mm"
        # period is string in format "hh:mm-hh:mm"
        try:
            start, end = period.split("–")
            start_time = TimeService.map_time_to_minutes(start)
            end_time = TimeService.map_time_to_minutes(end)
            current_time = TimeService.map_time_to_minutes(time)

            return start_time <= current_time <= end_time
        except Exception as e:
            return True

    @staticmethod
    def map_time_to_minutes(time: str) -> int:
        # time is string in format "hh:mm"
        hours, minutes = time.split(":")
        return int(hours) * 60 + int(minutes)

    @staticmethod
    def map_minutes_to_time_str(minutes: int) -> str:
        # minutes is integer
        hours = minutes // 60
        minutes = minutes % 60
        return f"{hours}:{minutes}"
