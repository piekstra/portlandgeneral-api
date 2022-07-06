class TokenExchangeResponse:

    def __init__(self, response_json: dict):
        self.access_token: str = response_json.get('access_token')

        # This is just the Apigee Client ID
        # Value: rHuS10KrfsLwFAr2sZ7MHh7oHELGx6YK
        self.client_id: str = response_json.get('client_id')

        # Value: shashank.shetti@pgn.com
        self.developer_email: str = response_json.get('developer.email')

        # Appears to be an int but comes across as a string
        self.expires_in: str = response_json.get('expires_in')

        # Appears to be an int but comes across as a string
        self.expires_at: str = response_json.get('expires_at')
        self.claim_email: str = response_json.get('claim_email')

        # Value: pge-prod
        self.organization_name: str = response_json.get('organization_name')
