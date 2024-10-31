from graphene import ObjectType, List, Field, Int, Date, String

from app.gql.types.mission_type import MissionType
from app.gql.types.targettype_type import TargetTypeType

from app.repository.mission_repository import get_mission_by_id, get_mission_between_date, \
    get_mission_by_target_industry, get_mission_by_country_name
from app.repository.target_repository import get_plains_by_target_type_name


class Query(ObjectType):
    mission_by_date = List(MissionType, first_date=Date(), end_date=Date())
    mission_by_id = List(MissionType, mission_id=Int())
    mission_by_industry = List(MissionType, industry=String())
    mission_by_country = List(MissionType, country=String())
    plains_by_target_type = List(TargetTypeType, target_type=String())

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
    def resolve_plains_by_target_type(root, info, target_type):
        return get_plains_by_target_type_name(target_type)
