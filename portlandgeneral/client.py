import requests
import json
from typing import List

from .constants import Api

from .queries import AccountDetails
from .queries import AccountInfo
from .queries import EnergyTracker

from .responses.account_details import AccountDetail
from .responses.account_info import AccountCustomer
from .responses.energy_tracker import EnergyTrackerData
from .responses.energy_tracker import PgeEnergyTrackerData
from .responses.auth import SignInResponse
from .responses.auth import TokenExchangeResponse


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
        self._verbose = verbose

        self._api_constants = Api(idp_host_override, api_host_override)

        # This will get set by the login process
        self._bearer_token = None

    def _request_idp(self, headers, body, params):
        return self._request('POST', self._api_constants.auth.firebase_idp.endpoint, headers, body, params)

    def _request_token(self, headers, params):
        return self._request('POST', self._api_constants.token_endpoint, headers, None, params)

    def _request_graphql(self, body):
        if self._bearer_token is None:
            raise Exception("Bearer token is not present - make sure the login function is used first.")

        headers = {
            **self._api_constants.headers.defaults,
            'authorization': f'Bearer {self._bearer_token}'
        }
        return self._request('POST', self._api_constants.graphql_endpoint, headers, body, None)

    def _request(self, method, url, headers, body=None, params=None):

        if self._verbose:
            print(method, url)

        s = requests.Session()
        response = s.request(
            method,
            url,
            data=json.dumps(body) if body else None,
            params=params,
            headers=headers,
            verify=False
        )

        if response.status_code == 200:
            return response.json()
        elif response.content:
            raise Exception(str(response.status_code) + ": " + response.reason + ": " + str(response.content))
        else:
            raise Exception(str(response.status_code) + ": " + response.reason)

    def _get_jwt(self, username: str, password: str) -> SignInResponse:
        if not username:
            raise ValueError("Cannot login, username is not set")
        if not password:
            raise ValueError("Cannot login, password not set")

        headers = {
            **self._api_constants.headers.defaults,
            'authority': 'identitytoolkit.googleapis.com',
            'sec-fetch-site': 'cross-site',
        }
        body = {
            'email': username,
            'password': password,
            'returnSecureToken': True,
        }
        params = {
            'key': self._api_constants.auth.firebase_idp.key,
        }
        response_json = self._request_idp(headers, body, params)

        return SignInResponse(response_json)

    def _exchange_jwt_for_bearer_token(self, sign_in_response: SignInResponse) -> TokenExchangeResponse:
        params = {
            'client_id': self._api_constants.auth.apigee.client_id,
            'response_type': 'token',
            'redirect_uri': ''  # Not sure why this is present with an empty value
        }
        headers = {
            **self._api_constants.headers.defaults,
            'content-length': '0',
            'idp_access_token': sign_in_response.id_token
        }
        response_json = self._request_token(headers, params)

        token_exchange_response = TokenExchangeResponse(response_json)
        # At this point, the token can be set to be added to the default headers as an Authorization
        self._bearer_token = token_exchange_response.access_token
        # TODO: handle token expiry and refreshes
        return token_exchange_response

    # Returns a token if properly authenticated
    def login(self, username: str, password: str) -> TokenExchangeResponse:
        sign_in_response = self._get_jwt(username, password)
        return self._exchange_jwt_for_bearer_token(sign_in_response)

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
