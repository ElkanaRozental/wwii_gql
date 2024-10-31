from graphene import ObjectType, Int, String


class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()
