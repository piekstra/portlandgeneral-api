from decimal import Decimal


class EnergyTrackerDetails:

    def __init__(self, energy_tracker_details_json: dict):

        self.billing_cycle_day: int = energy_tracker_details_json.get('billingCycleDay')
        self.number_of_billing_days: int = energy_tracker_details_json.get('numberOfBillingDays')

        # Format: "2022-01-01T00:00:00-07:00"
        self.last_read_date: str = energy_tracker_details_json.get('lastReadDate')
        self.bill_to_date_amount: Decimal = Decimal(str(energy_tracker_details_json.get('billToDateAmount')))
        self.projected_amount: Decimal = Decimal(str(energy_tracker_details_json.get('projectedAmount')))
        self.min_projected_amount: Decimal = Decimal(str(energy_tracker_details_json.get('minProjectedAmount')))
        self.max_projected_amount: Decimal = Decimal(str(energy_tracker_details_json.get('maxProjectedAmount')))
        self.billing_progress: int = energy_tracker_details_json.get('billingProgress')

        # Value: EnergyTrackerDetails
        self.__typename: str = energy_tracker_details_json.get('__typename')
