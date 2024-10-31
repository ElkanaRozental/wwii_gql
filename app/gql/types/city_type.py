from graphene import ObjectType, Int, String, Field, Float, List

from app.db.database import session_maker
from app.models import Target


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    latitude = Float()
    longitude = Float()

    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_target(root, info):
        with session_maker() as session:
            return session.query(Target).filter(Target.city_id == root.id)

