from decimal import Decimal


class ViewBillDetails:

    def __init__(self, bill_details_json: dict):
        self.encrypted_bill_id = bill_details_json.get('encryptedBillId')
        self.download_bill_url: str = bill_details_json.get('downloadBillUrl')

        # Example value: "C"
        self.bill_status: str = bill_details_json.get('billStatus')

        # Format: 01/01/2022
        self.bill_date: str = bill_details_json.get('billDate')

        # Format: 01/01/2022
        self.due_date: str = bill_details_json.get('dueDate')
        self.amount_due: Decimal = Decimal(str(bill_details_json.get('amountDue')))
        self.previous_balance: Decimal = Decimal(str(bill_details_json.get('previousBalance')))
        self.total_adjustments: Decimal = Decimal(str(bill_details_json.get('totalAdjustments')))
        self.total_current_charges: Decimal = Decimal(str(bill_details_json.get('totalCurrentCharges')))
        self.total_balance_after_bill: Decimal = Decimal(str(bill_details_json.get('totalBalanceAfterBill')))
        self.has_bills: bool = bill_details_json.get('hasBills')
        self.kwh: int = bill_details_json.get('kwh')

        # Format: 01/01/2022
        self.billing_period_start_date: str = bill_details_json.get('billingPeriodStartDate')

        # Format: 01/01/2022
        self.billing_period_end_date: str = bill_details_json.get('billingPeriodEndDate')

        # Value: ViewBillDetails
        self.__typename: str = bill_details_json.get('__typename')
