"""Logging."""


import json
import logging
import pprint
from functools import wraps
from json import JSONDecodeError
from urllib.parse import unquote

from pydantic import ValidationError

logger = logging.getLogger("__name__")


def log(message: str):
    """Request Logging."""

    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            logger.info(message)
            response, err = function(*args, **kwargs)
            method = response.request.method
            url = unquote(response.request.url, encoding="utf-8", errors="replace")
            body = response.request.body
            status_code = response.status_code
            body_sep = " "
            log_request = f"Request method: {method}, url: {url}"
            if body is not None:
                try:
                    json_body = json.dumps(
                        json.loads(body.decode("utf-8")), indent=4, ensure_ascii=False
                    )
                    if len(body) > 20:
                        body_sep = "\n"
                    log_request += (
                        f", body:{body_sep}{json_body or pprint.pformat(body)}"
                    )
                except AttributeError:
                    log_request += f", body:\n{body}"
            logger.info(log_request)

            log_response = f"Response status code: {status_code}"
            try:
                body = response.json()
                if len(response.content) > 20:
                    body_sep = "\n"
                    bd = json.dumps(body, indent=4, ensure_ascii=False)
                    log_response += f", body:{body_sep}{bd}"
                else:
                    log_response += f", body:\n{json.dumps(body)}"
                logger.info(log_response)
            except JSONDecodeError:
                if len(response.text) > 120:
                    log_response += f", body:\n{response.text[:120]}..."
                else:
                    log_response += f", body:\n{response.text}"
                logger.info(log_response)
            if isinstance(err, ValidationError):
                logger.error(f"Response json did not pass validation!\n{err.json()}\n")
                raise err
            elif isinstance(err, JSONDecodeError):
                logger.error("Response body can not be converted to a dictionary!\n")
                raise err
            return response

        return inner

    return wrapper
