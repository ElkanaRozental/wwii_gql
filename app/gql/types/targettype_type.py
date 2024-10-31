from graphene import ObjectType, Int, String, List

from app.db.database import session_maker
from app.models import Target


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_target(root, info):
        with session_maker() as session:
            return session.query(Target).filter(Target.target_type_id == root.id)