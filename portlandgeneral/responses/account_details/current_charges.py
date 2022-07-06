from decimal import Decimal


class CurrentCharges:

    def __init__(self, current_charges_json: dict):

        self.amount_due = Decimal(str(current_charges_json.get('amountDue')))

        # Value: CurrentCharges
        self.__typename: str = current_charges_json.get('__typename')
