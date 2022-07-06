from typing import List

from .account_detail import AccountDetail


class AccountDetailList:

    def __init__(self, account_detail_list_json: dict):
        self.total_count: int = account_detail_list_json.get('totalCount')
        self.accounts: List[AccountDetail] = [AccountDetail(j) for j in account_detail_list_json.get('accounts')]

        # Value: AccountDetailList
        self.__typename: str = account_detail_list_json.get('__typename')
