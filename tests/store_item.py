import pytest

from blocks.store_item.api import StoreItem
from blocks.store_item.model import ItemData, CreateItemSuccessful, Item, ItemAlreadyExists, \
    ItemInfo, UpdateInfo
from common.constants import ItemMessage


class TestStoreItem:
    def test_create_store_item(self, create_store):
        name_item = Item.random()
        data = ItemData.random(create_store["store_id"]).dict()
        request = StoreItem()
        response = request.post(data=data, tag=name_item,
                                headers=create_store['access_token'],
                                response_model=CreateItemSuccessful)

        assert response.status_code == 201
        assert response.data.name == name_item
        assert response.data.price == data["price"]
        assert response.data.description == data["description"]
        assert response.data.image == data["image"]

    def test_store_item_already_exists(self, create_store_item):
        request = StoreItem()
        response = request.post(data=create_store_item["info"], tag=create_store_item["name_item"],
                                headers=create_store_item['access_token'],
                                response_model=ItemAlreadyExists)

        assert response.status_code == 400
        assert response.data.message == ItemMessage.genetate_already_exists_message(
            create_store_item["name_item"])

    def test_get_store_info(self, create_store_item):
        request = StoreItem()
        response = request.get(tag=create_store_item["name_item"],
                               headers=create_store_item["access_token"],
                               response_model=ItemInfo)

        assert response.status_code == 200
        assert response.data.name == create_store_item[
            "name_item"], f'{response.data.name} != {create_store_item["name_item"]}'
        assert response.data.price == create_store_item["info"]["price"]
        assert response.data.description == create_store_item["info"]["description"]
        assert response.data.image == create_store_item["info"]["image"]
        assert response.data.itemID == create_store_item["itemID"]

    @pytest.mark.xfail(reason="bug: don't change description and image")
    def test_update_store_item(self, create_store_item):
        update_data = ItemData.random(create_store_item["store_id"]).dict()
        request = StoreItem()
        response = request.put(data=update_data, tag=create_store_item["name_item"],
                               headers=create_store_item['access_token'],
                               response_model=UpdateInfo)

        assert response.status_code == 200
        assert response.data.name == create_store_item["name_item"]
        assert response.data.price == update_data["price"]
        assert response.data.description == update_data["description"]
        assert response.data.image == update_data["image"]
