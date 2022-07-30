import json
from decimal import Decimal

from portlandgeneral import OPowerApi


def json_lambda(x): return str(x) if type(x) is Decimal else x.__dict__


client = OPowerApi(verbose=True)
client.login(
    username='user@email.com',
    password='redacted'
)

current_customers = client.current_customers()
print('current_customers')
print(json.dumps(current_customers, indent=2, default=json_lambda))

opower_uuid = current_customers.uuid
utility_account_uuid = current_customers.utility_accounts[0].uuid

bill_dates = client.bill_dates(opower_uuid)
print('bill_dates')
print(json.dumps(bill_dates, indent=2, default=json_lambda))

previous_bill_comparison = client.previous_bill_comparison(opower_uuid)
print('previous_bill_comparison')
print(json.dumps(previous_bill_comparison, indent=2, default=json_lambda))

utility_account_metadata = client.utility_account_metadata(opower_uuid)
print('utility_account_metadata')
print(json.dumps(utility_account_metadata, indent=2, default=json_lambda))

utility_billing_windows = client.utility_billing_windows(opower_uuid)
print('utility_billing_windows')
print(json.dumps(utility_billing_windows, indent=2, default=json_lambda))

utility_usage_hourly = client.utility_usage_hourly(utility_account_uuid)
print('utility_usage_hourly')
print(json.dumps(utility_usage_hourly, indent=2, default=json_lambda))

utility_usage_daily = client.utility_usage_daily(utility_account_uuid)
print('utility_usage_daily')
print(json.dumps(utility_usage_daily, indent=2, default=json_lambda))

utility_usage_billing_periods = client.utility_usage_billing_periods(utility_account_uuid)
print('utility_usage_billing_periods')
print(json.dumps(utility_usage_billing_periods, indent=2, default=json_lambda))

utility_cost_hourly = client.utility_cost_hourly(utility_account_uuid)
print('utility_cost_hourly')
print(json.dumps(utility_cost_hourly, indent=2, default=json_lambda))

utility_cost_daily = client.utility_cost_daily(utility_account_uuid)
print('utility_cost_daily')
print(json.dumps(utility_cost_daily, indent=2, default=json_lambda))

utility_cost_billing_periods = client.utility_cost_billing_periods(utility_account_uuid)
print('utility_cost_billing_periods')
print(json.dumps(utility_cost_billing_periods, indent=2, default=json_lambda))

weather_hourly = client.weather_hourly()
print('weather_hourly')
print(json.dumps(weather_hourly, indent=2, default=json_lambda))

weather_daily = client.weather_daily()
print('weather_daily')
print(json.dumps(weather_daily, indent=2, default=json_lambda))

weather_aggregates = client.weather_aggregates()
print('weather_aggregates')
print(json.dumps(weather_aggregates, indent=2, default=json_lambda))

neighbor_utility_comparisons = client.neighbor_utility_comparisons(utility_account_uuid)
print('neighbor_utility_comparisons')
print(json.dumps(neighbor_utility_comparisons, indent=2, default=json_lambda))

solar_accounts = client.solar_accounts(opower_uuid)
print('solar_accounts')
print(json.dumps(solar_accounts, indent=2, default=json_lambda))
