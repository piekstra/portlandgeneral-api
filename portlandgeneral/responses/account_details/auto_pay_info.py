

class AutoPayInfo:

    def __init__(self, auto_pay_json: dict):
        self.isEnrolled: bool = auto_pay_json.get('isEnrolled')

        # Value: AutoPayInfo
        self.__typename: str = auto_pay_json.get('__typename')
