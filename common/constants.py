"""Constants for tests."""


class Hosts:
    """Registration block constants."""

    LOCAL = "localhost:56733"


class ApiUrl:
    REGISTRATION = "register"
    AUTH = "auth"
    STORE = "store"
    USER_INFO = "user_info"
    STORE_ITEM = "item"


class Registration:
    """Registration block constants."""

    SUCCESS = "User created successfully."
    ALREADY_EXISTS = "A user with that username already exists"


class Auth:
    """Autorization block constants."""
    ERROR_MESSAGE = "Invalid credentials"
    NO_USER = {
        "username": "Michaeli Kelly",
        "password": "(zlsA8Djg6"
    }


class StoreMessage:
    """Store  block constants."""

    @staticmethod
    def genetate_already_exists_message(store_name):
        return f"A store with name '{store_name}' already exists."


class UserInfoMessage:
    """Store  block constants."""

    SUCCESS_ADD = "User info created successfully."
    SUCCESS_EDIT = "User info updated successfully."
    NOT_FOUND = "User info not found"
    SUCCESS_DELETE = "User info deleted."


class ItemMessage:
    """Store  block constants."""

    @staticmethod
    def genetate_already_exists_message(item_name):
        return f"An item with name {item_name} already exists."
