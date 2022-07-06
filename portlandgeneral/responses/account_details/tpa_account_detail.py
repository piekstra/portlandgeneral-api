class TpaAccountDetail:

    def __init__(self, tpa_account_detail_json: dict):
        self.is_eligible: bool = tpa_account_detail_json.get('isEligible')
        self.is_enrolled: bool = tpa_account_detail_json.get('isEnrolled')

        # TODO: determine type - probably a float that should be captured as a Decimal
        self.account_balance = tpa_account_detail_json.get('accountBalance')

        # TODO: determine type
        self.recommended_payment_months = tpa_account_detail_json.get('recommendedPaymentMonths')

        # TODO: determine type
        self.enrolled_installment_details = tpa_account_detail_json.get('enrolledInstallmentDetails')

        # Value: TPA_AccountDetail
        self.__typename: str = tpa_account_detail_json.get('__typename')
