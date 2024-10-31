from graphene import Mutation, String, Int, Field

from app.gql.types.target_type import TargetType
from app.models import Target
from app.repository.target_repository import create_target


class AddTarget(Mutation):
    class Arguments:
        target_industry = String()
        target_priority = Int()

        target_type_id = Int()
        city_id = Int()
        mission_id = Int()

    target = Field(TargetType)

    @staticmethod
    def mutate(root, info,
               target_industry,
               target_priority,
               target_type_id,
               city_id,
               mission_id):
        target = Target(target_industry=target_industry,
                        target_priority=target_priority,
                        target_type_id=target_type_id,
                        city_id=city_id,
                        mission_id=mission_id)
        return create_target(target).value_or(None)