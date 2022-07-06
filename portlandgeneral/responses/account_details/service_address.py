

class ServiceAddress:

    def __init__(self, service_addresses_json: dict):
        self.address_line_1: str = service_addresses_json.get('addressLine1')
        self.address_line_2: str = service_addresses_json.get('addressLine2')
        self.city: str = service_addresses_json.get('city')
        self.state: str = service_addresses_json.get('state')
        self.postal: str = service_addresses_json.get('postal')

        # Value: ServiceAddress
        self._typename: str = service_addresses_json.get('__typename')
