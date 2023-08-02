from typing import Optional

from pydantic import BaseModel

from utilites.logger import log
from common.constants import Hosts, ApiUrl
from utilites.client import ApiClient, ApiRequest
from utilites.validator import Validator


class AuthUser(Validator):
    """Authorization block."""

    def __init__(self):
        self.api = ApiClient()

    @log("POST /auth")  # type: ignore
    def post(self, data, response_model: Optional[BaseModel] = None):
        api_request = ApiRequest(host=Hosts.LOCAL, api_url=ApiUrl.AUTH,
                                 data=data)
        response = self.api.post(api_request)

        return self.transform(response, response_model=response_model)
