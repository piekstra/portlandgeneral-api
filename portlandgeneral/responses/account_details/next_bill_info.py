class NextBillInfo:

    def __init__(self, next_bill_json: dict):

        # Format: 2022-01-01T00:00:00
        self.bill_date: str = next_bill_json.get('billDate')

        # Value: NextBillInfo
        self.__typename: str = next_bill_json.get('__typename')
