

class TimeOfDayInfo:

    def __init__(self, time_of_day_info_json: dict):

        # Example: Unenrolled
        self.enrollment_status: str = time_of_day_info_json.get('enrollmentStatus')

        # Value: TimeOfDayInfo
        self.__typename: str = time_of_day_info_json.get('__typename')
