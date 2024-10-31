from graphene import Mutation, Int, Date, Float, Field

from app.gql.types.mission_type import MissionType
from app.models import Mission
from app.repository.mission_repository import create_mission, update_mission, delete_mission


class AddMission(Mutation):
    class Arguments:
        mission_id = Int()
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info,
               mission_date,
               airborne_aircraft,
               attacking_aircraft,
               bombing_aircraft,
               aircraft_returned,
               aircraft_failed,
               aircraft_damaged,
               aircraft_lost):
        mission = Mission(mission_date=mission_date,
                          airborne_aircraft=airborne_aircraft,
                          attacking_aircraft=attacking_aircraft,
                          bombing_aircraft=bombing_aircraft,
                          aircraft_returned=aircraft_returned,
                          aircraft_failed=aircraft_failed,
                          aircraft_damaged=aircraft_damaged,
                          aircraft_lost=aircraft_lost
                          )
        return create_mission(mission).value_or(None)


class UpdateMission(Mutation):
    class Arguments:
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()

        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info,
               mission_id,
               aircraft_returned,
               aircraft_failed,
               aircraft_damaged,
               aircraft_lost):
        mission = Mission(aircraft_returned=aircraft_returned,
                          aircraft_failed=aircraft_failed,
                          aircraft_damaged=aircraft_damaged,
                          aircraft_lost=aircraft_lost
                          )
        return update_mission(mission_id, mission)


class DeleteMission(Mutation):
    class Arguments:
        mission_id = Int()

    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_id):
        return delete_mission(mission_id)

