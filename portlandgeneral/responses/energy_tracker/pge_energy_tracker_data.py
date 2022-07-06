from typing import List

from .billable_account_info import BillableAccountInfo


class PgeEnergyTrackerData:

    def __init__(self, pge_energy_tracker_data_json: dict):

        self.show_energy_tracker: bool = pge_energy_tracker_data_json.get('showEnergyTracker')

        # Example: OPower
        self.service_provider: str = pge_energy_tracker_data_json.get('serviceProvider')
        self.identifiers: List[str] = [identifier for identifier in (pge_energy_tracker_data_json.get('identifiers'))]
        self.billable_account_details: BillableAccountInfo = BillableAccountInfo(
            pge_energy_tracker_data_json.get('billableAccountDetails'))

        # Value: PgeEnergyTrackerData
        self.__typename: str = pge_energy_tracker_data_json.get('__typename')
