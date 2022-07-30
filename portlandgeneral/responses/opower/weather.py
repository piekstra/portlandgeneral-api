from decimal import Decimal
from typing import List


class Weather:

    def __init__(self, resp_json: dict):

        self.reads: List[Read] = [Read(read_json) for read_json in resp_json.get('reads')]


class Read:

    def __init__(self, read_json: dict):

        # Format like: YYYY-MM-DDT00:00:00.000Z
        self.date: str = read_json.get('date')

        self.mean_temperature = Decimal(str(read_json.get('meanTemperature')))

        max_temperature = read_json.get('maxTemperature')
        self.max_temperature = Decimal(str(max_temperature)) if max_temperature else None

        min_temperature = read_json.get('minTemperature')
        self.min_temperature = Decimal(str(min_temperature)) if min_temperature else None
