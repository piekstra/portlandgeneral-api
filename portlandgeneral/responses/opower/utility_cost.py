from decimal import Decimal
from typing import List


class UtilityCost:

    def __init__(self, resp_json: dict):

        self.service_point_id: str = resp_json.get('servicePointId')

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.utility_account_uuid: str = resp_json.get('utilityAccountUuid')

        # Example: KWH
        self.unit = resp_json.get('unit')

        # Example: America/Los_Angeles
        self.site_time_zone_id: str = resp_json.get('siteTimeZoneId')

        self.reads: List[Read] = [Read(read_json) for read_json in resp_json.get('reads')]

        series_components = resp_json.get('seriesComponents')
        self.series_components: List[SeriesComponent] = [SeriesComponent(
            component_json) for component_json in series_components] if series_components else None

        rate_plans = resp_json.get('ratePlans')
        self.rate_plans: List[RatePlan] = [RatePlan(plan_json) for plan_json in rate_plans] if rate_plans else None


class Read:

    def __init__(self, read_json: dict):

        # Format like: YYYY-MM-DDT00:00:00.000-07:00
        self.start_time = read_json.get('startTime')

        # Format like: YYYY-MM-DDT00:00:00.000-07:00
        self.end_time = read_json.get('endTime')

        value = read_json.get('value')
        self.value = Decimal(str(value)) if value else None

        # Example: ACTUAL
        self.read_type = read_json.get('readType')

        provided_cost = read_json.get('providedCost')
        self.provided_cost = Decimal(str(provided_cost)) if provided_cost else None

        read_components = read_json.get('readComponents')
        self.read_components: List[ReadComponent] = [ReadComponent(
            component_json) for component_json in read_components] if read_components else None

        is_peak_period = read_json.get('isPeakPeriod')
        self.is_peak_period: bool = bool(is_peak_period) if is_peak_period else None

        rebate_amount = read_json.get('rebateAmount')
        self.rebate_amount: Decimal = Decimal(str(rebate_amount)) if rebate_amount else None
        self.miles_driven: int = int(read_json.get('milesDriven'))


class ReadComponent:

    def __init__(self, component_json: dict):

        # Example: ORDINAL
        self.tier_type: str = component_json.get('tierType')

        # Examples: 1, 2
        self.tier_number: int = int(component_json.get('tierNumber'))

        # TODO: determine type
        self.season: str = component_json.get('season')

        # TODO: determine type
        self.dayPart: str = component_json.get('dayPart')

        cost = component_json.get('cost')
        self.cost = Decimal(str(cost)) if cost else None

        value = component_json.get('value')
        self.value = Decimal(str(value)) if value else None


class SeriesComponent:

    def __init__(self, component_json: dict):

        # Example: TIERED
        self.rate_type = component_json.get('rateType')

        # Examples: 1, 2
        # These are cost tiers - higher usage places you in a higher tier
        self.tier_number: int = int(component_json.get('tierNumber'))

        # TODO: determine type
        self.season = component_json.get('season')

        # TODO: determine type
        self.day_part = component_json.get('dayPart')

        # Format like: YYYY-MM-DDT00:00:00.000-07:00
        self.start_date: str = component_json.get('startDate')

        # Format like: YYYY-MM-DDT00:00:00.000-08:00
        # Seems to just have the value: 2998-12-31T21:00:00.000-08:00
        self.end_date: str = component_json.get('endDate')

        cost = component_json.get('cost')
        self.cost: Decimal = Decimal(str(cost)) if cost else None

        # TODO: determine type
        self.day_part_hours = component_json.get('dayPartHours')


class RatePlan:

    def __init__(self, plan_json: dict):

        self.code: str = plan_json.get('code')

        # TODO: determine type
        self.name = plan_json.get('name')

        # TODO: determine type
        self.description = plan_json.get('description')

        # Example: ELEC
        self.meter_type: str = plan_json.get('meterType')

        # Format like: YYYY-MM-DDT00:00:00.000-08:00
        self.start_date: str = plan_json.get('startDate')

        # Format like: YYYY-MM-DDT00:00:00.000-08:00
        self.end_date: str = plan_json.get('endDate')

        self.is_new: bool = bool(plan_json.get('isNew'))

        # TODO: determine type
        self.ways_to_lower = plan_json.get('waysToLower')

        # TODO: determine content fields
        self.series: dict = plan_json.get('series')
