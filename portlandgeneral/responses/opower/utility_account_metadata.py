from typing import List


class UtilityAccountMetadata:

    def __init__(self, resp_json: dict):

        # Example: [ "ELECTRICITY" ]
        self.available_fuel_types: List[str] = resp_json.get('availableFuelTypes')

        # Keys should be found in available_fuel_types
        self.fuel_type_service_point: dict = {}
        for fuel_type in self.available_fuel_types:
            sp_json_list = resp_json.get('fuelTypeServicePoint')[fuel_type]
            self.fuel_type_service_point[fuel_type] = [FuelTypeServicePoint(sp_json) for sp_json in sp_json_list]

        # Example: America/Los_Angeles
        self.time_zone_id: str = resp_json.get('timeZoneId')


class FuelTypeServicePoint:

    def __init__(self, sp_json: dict):

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.account_uuid: str = sp_json.get('accountUuid')

        # Example: ELECTRICITY
        self.fuel_type: str = sp_json.get('fuelType')

        self.service_point_id: str = sp_json.get('servicePointId')

        self.preferred_utility_account_id: str = sp_json.get('preferredUtilityAccountId')

        # Format like: YYYY-MM-DDT00:00:00-08:00
        # The first date of service
        self.active_date: str = sp_json.get('activeDate')

        # Example: HOUR
        self.read_resolution: str = sp_json.get('readResolution')

        self.has_ami_usage: bool = sp_json.get('hasAmiUsage')
        self.has_bill_usage: bool = sp_json.get('hasBillUsage')

        # Format like: YYYY-MM-DD
        self.date_of_first_ami_read: str = sp_json.get('dateOfFirstAmiRead')

        # Format like: YYYY-MM-DD
        self.date_of_last_ami_read: str = sp_json.get('dateOfLastAmiRead')
