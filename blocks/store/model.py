from faker import Faker
from pydantic import BaseModel

fake = Faker()


class StoreData(BaseModel):
    """Data to register new user."""

    @staticmethod
    def random():
        """Random username and password for registration."""
        store_name = fake.word()
        return store_name


class CreateStoreSuccessful(BaseModel):
    """Successful user registering response model."""

    name: str
    items: list
    uuid: int


class NotCreateStore(BaseModel):
    """Successful user registering response model."""

    description: str
    error: str
    status_code: int


class StoreAlreadyExist(BaseModel):
    """Successful user registering response model."""

    message: str


class StoreInfo(BaseModel):
    """Successful user registering response model."""

    name: str
    items: list
    uuid: int
