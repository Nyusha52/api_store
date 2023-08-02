from typing import Optional

from pydantic import BaseModel

from utilites.logger import log
from common.constants import Hosts, ApiUrl
from utilites.client import ApiClient, ApiRequest
from utilites.validator import Validator


class StoreItem(Validator):
    """User info block."""

    def __init__(self):
        self.api = ApiClient()

    @log("POST /item")
    def post(self, data, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.STORE_ITEM,
                                 data=data, tag=tag, headers=headers)
        response = self.api.post(api_request)

        return self.transform(response, response_model=response_model)

    @log("PUT /item")
    def put(self, data, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.STORE_ITEM,
                                 data=data, tag=tag, headers=headers)
        response = self.api.put(api_request)

        return self.transform(response, response_model=response_model)

    @log("GET /item")
    def get(self, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.STORE_ITEM,
                                 tag=tag, headers=headers)
        response = self.api.get(api_request)

        return self.transform(response, response_model=response_model)
