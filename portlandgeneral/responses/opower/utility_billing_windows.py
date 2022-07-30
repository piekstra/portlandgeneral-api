from typing import List


class UtilityBillingWindows:

    def __init__(self, resp_json: dict):

        self.bills: List[BillingWindow] = [BillingWindow(window_json) for window_json in resp_json.get('bills')]
        self.has_billing_data: bool = resp_json.get('hasBillingData')
        self.has_ami_data: bool = resp_json.get('hasAmiData')

        # Example: America/Los_Angeles
        self.time_zone_id: str = resp_json.get('timeZoneId')


class BillingWindow:

    def __init__(self, window_json: dict):

        # UTC Iso8601 Format like: YYYY-MM-DDT00:00:00.000Z
        self.start_date: str = window_json.get('startDate')

        # UTC Iso8601 Format like: YYYY-MM-DDT00:00:00.000Z
        self.end_date: str = window_json.get('endDate')

        self.year: int = window_json.get('year')

        # The count of billing periods in the given year up to and including this window
        self.bill_period: int = window_json.get('billPeriod')
