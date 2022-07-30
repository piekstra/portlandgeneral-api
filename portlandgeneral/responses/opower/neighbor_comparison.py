from decimal import Decimal


class NeighborComparison:

    def __init__(self, resp_json: dict):

        # Format like: YYYY-MM-DDT00:00:00.000Z
        self.start_time = resp_json.get('startTime')

        # Format like: YYYY-MM-DDT00:00:00.000Z
        self.end_time = resp_json.get('endTime')

        you_value = resp_json.get('youValue')
        self.you_value: int = int(you_value) if you_value else None

        efficient_value = resp_json.get('efficientValue')
        self.efficient_value: Decimal = Decimal(str(efficient_value)) if efficient_value else None

        neighbors_value = resp_json.get('neighborsValue')
        self.neighbors_value: Decimal = Decimal(str(neighbors_value)) if neighbors_value else None

        number_of_neighbors = resp_json.get('numberOfNeighbors')
        self.number_of_neighbors: int = int(number_of_neighbors) if number_of_neighbors else None
