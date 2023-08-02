import pytest

from blocks.auth.api import AuthUser
from blocks.auth.model import AuthSuccessful
from blocks.registration.api import RegistrationUser
from blocks.registration.model import RegistrationData, RegistrationSuccessful
from blocks.store.api import Store
from blocks.store.model import StoreData, CreateStoreSuccessful
from blocks.store_item.api import StoreItem
from blocks.store_item.model import Item, ItemData, CreateItemSuccessful
from blocks.user_info.api import UserInfo
from blocks.user_info.model import UserData


@pytest.fixture
def new_user():
    data = RegistrationData.random().dict()
    request = RegistrationUser()
    response = request.post(data=data, response_model=RegistrationSuccessful)
    yield {"data": data, "uuid_user": response.data.uuid}


@pytest.fixture
def access_token(new_user):
    request = AuthUser()
    response = request.post(data=new_user["data"], response_model=AuthSuccessful)
    yield {"access_token": response.data.access_token, "uuid_user": new_user["uuid_user"]}


@pytest.fixture
def create_store(access_token):
    data = StoreData.random()
    request = Store()
    response = request.post(data=data,
                            headers={"Authorization": f"JWT {access_token['access_token']}"},
                            response_model=CreateStoreSuccessful)
    yield {"storename": data,
           "access_token": {"Authorization": f"JWT {access_token['access_token']}"},
           "store_id": response.data.uuid}


@pytest.fixture
def add_user_info(access_token):
    request = UserInfo()
    info = UserData.random().dict()
    request.post(tag=access_token["uuid_user"], data=info,
                 headers={"Authorization": f"JWT {access_token['access_token']}"},
                 response_model=UserData)
    yield {"access_token": access_token['access_token'], "uuid_user": access_token["uuid_user"],
           "info": info}


@pytest.fixture
def create_store_item(create_store):
    name_item = Item.random()
    data = ItemData.random(create_store["store_id"]).dict()
    request = StoreItem()
    response = request.post(data=data, tag=name_item,
                            headers=create_store['access_token'],
                            response_model=CreateItemSuccessful)
    yield {"access_token": create_store['access_token'], "store_id": create_store["store_id"],
           "itemID": response.data.itemID, "name_item": name_item, "info": data}
