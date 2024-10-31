from graphene import ObjectType, Int, String


class TargetType(ObjectType):
    target_id = Int()
    target_industry = String()
    target_priority = String()
