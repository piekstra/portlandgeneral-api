from typing import List

from .person_contact import PersonContact
from .group import Group
from .account_meta import AccountMeta


class AccountCustomer:

    def __init__(self, account_customer_json: dict):

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.uid: str = account_customer_json.get('uid')

        # Example: en-US
        self.language: str = account_customer_json.get('language')

        # Example: English
        self.pref_language: str = account_customer_json.get('prefLanguage')
        self.email: str = account_customer_json.get('email')
        self.person_name: str = account_customer_json.get('personName')

        # Appears to be an int, but comes across as a string
        self.person_id: str = account_customer_json.get('personId')
        self.encrypted_person_id: str = account_customer_json.get('encryptedPersonId')

        # Format: 2022-01-01T00:00:00.000Z
        self.timestamp: str = account_customer_json.get('timestamp')
        self.account_meta: AccountMeta = AccountMeta(account_customer_json.get('accountMeta'))

        # Format: 2022-01-01
        self.last_confirmed_date: str = account_customer_json.get('lastConfirmedDate')
        self.groups: List[Group] = [Group(j) for j in account_customer_json.get('groups')]
        self.contact_details: List[PersonContact] = [PersonContact(j) for j in account_customer_json.get('contactDetails')]

        # Value: AccountCustomer
        self.__typename: str = account_customer_json.get('__typename')
