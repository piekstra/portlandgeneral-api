class DefaultAccountInfo:

    def __init__(self, default_account_info_json: dict):

        # Seems to always be an int but comes across as a string
        self.account_number: str = default_account_info_json.get('accountNumber')
        self.encrypted_account_number: str = default_account_info_json.get('defaultAccountNumber')
        self.encrypted_person_id: str = default_account_info_json.get('encryptedPersonId')

        # Value: DefaultAccountInfo
        self.__typename: str = default_account_info_json.get('__typename')
