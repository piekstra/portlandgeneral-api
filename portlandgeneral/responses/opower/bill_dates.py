from typing import List


class BillDates:

    def __init__(self, resp_json: dict):

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.customer_uuid: str = resp_json.get('customerUuid')

        # Example: pgn
        self.utility_code: str = resp_json.get('utilityCode')

        self.statement_dates: List[StatementDate] = [StatementDate(stmt_json) for stmt_json in resp_json.get('statementDates')]


class StatementDate:

    def __init__(self, stmt_json: dict):

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.bill_uuid: str = stmt_json.get('billUuid')

        # Format like: YYYY-MM-DD
        self.statement_date: str = stmt_json.get('statementDate')

        # UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.previous_bill_uuid: str = stmt_json.get('previousBillUui')

        # List of UUIDs. UUID format like: AAAABBBB-CCCC-DDDD-1111-FFFF44442222
        self.utility_account_uuids: List[str] = stmt_json.get('utilityAccountUuids')
