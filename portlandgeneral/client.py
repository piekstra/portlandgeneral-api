import requests
import json
from typing import List

from .constants import PgeApi

from .queries import AccountDetails
from .queries import AccountInfo
from .queries import EnergyTracker

from .responses.account_details import AccountDetail
from .responses.account_info import AccountCustomer
from .responses.energy_tracker import EnergyTrackerData
from .responses.energy_tracker import PgeEnergyTrackerData
from .responses.auth import TokenExchangeResponse

from .client_auth import ClientAuth


class PortlandGeneralApi:
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

        self._api_constants: PgeApi = PgeApi(idp_host_override, api_host_override)
        self._client_auth: ClientAuth = ClientAuth(
            verbose,
            idp_host_override,
            api_host_override,
            self._api_constants.auth.apigee.auth.client_id
        )

    def _request_graphql(self, body=None):
        method = 'POST'
        url = self._api_constants.graphql_endpoint

        if self._verbose:
            print(method, url)

        s = requests.Session()
        response = s.request(
            method,
            url,
            data=json.dumps(body) if body else None,
            auth=self._client_auth
        )

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    # Gets a new bearer token
    def refresh_token(self) -> TokenExchangeResponse:
        return self._client_auth.refresh_token()

    # Returns a token if properly authenticated
    def login(self, username: str, password: str) -> TokenExchangeResponse:
        return self._client_auth.login(username, password)

    def get_account_details(self, account_number: str, encrypted_person_id: str) -> List[AccountDetail]:
        details = AccountDetails(account_number, encrypted_person_id)
        query = details.full_details_query()
        response_json = self._request_graphql(body=query)
        return details.build_response(response_json)

    def get_account_info(self) -> AccountCustomer:
        info = AccountInfo()
        query = info.full_info_query()
        response_json = self._request_graphql(body=query)
        return info.build_response(response_json)

    def get_energy_tracker_info(self, encrypted_account_number: str, encrypted_person_id: str) -> EnergyTrackerData:
        tracker = EnergyTracker(encrypted_account_number, encrypted_person_id)
        query = tracker.data_details_query()
        response_json = self._request_graphql(body=query)
        return tracker.build_response(response_json)

    def get_pge_energy_tracker_info(self, encrypted_account_number: str, encrypted_person_id: str) -> PgeEnergyTrackerData:
        tracker = EnergyTracker(encrypted_account_number, encrypted_person_id)
        query = tracker.pge_billable_details_query()
        response_json = self._request_graphql(body=query)
        return tracker.build_response_pge(response_json)

    def download_bill_pdf(self):
        # TODO: there's an endpoint: https://csapi.portlandgeneral.com/api/ViewBill/Download
        # POST: {"encryptedBillId":"REDACTED="}
        ""
