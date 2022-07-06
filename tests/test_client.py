import os
import pytest

from portlandgeneral import PortlandGeneralApi


@pytest.fixture(scope='module')
def client() -> PortlandGeneralApi:
    return PortlandGeneralApi(
        idp_host_override=os.environ.get('IDP_HOST_OVERRIDE'),
        api_host_override=os.environ.get('API_HOST_OVERRIDE')
    )


@pytest.mark.usefixtures('client')
class TestGetDevices(object):

    def test_login(self, client: PortlandGeneralApi):
        login_result = client.login(
            username=os.environ.get('PORTLANDGENERAL_USERNAME'),
            password=os.environ.get('PORTLANDGENERAL_PASSWORD')
        )
        assert login_result is not None
        assert login_result.access_token == 'greatTOKEN123'
        assert login_result.client_id == 'rHuS10KrfsLwFAr2sZ7MHh7oHELGx6YK'
        assert login_result.developer_email == 'shashank.shetti@pgn.com'
        assert login_result.expires_in == '1200'
        assert login_result.expires_at == '1656717216'
        assert login_result.claim_email == 'example@email.com'
        assert login_result.organization_name == 'pge-prod'
