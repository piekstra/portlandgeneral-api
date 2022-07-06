from ..responses.account_info import AccountCustomer


class AccountInfo:
    def __init__(self, remove_inactive_accounts: bool = False):
        self.remove_inactive_accounts = remove_inactive_accounts
        self.operation_name = 'getAccountInfo'
        self.base_query_payload = {
            'operationName': self.operation_name,
            'variables': {
                'params': {
                    'removeInactiveAccounts': self.remove_inactive_accounts
                }
            },
        }

    def build_response(self, response_json: dict) -> AccountCustomer:
        data = response_json.get('data')
        info = data.get(self.operation_name)
        return AccountCustomer(info)

    def full_info_query(self, is_limit_details_to_default_group: bool = True) -> dict: return {
        **self.base_query_payload,
        # Extend base variables
        'variables': {
            **self.base_query_payload['variables'],
            'isLimitDetailsToDefaultGroup': is_limit_details_to_default_group,
        },
        'query': """
query getAccountInfo($params: GetAccountInfoParams) {
  getAccountInfo(params: $params) {
    ...accountInfo
    __typename
  }
}

fragment accountInfo on AccountCustomer {
  uid
  personId
  encryptedPersonId
  language
  prefLanguage
  email
  personName
  timestamp
  lastConfirmedDate
  accountMeta {
    totalAccounts
    hasInactiveAccounts
    __typename
  }
  groups {
    groupName
    groupId
    groupCode
    numberOfAccounts
    isDefault
    type
    isDefaultAccountExists
    isLoggedOnUserAutoGroup
    defaultAccount {
      accountNumber
      encryptedAccountNumber
      encryptedPersonId
      __typename
    }
    __typename
  }
  contactDetails {
    contactType
    contactValue
    __typename
  }
  __typename
}
"""
    }

    def summary(self, is_limit_details_to_default_group: bool = True) -> dict: return {
        **self.base_query_payload,
        # Extend base variables
        'variables': {
            **self.base_query_payload['variables'],
            'isLimitDetailsToDefaultGroup': is_limit_details_to_default_group,
        },
        'query': """
query getAccountInfo($params: GetAccountInfoParams) {
  getAccountInfo(params: $params) {
    ...accountInfo
    __typename
  }
}

fragment accountInfo on AccountCustomer {
  personId
  encryptedPersonId
  prefLanguage
  email
  personName
  accountMeta {
    totalAccounts
    __typename
  }
  groups {
    groupName
    groupId
    groupCode
    numberOfAccounts
    isDefault
    type
    isDefaultAccountExists
    isLoggedOnUserAutoGroup
    defaultAccount {
      accountNumber
      encryptedAccountNumber
      encryptedPersonId
      __typename
    }
    __typename
  }
  contactDetails {
    contactType
    contactValue
    __typename
  }
  __typename
}
"""
    }

    # TODO: see if this can be merged into the other request
    def summary_other(self) -> dict: return {
        **self.base_query_payload,
        'query': """
query getAccountInfo($params: GetAccountInfoParams) {
  getAccountInfo(params: $params) {
    ...accountInfo
    __typename
  }
}

fragment accountInfo on AccountCustomer {
  uid
  language
  prefLanguage
  email
  personName
  personId
  timestamp
  encryptedPersonId
  accountMeta {
    totalAccounts
    hasInactiveAccounts
    __typename
  }
  lastConfirmedDate
  groups {
    groupName
    groupId
    groupCode
    numberOfAccounts
    isDefault
    type
    isDefaultAccountExists
    isLoggedOnUserAutoGroup
    defaultAccount {
      accountNumber
      encryptedAccountNumber
      encryptedPersonId
      __typename
    }
    __typename
  }
  contactDetails {
    contactType
    contactValue
    __typename
  }
  __typename
}
"""
    }
