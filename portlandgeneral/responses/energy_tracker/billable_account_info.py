class BillableAccountInfo:

    def __init__(self, billable_account_info_json: dict):

        self.is_account_billable: bool = billable_account_info_json.get('isAccountBillable')
        self.is_service_designation_electric: bool = billable_account_info_json.get('isServiceDesignationElectric')
        self.is_account_on_flex_price_plan: bool = billable_account_info_json.get('isAccountOnFlexPricePlan')
        self.is_non_spo: bool = billable_account_info_json.get('isNonSpo')

        # Value: BillableAccountInfo
        self.__typename: str = billable_account_info_json.get('__typename')
