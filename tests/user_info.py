from blocks.user_info.api import UserInfo
from blocks.user_info.model import UserData, UserDataCreateSuccessful, UserDataUpdateSuccessful, \
    GetUserInfo, DeleteUserInfo, NoUserInfo
from common.constants import UserInfoMessage


class TestUserInfo:
    def test_add_user_info(self, access_token):
        request = UserInfo()
        response = request.post(tag=access_token["uuid_user"], data=UserData.random().dict(),
                                headers={"Authorization": f"JWT {access_token['access_token']}"},
                                response_model=UserDataCreateSuccessful)

        assert response.status_code == 200
        assert response.data.message == UserInfoMessage.SUCCESS_ADD

    def test_edit_user_info(self, add_user_info):
        request = UserInfo()
        response = request.put(tag=add_user_info["uuid_user"], data=UserData.random().dict(),
                               headers={"Authorization": f"JWT {add_user_info['access_token']}"},
                               response_model=UserDataUpdateSuccessful)

        assert response.status_code == 200
        assert response.data.message == UserInfoMessage.SUCCESS_EDIT

    def test_get_user_no_info(self, access_token):
        request = UserInfo()
        response = request.get(tag=access_token["uuid_user"],
                               headers={"Authorization": f"JWT {access_token['access_token']}"},
                               response_model=NoUserInfo)

        assert response.status_code == 404
        assert response.data.message == UserInfoMessage.NOT_FOUND

    def test_get_user_info(self, add_user_info):
        request = UserInfo()
        response = request.get(tag=add_user_info["uuid_user"],
                               headers={"Authorization": f"JWT {add_user_info['access_token']}"},
                               response_model=GetUserInfo)

        assert response.status_code == 200
        assert response.data.city == add_user_info["info"]["address"]["city"]
        assert response.data.street == add_user_info["info"]["address"]["street"]
        assert response.data.phone == add_user_info["info"]["phone"]
        assert response.data.email == add_user_info["info"]["email"]

    def test_delete_user_info(self, add_user_info):
        request = UserInfo()
        response = request.delete(tag=add_user_info["uuid_user"],
                                  headers={
                                      "Authorization": f"JWT {add_user_info['access_token']}"},
                                  response_model=DeleteUserInfo)

        assert response.status_code == 200
        assert response.data.message == UserInfoMessage.SUCCESS_DELETE
        response = request.get(tag=add_user_info["uuid_user"],
                               headers={"Authorization": f"JWT {add_user_info['access_token']}"},
                               response_model=NoUserInfo)
        assert response.status_code == 404
        assert response.data.message == UserInfoMessage.NOT_FOUND
