from typing import List


class CurrentCustomers:

    def __init__(self, resp_json: dict):

        self.id: int = resp_json.get('id')

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.uuid: str = resp_json.get('uuid')

        self.legacy_opower_id: str = resp_json.get('legacyOpowerId')
        self.account_number: str = resp_json.get('accountNumber')
        self.account_name: str = resp_json.get('accountName')
        self.address: Address = Address(resp_json.get('address'))

        # Example: RESIDENTIAL
        self.type: int = resp_json.get('type')

        self.utility_accounts: List[UtilityAccount] = [UtilityAccount(account_json)
                                                       for account_json in resp_json.get('utilityAccounts')]


class Address:

    def __init__(self, address_json: dict):

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.uuid: str = address_json.get('uuid')

        self.street_number: str = address_json.get('streetNumber')
        self.street_name: str = address_json.get('streetName')
        self.subpremise: str = address_json.get('subpremise')
        self.postal_code: str = address_json.get('postalCode')
        self.city: str = address_json.get('city')

        # Two-letter
        self.country: str = address_json.get('country')

        # Two-letter
        self.state: str = address_json.get('state')


class UtilityAccount:

    def __init__(self, account_json: dict):
        self.id: int = account_json.get('id')

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.uuid: str = account_json.get('uuid')

        self.utility_account_id: str = account_json.get('utilityAccountId')

        # May be the same ID as utilityAccountId
        self.utility_account_id_2: str = account_json.get('utilityAccountId2')

        self.service_point_id: int = account_json.get('servicePointId')

        # Example: ELEC
        self.meter_type: str = account_json.get('meterType')

        # May be the same ID as utilityAccountId and utilityAccountId2
        self.preferred_utility_account_id: str = account_json.get('preferredUtilityAccountId')

        # Example: HOUR
        self.read_resolution: str = account_json.get('readResolution')
        ""
