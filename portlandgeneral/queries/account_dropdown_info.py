from ..responses.account_details.account_detail_list import AccountDetailList


class AccountDropdownInfo:

    def __init__(self):
        self.operation_name = 'getAccountDropdownInfo'
        self.base_query_payload = {
            'operationName': self.operation_name,
        }

    def build_response(self, response_json: dict) -> AccountDetailList:
        data = response_json.get('data')
        # Note that the response is specifically not the same as the operation_name
        detail_list = data.get('getAccountDetailList')
        return AccountDetailList(detail_list)

    def query(self) -> dict: return {
        **self.base_query_payload,
        'variables': {
            'params': {
                'groupId': '7880ada0-c604-48c0-ad80-ced86739425d',
                'filter': {
                    'filterBy': '',
                    'operator': 'STARTSWITH'
                },
                'paging': {
                    'limit': 5,
                    'offset': 0
                },
                'sort': {
                    'sort': 'DEFAULT',
                    'direction': 'ASC'
                },
                'accountStatus': 'ALL'
            }
        },
        'query': """
query getAccountDropdownInfo($params: AccountDetailListParams!) {
  getAccountDetailList(params: $params) {
    totalCount
    accounts {
      ...DropdownInfo
      __typename
    }
    __typename
  }
}

fragment DropdownInfo on AccountDetail {
  isDefault
  accountNumber
  encryptedAccountNumber
  encryptedPersonId
  description
  mainCustomerName
  isActive
  serviceAddresses {
    addressLine1
    addressLine2
    city
    state
    postal
    __typename
  }
  serviceConnectivity {
    isEligibleForReconnect
    isDisconnected
    isReconnectInProgress
    __typename
  }
  __typename
}
"""
    }
