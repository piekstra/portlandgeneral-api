class Api:
    def __init__(self, idp_host_override: str = None, api_host_override: str = None):
        self.auth = ApiAuth(idp_host_override)
        self.headers = ApiHeaders()
        self.host = 'https://api.portlandgeneral.com' if api_host_override is None else api_host_override
        self.token_endpoint = self.host + '/pg-token-implicit/token'
        self.graphql_endpoint = self.host + '/pge-graphql'


class ApiAuth:
    def __init__(self, idp_host_override: str = None):
        self.firebase_idp = AuthFirebaseIdp(idp_host_override)
        self.apigee = AuthApigee()


class AuthFirebaseIdp:
    def __init__(self, idp_host_override: str = None):
        self.key = 'AIzaSyDGQGl4SfFoD_KJTo87PboxfNmq89pifqU'
        endpoint_base = 'https://identitytoolkit.googleapis.com' if idp_host_override is None else idp_host_override
        self.endpoint = f'{endpoint_base}/v1/accounts:signInWithPassword'


class AuthApigee:
    def __init__(self):
        self.client_id = 'rHuS10KrfsLwFAr2sZ7MHh7oHELGx6YK'


class ApiHeaders:
    def __init__(self):
        self.defaults = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'no-cache',
            'connection': 'keep-alive',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://portlandgeneral.com',
            'pragma': 'no-cache',
            'referer': 'https://portlandgeneral.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',  # This should be overridden for certain requests
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        }
