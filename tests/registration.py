from blocks.registration.api import RegistrationUser
from blocks.registration.model import RegistrationData, RegistrationSuccessful
from common.constants import Registration

class TestRegisterUser:

    def test_register_user(self):
        data = RegistrationData.random().dict()
        request = RegistrationUser()
        response = request.post(data=data, response_model=RegistrationSuccessful)

        assert response.status_code == 201
        assert response.data.message == Registration.SUCCESS

    def test_register_user_already_exists(self, new_user):
        request = RegistrationUser()
        response = request.post(data=new_user["data"], response_model=RegistrationSuccessful)

        assert response.status_code == 400
        assert response.data.message == Registration.ALREADY_EXISTS