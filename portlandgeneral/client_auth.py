import requests
import json

from requests.auth import AuthBase

from .constants import PgeApi

from .responses.auth import SignInResponse
from .responses.auth import TokenExchangeResponse


class ClientAuth(AuthBase):
    def __init__(
        self,
        verbose: bool = False,
        idp_host_override: str = None,
        api_host_override: str = None,
        client_id: str = None
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
        self.client_id = client_id

        # These will get set by the login process
        self.bearer_token: str = None
        self.refresh_token: str = None

    # Auth handler for requests using this ClientAuth
    def __call__(self, request):
        if self.bearer_token is None:
            raise Exception("Bearer token is not present - make sure the login function is used first.")
        request.headers.update({
            **self._api_constants.headers.defaults,
            'authorization': f'Bearer {self.bearer_token}',
        })
        # TODO: handle token expiry and refreshes
        return request

    def _request(self, method: str, url: str, headers: dict, body=None, params=None):
        request_headers = {
            **self._api_constants.headers.defaults,
            **headers
        }

        if self._verbose:
            print(method, url)

        s = requests.Session()
        response = s.request(
            method,
            url,
            data=json.dumps(body) if body else None,
            params=params,
            headers=request_headers
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
        response_json = self._request('POST', self._api_constants.auth.firebase_idp.endpoint, headers, body, params)

        sign_in_response = SignInResponse(response_json)
        self.refresh_token = sign_in_response.refresh_token
        return sign_in_response

    def _exchange_jwt_for_bearer_token(self, headers) -> TokenExchangeResponse:
        params = {
            'client_id': self.client_id,
            'response_type': 'token',
            'redirect_uri': ''  # Not sure why this is present with an empty value
        }
        headers = {
            'content-length': '0',
            **headers
        }
        response_json = self._request('POST', self._api_constants.token_endpoint, headers, None, params)

        token_exchange_response = TokenExchangeResponse(response_json)
        # At this point, the token can be set to be added to the default headers as an Authorization
        self.bearer_token = token_exchange_response.access_token
        return token_exchange_response

    # Gets a new bearer token
    def refresh_token(self) -> TokenExchangeResponse:
        headers = {
            'idp_refresh_token': self.refresh_token
        }
        return self._exchange_jwt_for_bearer_token(headers)

    # Returns a token if properly authenticated
    def login(self, username: str, password: str) -> TokenExchangeResponse:
        sign_in_response = self._get_jwt(username, password)

        headers = {
            'idp_access_token': sign_in_response.id_token
        }
        return self._exchange_jwt_for_bearer_token(headers)
