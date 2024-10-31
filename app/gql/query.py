from graphene import ObjectType, List, Field, Int, Date, String

from app.gql.types.mission_type import MissionType


from app.repository.mission_repository import get_mission_by_id, get_mission_between_date, \
    get_mission_by_target_industry, get_mission_by_country_name, get_mission_type_name


class Query(ObjectType):
    mission_by_date = List(MissionType, first_date=Date(), end_date=Date())
    mission_by_id = Field(MissionType, mission_id=Int())
    mission_by_industry = List(MissionType, industry=String())
    mission_by_country = List(MissionType, country=String())
    mission_by_target_type = List(MissionType, target_type=String())

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
        return get_mission_by_id(mission_id).value_or(None)

    @staticmethod
    def resolve_mission_by_date(root, info, first_date, end_date):
        return get_mission_between_date(first_date, end_date)

    @staticmethod
    def resolve_mission_by_industry(root, info, industry):
        return get_mission_by_target_industry(industry)

    @staticmethod
    def resolve_mission_by_country(root, info, country):
        return get_mission_by_country_name(country)

    @staticmethod
    def resolve_mission_by_target_type(root, info, target_type):
        return get_mission_type_name(target_type)


# class Query(ObjectType):
#     get_missions = List(MissionType)
#     get_mission = Field(MissionType, mission_id=Int())
#     @staticmethod
#     def resolve_get_missions(root, info):
#         with session_maker() as session:
#             return session.query(Mission).all()
#
#     @staticmethod
#     def resolve_get_mission(root, info, mission_id):
#         with session_maker() as session:
#             return session.query(Mission).filter(Mission.mission_id == mission_id).first()
