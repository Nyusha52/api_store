from pydantic import BaseModel


class AUthData(BaseModel):
    """Data to register new user."""

    username: str
    password: str


class AuthSuccessful(BaseModel):
    """Successful user registering response model."""

    access_token: str


class AuthNotSuccessful(BaseModel):
    """Successful user registering response model."""

    description: str
    error: str
    status_code: int
