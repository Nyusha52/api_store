from faker import Faker
from faker.generator import random
from pydantic import BaseModel
from typing import Optional

fake = Faker()


class Item(BaseModel):
    item: str

    @staticmethod
    def random():
        return fake.word()


class ItemData(BaseModel):
    """ """
    price: int
    store_id: int
    description: Optional[str] = None
    image: Optional[str] = None

    @staticmethod
    def random(store_id):
        return ItemData(
            price=random.randint(5, 15000), store_id=store_id, description=" ".join(fake.words(8)),
            image=fake.word()
        )


class CreateItemSuccessful(BaseModel):
    """ ."""

    name: str
    price: float
    itemID: int
    description: str
    image: str


class ItemAlreadyExists(BaseModel):
    """ ."""

    message: str


class ItemInfo(BaseModel):
    """ ."""

    name: str
    price: float
    itemID: int
    description: str
    image: str


class UpdateInfo(BaseModel):
    """ ."""

    name: str
    price: float
    itemID: int
    description: str
    image: str
