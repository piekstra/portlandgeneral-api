from typing import List
from decimal import Decimal


class BillComparison:

    def __init__(self, resp_json: dict):

        self.comparisons: Comparisons = Comparisons(resp_json.get('comparisons'))
        self.reference_data: ReferenceData = ReferenceData(resp_json.get('referenceData'))


class Comparisons:

    def __init__(self, comparisons_json: dict):
        self.accounts: List[Account] = [Account(acct_json) for acct_json in comparisons_json.get('accounts')]


class Account:

    def __init__(self, account_json: dict):

        # Example: KWH
        self.meter_unit: str = account_json.get('meterUnit')
        self.reasons: List[Reason] = [Reason(reason_json) for reason_json in account_json.get('reasons')]

        # TODO: list of something, determine what
        self.insights = account_json.get('insights')

        self.bill_reference: Bill = Bill(account_json.get('billReference'))
        self.bill_compared: Bill = Bill(account_json.get('billCompared'))
        self.difference: Difference = Difference(account_json.get('difference'))

        # Example: ELEC
        self.fuel_type: str = account_json.get('fuelType')

        self.account_number: str = account_json.get('accountNumber')

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.account_uuid: str = account_json.get('accountUUID')

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.customer_uuid: str = account_json.get('customerUUID')

        self.is_solar: bool = account_json.get('isSolar')


class Bill:

    def __init__(self, bill_ref_json: dict):
        self.cost: Decimal = Decimal(str(bill_ref_json.get('cost')))
        self.usage: Decimal = Decimal(str(bill_ref_json.get('usage')))
        self.usage_daily_avg: Decimal = Decimal(str(bill_ref_json.get('usageDailyAvg')))
        self.date_range: DateRange = DateRange(bill_ref_json.get('dateRange'))

        # TODO: list of something, determine what
        self.time_of_use = bill_ref_json.get('timeOfUse')

        # TODO: list of something, determine what
        self.itemization = bill_ref_json.get('itemization')

        self.usage_estimated: bool = bill_ref_json.get('usageEstimated')


class Difference:

    def __init__(self, diff_json: dict):
        self.cost: Decimal = Decimal(str(diff_json.get('cost')))

        # Example: MORE_THAN
        self.explanation: str = diff_json.get('explanation')


class DateRange:

    def __init__(self, date_range_json: dict):

        # Format like: YYYY-MM-DD
        self.start: str = date_range_json.get('start')

        # Format like: YYYY-MM-DD
        self.end: str = date_range_json.get('end')

        self.days: int = date_range_json.get('days')


class Reason:

    def __init__(self, reason_json: dict):

        # Example: NUM_DAYS, OTHER
        self.reason: str = reason_json.get('reason')

        # List of something - TODO: determine what
        self.details = reason_json.get('details')

        self.cost: Decimal = Decimal(str(reason_json.get('cost')))

        # Example: MORE_THAN
        self.explanation: str = reason_json.get('explanation')

        # Example: [ "2" ]
        self.display_values: List[str] = reason_json.get('displayValues')


class ReferenceData:

    def __init__(self, reference_json: dict):

        # Example: $
        self.currency_unit = reference_json.get('currencyUnit')
