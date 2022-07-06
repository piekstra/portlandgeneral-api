class AccountMeta:

    def __init__(self, account_meta_json: dict):
        self.total_accounts: int = account_meta_json.get('totalAccounts')

        # Presumably a bool, but can come across as null
        self.has_inactive_accounts = account_meta_json.get('hasInactiveAccounts')

        # Value: AccountMeta
        self.__typename: str = account_meta_json.get('__typename')
