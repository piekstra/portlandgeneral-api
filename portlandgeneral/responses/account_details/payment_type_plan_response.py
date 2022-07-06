
class PaymentPlanTypeResponse:

    def __init__(self, equal_pay_json: dict):

        # Example: "RegularPay"
        self.payment_plan_type: str = equal_pay_json.get('paymentPlanType')

        # Value: PaymentPlanTypeResponse
        self.__typename: str = equal_pay_json.get('__typename')
