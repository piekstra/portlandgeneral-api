from .default_account_info import DefaultAccountInfo


class Group:

    def __init__(self, group_json: dict):

        # Example: My Residential Accounts, All Accounts
        self.group_name: str = group_json.get('groupName')

        # Seems to be some sort of UUID like 'aaaabbbb-cccc-dddd-1111-ffff44442222 when code is "My Residential Accounts"
        # For group "All Accounts", ID is also "All Accounts"
        self.group_id: str = group_json.get('groupId')

        # Example: My Residential Accounts, All Accounts
        self.group_code: str = group_json.get('groupCode')
        self.number_of_accounts: int = group_json.get('numberOfAccounts')
        self.is_default: bool = group_json.get('isDefault')

        # Example: Automatic, Virtual
        self.type: str = group_json.get('type')
        self.is_default_account_exists: bool = group_json.get('isDefaultAccountExists')
        self.is_logged_on_user_auto_group: bool = group_json.get('isLoggedOnUserAutoGroup')
        self.default_account: DefaultAccountInfo = DefaultAccountInfo(group_json.get('defaultAccount'))

        # Value: Group
        self.__typename: str = group_json.get('__typename')
