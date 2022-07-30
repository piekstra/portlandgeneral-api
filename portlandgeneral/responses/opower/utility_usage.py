from decimal import Decimal
from typing import List


class UtilityUsage:

    def __init__(self, resp_json: dict):

        # Format like: YYYY-MM-DD
        self.start_date = resp_json.get('startDate')

        # Format like: YYYY-MM-DD
        self.end_date = resp_json.get('endDate')

        self.reads: List[UsageRead] = [UsageRead(read_json) for read_json in resp_json.get('reads')]

        # Example: America/Los_Angeles
        self.site_time_zone_id: str = resp_json.get('siteTimeZoneId')

        self.units: Units = Units(resp_json.get('units'))

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.utility_account_uuid: str = resp_json.get('utilityAccountUuid')

        self.utility_service_point_id: str = resp_json.get('utilityServicePointId')


class UsageRead:

    def __init__(self, read_json: dict):

        # Format like: YYYY-MM-DDT00:00:00.000-08:00
        self.start_time = read_json.get('startTime')

        # Format like: YYYY-MM-DDT00:00:00.000-08:00
        self.end_time = read_json.get('endTime')

        self.consumption: Consumption = Consumption(read_json.get('consumption'))

        # TODO: determine type
        self.demand = read_json.get('demand')

        # TODO: determine type
        self.exported = read_json.get('exported')

        # TODO: determine type
        self.gross_consumption = read_json.get('grossConsumption')

        # TODO: determine type
        self.gross_generation = read_json.get('grossGeneration')

        # TODO: determine type
        self.imported = read_json.get('imported')

        # TODO: determine type
        self.reactive_power = read_json.get('reactivePower')

        provided_cost = read_json.get('providedCost')
        self.provided_cost = Decimal(str(provided_cost)) if provided_cost else None

        self.miles_driven: int = int(read_json.get('milesDriven'))


class Units:

    def __init__(self, units_json: dict):

        # Example: KWH
        self.consumption: str = units_json.get('consumption')

        # TODO: determine type
        self.demand = units_json.get('demand')

        # TODO: determine type
        self.exported = units_json.get('exported')

        # TODO: determine type
        self.gross_consumption = units_json.get('grossConsumption')

        # TODO: determine type
        self.gross_generation = units_json.get('grossGeneration')

        # TODO: determine type
        self.imported = units_json.get('imported')

        # TODO: determine type
        self.reactive_power = units_json.get('reactivePower')


class Consumption:

    def __init__(self, consumption_json: dict):

        value = consumption_json.get('value')
        self.value = Decimal(str(value)) if value else None

        # Example: ACTUAL
        self.type = consumption_json.get('type')
