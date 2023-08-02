from faker import Faker
from pydantic import BaseModel
from typing import Optional

fake = Faker()


class Address(BaseModel):
    """User address."""
    city: Optional[str] = None
    street: Optional[str] = None
    home_number: Optional[str] = None


class UserData(BaseModel):
    """Data to user info."""
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Address = None

    @staticmethod
    def random():
        address = Address(
            city=fake.city(),
            street=fake.street_name(),
            home_number=fake.building_number(),
        )
        return UserData(
            phone=fake.phone_number(), email=fake.email(), address=address
        )


class UserDataUpdateSuccessful(BaseModel):
    """ ."""

    message: str


class UserDataCreateSuccessful(BaseModel):
    """ ."""

    message: str


class GetUserInfo(BaseModel):
    city: str
    street: str
    userID: int
    phone: str
    email: str


class DeleteUserInfo(BaseModel):
    """ """

    message: str


class NoUserInfo(BaseModel):
    """."""

    message: str
