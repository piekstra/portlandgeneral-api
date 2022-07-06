class SignInResponse:

    def __init__(self, response_json: dict):

        # Value: identitytoolkit#VerifyPasswordResponse
        self.kind: str = response_json.get('kind')
        self.local_id: str = response_json.get('localId')
        self.email: str = response_json.get('email')
        self.display_name: str = response_json.get('displayName')
        self.id_token: str = response_json.get('idToken')
        self.registered: bool = response_json.get('registered')
        self.refresh_token: str = response_json.get('refreshToken')

        # Appears to be an int but comes across as a string
        self.expires_in: str = response_json.get('expiresIn')
