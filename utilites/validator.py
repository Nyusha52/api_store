from json import JSONDecodeError
from typing import Optional, Tuple

from pydantic import BaseModel, ValidationError
from requests import Response


class Validator:
    """Response json validator."""

    @staticmethod
    def transform(
            response: Response, response_model: Optional[BaseModel] = None
    ) -> Tuple[Response, Optional[Exception]]:
        """Transform response json to response.data field."""
        if response_model:
            try:
                response.data = response_model.parse_obj(  # type: ignore
                    response.json()
                )
            except (ValidationError, JSONDecodeError) as err:
                return response, err
        return response, None
