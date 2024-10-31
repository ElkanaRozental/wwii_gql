from graphene import ObjectType, Int, Date, Float, List

import app.gql.types.target_type
from app.db.database import session_maker
from app.models import Target


class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft = Float()
    aircraft_returned = Float()
    aircraft_failed = Float()
    aircraft_damaged = Float()
    aircraft_lost = Float()

    targets = List('app.gql.types.target_type.TargetType')

    @staticmethod
    def resolve_target(root, info):
        with session_maker() as session:
            return session.query(Target).filter(Target.mission_id == root.id)