from blocks.auth.api import AuthUser
from blocks.auth.model import AuthSuccessful, AuthNotSuccessful
from common.constants import Auth


class TestAuth:
    def test_auth_user(self, new_user):
        request = AuthUser()
        response = request.post(data=new_user["data"], response_model=AuthSuccessful)

        assert response.status_code == 200


class TestAuthNegative:
    def test_not_auth_user(self):
        request = AuthUser()
        response = request.post(data=Auth.NO_USER, response_model=AuthNotSuccessful)

        assert response.status_code == 401
        assert response.data.description == Auth.ERROR_MESSAGE
