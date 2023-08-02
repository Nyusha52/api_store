from blocks.store.api import Store
from blocks.store.model import StoreData, CreateStoreSuccessful, StoreAlreadyExist, StoreInfo
from common.constants import StoreMessage


class TestStore:
    def test_create_store(self, access_token):
        data = StoreData.random()
        request = Store()
        response = request.post(data=data,
                                headers={"Authorization": f"JWT {access_token['access_token']}"},
                                response_model=CreateStoreSuccessful)

        assert response.status_code == 201
        assert response.data.name == data

    def test_store_already_exists(self, create_store):
        request = Store()
        response = request.post(data=create_store["storename"],
                                headers=create_store["access_token"],
                                response_model=StoreAlreadyExist)

        assert response.status_code == 400
        assert response.data.message == StoreMessage.genetate_already_exists_message(
            create_store["storename"])

    def test_get_store_info(self, create_store):
        request = Store()
        response = request.get(data=create_store["storename"],
                               headers=create_store["access_token"],
                               response_model=StoreInfo)

        assert response.status_code == 200
