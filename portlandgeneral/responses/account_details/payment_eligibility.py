

class PaymentEligibility:

    def __init__(self, payment_eligibility_json: dict):
        self.is_cash_only: bool = payment_eligibility_json.get('isCashOnly')
        self.is_non_billable_no_balance: bool = payment_eligibility_json.get('isNonBillableNoBalance')

        # Value: PaymentEligibility
        self.__typename: str = payment_eligibility_json.get('__typename')
