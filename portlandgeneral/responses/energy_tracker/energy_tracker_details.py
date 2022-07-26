from decimal import Decimal


class EnergyTrackerDetails:

    def __init__(self, energy_tracker_details_json: dict):

        self.billing_cycle_day: int = energy_tracker_details_json.get('billingCycleDay')
        self.number_of_billing_days: int = energy_tracker_details_json.get('numberOfBillingDays')

        # Format: "2022-01-01T00:00:00-07:00"
        self.last_read_date: str = energy_tracker_details_json.get('lastReadDate')

        bill_to_date_amount = energy_tracker_details_json.get('billToDateAmount')
        self.bill_to_date_amount: Decimal = Decimal(str(bill_to_date_amount)) if bill_to_date_amount is not None else None

        projected_amount = energy_tracker_details_json.get('projectedAmount')
        self.projected_amount: Decimal = Decimal(str(projected_amount)) if projected_amount is not None else None

        min_projected_amount = energy_tracker_details_json.get('minProjectedAmount')
        self.min_projected_amount: Decimal = Decimal(str(min_projected_amount)) if min_projected_amount is not None else None

        max_projected_amount = energy_tracker_details_json.get('maxProjectedAmount')
        self.max_projected_amount: Decimal = Decimal(str(max_projected_amount)) if max_projected_amount is not None else None

        self.billing_progress: int = energy_tracker_details_json.get('billingProgress')

        # Value: EnergyTrackerDetails
        self.__typename: str = energy_tracker_details_json.get('__typename')
