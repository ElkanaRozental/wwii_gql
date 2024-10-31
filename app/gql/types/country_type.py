from graphene import ObjectType, Int, Date, String, List

from app.db.database import session_maker
from app.models import City, Mission


class CountryType(ObjectType):
    country_id = Int()
    country_name = String()

    cities = List('app.gql.types.city_type.CityType')

    @staticmethod
    def resolve_city(root, info):
        with session_maker() as session:
            return session.query(City).filter(City.country_id == root.id)

    @staticmethod
    def resolve_mission(root, info):
        with session_maker() as session:
            return session.query(Mission).filter(Mission.country_id == root.id)