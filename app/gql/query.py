from graphene import ObjectType, List, Field, Int

from app.gql.types.city_type import AddressType
from app.gql.types.country_type import CreditcardType
from app.gql.types.target_type import UserType
from app.repository.address_repository import get_all_addresses, get_address_by_id
from app.repository.creditcard_repository import get_all_cards, get_card_by_id
from app.repository.user_repository import get_all_users, get_user_by_id


class Query(ObjectType):
    users = List(UserType)
    credit_cards = List(CreditcardType)
    addresses = List(AddressType)
    user_by_id = Field(UserType, user_id=Int())
    card_by_id = Field(CreditcardType, user_id=Int())
    address_by_id = Field(AddressType, user_id=Int())

    @staticmethod
    def resolve_users(root, info):
        return get_all_users()

    @staticmethod
    def resolve_credit_cards(root, info):
        return get_all_cards()

    @staticmethod
    def resolve_addresses(root, info):
        return get_all_addresses()

    @staticmethod
    def resolve_user_by_id(root, info, user_id):
        return get_user_by_id(user_id).value_or(None)

    @staticmethod
    def resolve_card_by_id(root, info, card_id):
        return get_card_by_id(card_id)

    @staticmethod
    def resolve_address_by_id(root, info, address_id):
        return get_address_by_id(address_id)