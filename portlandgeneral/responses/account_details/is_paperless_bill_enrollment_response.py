

class IsPaperlessBillEnrolledResponse:

    def __init__(self, is_paperless_bill_enrolled_json: dict):
        self.result: bool = is_paperless_bill_enrolled_json.get('result')

        # Value: IsPaperlessBillEnrolledResponse
        self.__typename: str = is_paperless_bill_enrolled_json.get('__typename')
