from graphene import ObjectType, Int, String, Field

import app.gql.types.targettype_type


class TargetType(ObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = String()

    target_type_id = Int()
    target_type = Field('app.gql.types.targettype_type.TargetTypeType')

