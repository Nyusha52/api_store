from typing import Optional

from pydantic import BaseModel

from blocks.store.model import StoreData
from utilites.logger import log
from common.constants import Hosts, ApiUrl
from utilites.client import ApiClient, ApiRequest
from utilites.validator import Validator


class Store(Validator):
    """Store block."""

    def __init__(self):
        self.api = ApiClient()

    @log("POST /store")
    def post(self, data, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.STORE,
                                 data=data, tag=data, headers=headers)
        response = self.api.post(api_request)

        return self.transform(response, response_model=response_model)

    @log("GET /store")
    def get(self, data, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.STORE,
                                 data=data, tag=data, headers=headers)
        response = self.api.get(api_request)

        return self.transform(response, response_model=response_model)
