class SolarAccounts:

    def __init__(self, resp_json: dict):

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.customer_uuid = resp_json.get('customerUuid')

        # TODO: determine list content
        self.solar_accounts = resp_json.get('solarAccounts')
