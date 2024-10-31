from graphene import ObjectType, Int, String, Field, Float


class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    latitude = Float()
    longitude = Float()


    # user_id = Int()
    # user = Field("app.gql.types.user_type.UserType")
    #
    # @staticmethod
    # def resolve_user(root, info):
    #     with session_maker() as session:
    #         return session.query(UserDetails).filter(UserDetails.id == root.user_id).first()
