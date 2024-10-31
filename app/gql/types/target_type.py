from graphene import ObjectType, Int, String, Field, List

import app.gql.types.targettype_type


class TargetType(ObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = String()



