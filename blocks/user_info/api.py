from typing import Optional

from pydantic import BaseModel

from blocks.store.model import StoreData
from utilites.logger import log
from common.constants import Hosts, ApiUrl
from utilites.client import ApiClient, ApiRequest
from utilites.validator import Validator


class UserInfo(Validator):
    """User info block."""

    def __init__(self):
        self.api = ApiClient()

    @log("POST /user_info")
    def post(self, data, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.USER_INFO,
                                 data=data, tag=tag, headers=headers)
        response = self.api.post(api_request)

        return self.transform(response, response_model=response_model)

    @log("PUT /user_info")
    def put(self, data, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.USER_INFO,
                                 data=data, tag=tag, headers=headers)
        response = self.api.put(api_request)

        return self.transform(response, response_model=response_model)

    @log("GET /user_info")
    def get(self, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.USER_INFO,
                                 tag=tag, headers=headers)
        response = self.api.get(api_request)

        return self.transform(response, response_model=response_model)

    @log("DELETE /user_info")
    def delete(self, tag, headers, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.USER_INFO,
                                 tag=tag, headers=headers)
        response = self.api.delete(api_request)

        return self.transform(response, response_model=response_model)
