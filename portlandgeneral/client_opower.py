import requests
from typing import List
from datetime import date
from dateutil.relativedelta import relativedelta

from .constants import ApigeeWidgetAuth as ApiAuthSettings
from .constants import OPowerApi as ApiSettings

from .client_auth import ClientAuth

from .responses.auth import TokenExchangeResponse

from .responses.opower import BillDates
from .responses.opower import BillComparison
from .responses.opower import CurrentCustomers
from .responses.opower import UtilityAccountMetadata
from .responses.opower import UtilityBillingWindows
from .responses.opower import UtilityUsage
from .responses.opower import UtilityCost
from .responses.opower import Weather
from .responses.opower import NeighborComparison
from .responses.opower import SolarAccounts


class OPowerApi:
    def __init__(
        self,
        verbose: bool = False,
        idp_host_override: str = None,
        api_host_override: str = None
    ):
        """
        Initializes the API client.

        Parameters:
        verbose (bool): Whether to print messages to the console verbosely.
        idp_host_override (str): An override for the IDP Host defined in API Constants - only override for testing.
        api_host_override (str): An override for the API Host defined in API Constants - only override for testing.
        """
        self._verbose: bool = verbose

        widget_auth: ApiAuthSettings = ApiAuthSettings()
        self._api = ApiSettings()
        self._client_auth: ClientAuth = ClientAuth(
            verbose,
            idp_host_override,
            api_host_override,
            widget_auth.client_id
        )

    def _api_request(self, path: str, params: dict = None):
        return self._request('GET', self._api.api_endpoint + path, params)

    def _request(self, method: str, url: str, params: dict = None):

        if self._verbose:
            print(method, url)

        s = requests.Session()
        response = s.request(
            method,
            url,
            params=params,
            auth=self._client_auth
        )

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    # Gets a new bearer token
    def refresh_token(self, client_id: str) -> TokenExchangeResponse:
        return self._client_auth.refresh_token()

    # Returns a token if properly authenticated
    def login(self, username: str, password: str) -> TokenExchangeResponse:
        return self._client_auth.login(username, password)

    def current_customers(self) -> CurrentCustomers:
        response_json = self._api_request(
            '/multi-account-v1/cws/pgn/customers/current'
        )
        return CurrentCustomers(response_json)

    # as_of should be in iso format YYYY-MM-DD
    # Uses the current date if not specified
    def bill_dates(self, opower_uuid: str, as_of: str = None) -> BillDates:
        params = {
            'asOf': as_of if as_of is not None else date.today().isoformat()
        }
        response_json = self._api_request(
            f'/billComparison-v2/cws/v2/pgn/bill-comparison/customer/{opower_uuid}/bill-dates',
            params
        )
        return BillDates(response_json)

    # as_of should be in iso format YYYY-MM-DD
    # Uses the current date if not specified
    def previous_bill_comparison(self, opower_uuid: str, as_of: str = None) -> BillComparison:
        params = {
            'bill': 'PREVIOUS',
            'asOf': as_of if as_of is not None else date.today().isoformat()
        }
        response_json = self._api_request(
            f'/billComparison-v2/cws/v2/pgn/bill-comparison/customer/{opower_uuid}/comparison-by-type',
            params
        )
        return BillComparison(response_json)

    def utility_account_metadata(self, opower_uuid: str) -> UtilityAccountMetadata:
        params = {
            'preferredUtilityAccountIdType': 'UTILITY_ACCOUNT_ID_1',
            'includeCommercialAndIndustrial': True,
            'customerUuid': opower_uuid
        }
        response_json = self._api_request('/DataBrowser-v1/cws/metadata', params)
        return UtilityAccountMetadata(response_json)

    def utility_billing_windows(self, opower_uuid: str) -> UtilityBillingWindows:
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/utilities/pgn/customers/{opower_uuid}/usage_export',
        )
        return UtilityBillingWindows(response_json)

    # opower_account_utility_account_uuid
    # start_date should be in iso format YYYY-MM-DD
    # end_date should be in iso format YYYY-MM-DD
    # start and end dates will default to today if not specified
    def utility_usage_hourly(self, utility_account_uuid: str, start_date: str = None, end_date: str = None) -> UtilityUsage:
        today = date.today()
        yesterday = today - relativedelta(days=1)

        params = {
            'startDate': start_date if start_date is not None else yesterday.isoformat(),
            'endDate': end_date if end_date is not None else today.isoformat(),
            'aggregateType': 'hour',
            'includeEnhancedBilling': False,
            'includeMultiRegisterData': False
        }
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/utilities/pgn/utilityAccounts/{utility_account_uuid}/reads',
            params
        )
        return UtilityUsage(response_json)

    # opower_account_utility_account_uuid
    # start_date should be in iso format YYYY-MM-DD
    # end_date should be in iso format YYYY-MM-DD
    # start and end dates will default to one month ago and today
    def utility_usage_daily(self, utility_account_uuid: str, start_date: str = None, end_date: str = None) -> UtilityUsage:
        today = date.today()
        month_ago = today - relativedelta(months=1)

        params = {
            'startDate': start_date if start_date is not None else month_ago.isoformat(),
            'endDate': end_date if end_date is not None else today.isoformat(),
            'aggregateType': 'day',
            'includeEnhancedBilling': False,
            'includeMultiRegisterData': False
        }
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/utilities/pgn/utilityAccounts/{utility_account_uuid}/reads',
            params
        )
        return UtilityUsage(response_json)

    # opower_account_utility_account_uuid
    def utility_usage_billing_periods(self, utility_account_uuid: str, start_date: str = None, end_date: str = None) -> UtilityUsage:
        params = {
            'aggregateType': 'bill',
            'includeEnhancedBilling': False,
            'includeMultiRegisterData': False
        }
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/utilities/pgn/utilityAccounts/{utility_account_uuid}/reads',
            params
        )
        return UtilityUsage(response_json)

    # opower_account_utility_account_uuid
    # start_date should be in iso format YYYY-MM-DD
    # end_date should be in iso format YYYY-MM-DD
    # start and end dates will default to today if not specified
    def utility_cost_hourly(self, utility_account_uuid: str, start_date: str = None, end_date: str = None) -> UtilityCost:
        today = date.today()
        yesterday = today - relativedelta(days=1)

        params = {
            'startDate': start_date if start_date is not None else yesterday.isoformat(),
            'endDate': end_date if end_date is not None else today.isoformat(),
            'aggregateType': 'hour',
            'includePtr': True
        }
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/cost/utilityAccount/{utility_account_uuid}',
            params
        )
        return UtilityCost(response_json)

    # opower_account_utility_account_uuid
    # start_date should be in iso format YYYY-MM-DD
    # end_date should be in iso format YYYY-MM-DD
    # start and end dates will default to one month ago and today
    def utility_cost_daily(self, utility_account_uuid: str, start_date: str = None, end_date: str = None) -> UtilityCost:
        today = date.today()
        month_ago = today - relativedelta(months=1)

        params = {
            'startDate': start_date if start_date is not None else month_ago.isoformat(),
            'endDate': end_date if end_date is not None else today.isoformat(),
            'aggregateType': 'day',
            'includePtr': True
        }
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/cost/utilityAccount/{utility_account_uuid}',
            params
        )
        return UtilityCost(response_json)

    # opower_account_utility_account_uuid
    def utility_cost_billing_periods(self, utility_account_uuid: str) -> UtilityCost:
        params = {
            'aggregateType': 'bill',
            'includePtr': True
        }
        response_json = self._api_request(
            f'/DataBrowser-v1/cws/cost/utilityAccount/{utility_account_uuid}',
            params
        )
        return UtilityCost(response_json)

    # start_date should be in iso format YYYY-MM-DD
    # end_date should be in iso format YYYY-MM-DD
    # start and end dates will default to today if not specified
    def weather_hourly(self, start_date: str = None, end_date: str = None, use_celsius: bool = False) -> Weather:
        today = date.today()
        yesterday = today - relativedelta(days=1)

        params = {
            'startDate': start_date if start_date is not None else yesterday.isoformat(),
            'endDate': end_date if end_date is not None else today.isoformat(),
            'useCelsius': use_celsius
        }
        response_json = self._api_request(
            '/DataBrowser-v1/cws/weather/hourly',
            params
        )
        return Weather(response_json)

    # start_date should be in iso format YYYY-MM-DD
    # end_date should be in iso format YYYY-MM-DD
    # start and end dates will default to one month ago and today
    def weather_daily(self, start_date: str = None, end_date: str = None, use_celsius: bool = False) -> Weather:
        today = date.today()
        month_ago = today - relativedelta(months=1)

        params = {
            'startDate': start_date if start_date is not None else month_ago.isoformat(),
            'endDate': end_date if end_date is not None else today.isoformat(),
            'useCelsius': use_celsius
        }
        response_json = self._api_request(
            '/DataBrowser-v1/cws/weather/daily',
            params
        )
        return Weather(response_json)

    # intervals should be in iso format YYYY-MM-DD/YYYY-MM-DD like 2022-01-01/2022-02-01
    # If no intervals is specified, a single interval will be included for one month ago to today
    # Note the dates are inclusive and the last date in each interval will be what is returned
    def weather_aggregates(self, intervals: List[str] = None, use_celsius: bool = False) -> Weather:
        today = date.today()
        month_ago = today - relativedelta(months=1)

        if intervals is None:
            intervals = [f'{month_ago.isoformat()}/{today.isoformat()}']

        params = {
            'interval': intervals,
            'useCelsius': use_celsius
        }

        response_json = self._api_request(
            '/DataBrowser-v1/cws/weather/aggregate',
            params
        )
        return Weather(response_json)

    def neighbor_utility_comparisons(self, opower_uuid: str) -> NeighborComparison:
        params = {
            'customerUuid': opower_uuid
        }
        response_json = self._api_request(
            '/DataBrowser-v1/cws/neighbors/electricity',
            params
        )
        return NeighborComparison(response_json)

    def solar_accounts(self, opower_uuid: str) -> SolarAccounts:
        response_json = self._api_request(
            f'/solar-v1/cws/v1/pgn/customers/{opower_uuid}/accounts'
        )
        return SolarAccounts(response_json)
