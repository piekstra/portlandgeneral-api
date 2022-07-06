import json
from decimal import Decimal

from portlandgeneral import PortlandGeneralApi


def json_lambda(x): return str(x) if type(x) is Decimal else x.__dict__


client = PortlandGeneralApi(verbose=True)
client.login(
    username='user@email.com',
    password='redacted'
)

info = client.get_account_info()
print(json.dumps(info.__dict__, indent=2, default=json_lambda))

account_numbers = [group.default_account.account_number for group in info.groups]
first_account_number = account_numbers[0]

details = client.get_account_details(first_account_number, info.encrypted_person_id)
first_account_detail = details[0]
print(json.dumps(first_account_detail.__dict__, indent=2, default=json_lambda))

tracker = client.get_energy_tracker_info(
    first_account_detail.encrypted_account_number,
    first_account_detail.encrypted_person_id
)
print(json.dumps(tracker.__dict__, indent=2, default=json_lambda))

pge_tracker = client.get_pge_energy_tracker_info(
    first_account_detail.encrypted_account_number,
    first_account_detail.encrypted_person_id
)
print(json.dumps(pge_tracker.__dict__, indent=2, default=json_lambda))
