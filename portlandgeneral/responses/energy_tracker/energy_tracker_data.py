from typing import List

from .energy_tracker_details import EnergyTrackerDetails


class EnergyTrackerData:

    def __init__(self, energy_tracker_data_json: dict):

        self.details_available: bool = energy_tracker_data_json.get('detailsAvailable')
        self.show_energy_tracker: bool = energy_tracker_data_json.get('showEnergyTracker')
        self.has_more_than_15_days_of_data: bool = energy_tracker_data_json.get('hasMoreThan15DaysOfData')

        # Example: OPower
        self.service_provider: str = energy_tracker_data_json.get('serviceProvider')
        self.encrypted_identifiers: List[str] = [
            identifier for identifier in energy_tracker_data_json.get('encryptedIdentifiers')]
        self.details: EnergyTrackerDetails = EnergyTrackerDetails(energy_tracker_data_json.get('details'))

        # Value: EnergyTrackerData
        self.__typename: str = energy_tracker_data_json.get('__typename')
