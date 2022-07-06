from decimal import Decimal

from .view_bill_details import ViewBillDetails


class BillInfo:

    def __init__(self, bill_info_json: dict):
        self.amount_due: Decimal = Decimal(str(bill_info_json.get('amountDue')))

        # Format: 2022-01-01T00:00:00
        self.due_date: str = bill_info_json.get('dueDate')

        # Format: 2022-01-01T00:00:00
        self.last_payment_date: str = bill_info_json.get('lastPaymentDate')
        self.last_payment_amount: Decimal = Decimal(str(bill_info_json.get('lastPaymentAmount')))
        self.is_account_payable: bool = bill_info_json.get('isAccountPayable')
        self.is_new_account: bool = bill_info_json.get('isNewAccount')
        self.one_time_future_payment_scheduled: bool = bill_info_json.get('oneTimeFuturePaymentScheduled')
        self.multiple_future_payments_scheduled: bool = bill_info_json.get('multipleFuturePaymentsScheduled')
        self.enrolled_in_pta: bool = bill_info_json.get('enrolledInTPA')
        self.bill_details: ViewBillDetails = ViewBillDetails(bill_info_json.get('billDetails'))

        # Value: BillInfo
        self.__typename: str = bill_info_json.get('__typename')
