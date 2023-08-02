import requests
from requests import Response
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def get_rey_session(max_retries=3,
                    backoff_factor=1,
                    status_forcelist=(500, 503),
                    allowed_methods=frozenset(["GET", "PUT", "DELETE", "POST"]),
                    raise_on_status=False
                    ):
    "Return a request session that retries request."
    session = requests.session()
    retries = Retry(total=max_retries, backoff_factor=backoff_factor,
                    status_forcelist=status_forcelist, allowed_methods=allowed_methods,
                    raise_on_status=raise_on_status)
    session.mount("http://", HTTPAdapter(max_retries=retries))
    return session


class ApiRequest:
    def __init__(self, host: str, api_url: str, tag=None, query_params=None, headers=None,
                 data=None):
        self.host = host
        self.api_url = api_url
        self.tag = tag
        self.params = query_params
        self.headers = headers
        self.data = data
        self.url = self._compose_url()

    def _compose_url(self):
        url = f'http://{self.host}/{self.api_url}'
        if self.tag:
            url += f'/{self.tag}'

        return url

    def __repr__(self):
        return f'{self.url=}, {self.params=}, {self.headers=}, {self.data=}'


class ApiClient:

    @staticmethod
    def get(api_request: ApiRequest) -> Response:
        session = get_rey_session()
        response = session.get(url=api_request.url,
                               params=api_request.params,
                               headers=api_request.headers,
                               json=api_request.data)
        return response

    @staticmethod
    def post(api_request: ApiRequest) -> Response:
        response = requests.post(url=api_request.url,
                                 params=api_request.params,
                                 headers=api_request.headers,
                                 json=api_request.data)
        return response

    @staticmethod
    def put(api_request: ApiRequest) -> Response:
        response = requests.put(url=api_request.url,
                                params=api_request.params,
                                headers=api_request.headers,
                                json=api_request.data)
        return response

    @staticmethod
    def delete(api_request: ApiRequest) -> Response:
        response = requests.delete(url=api_request.url,
                                   params=api_request.params,
                                   headers=api_request.headers,
                                   json=api_request.data)
        return response


class JsonParser:
    @staticmethod
    def get_json_data(response):
        if response.headers.get('content-type') == 'application/json':
            # body = response.json()
            # json_body = json.dumps(
            #     json.loads(body.decode("utf-8")), indent=4, ensure_ascii=False
            # )
            return response.json()
        else:
            return "no_json"
