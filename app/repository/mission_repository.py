from typing import List

from returns.maybe import Maybe, Nothing, Some
from returns.result import Result, Success, Failure

from app.db.database import session_maker
from app.models import Mission, Target, Country, City


def get_mission_by_id(mission_id) -> Maybe[Mission]:
    with session_maker() as session:
        mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
        return Some(mission) if mission else Nothing


def get_mission_between_date(start_date, end_date) -> List[Maybe[Mission]]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .filter(start_date <= Mission.mission_date <= end_date)
                    .all())
        return Some(missions) if missions else Nothing


def get_mission_by_country_name(country_name):
    with session_maker() as session:
        missions = (session.query(Mission, Target, City, Country)
                    .join(Target, Mission.mission_id == Target.mission_id)
                    .join(City, City.city_id == Target.city_id)
                    .join(Country, Country.country_id == City.country_id)
                    .filter(Country.country_name == country_name)
                    .all())
        return Some(missions) if missions else Nothing


def get_mission_by_target_industry(target_industry) -> List[Maybe[Mission]]:
    with session_maker() as session:
        missions = (session.query(Mission, Target)
                    .join(Target, Target.mission_id == Mission.mission_id)
                    .filter(Target.target_industry == target_industry)
                    .all())
        return Some(missions) if missions else Nothing


def create_mission(mission: Mission) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission).value_or(None)
        except Exception as e:
            session.rollback()
            return Failure(str(e))


def update_mission(mission_id, mission: Mission) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            mission_to_update = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            mission_to_update.aircraft_returned = mission.aircraft_returned
            mission_to_update.aircraft_lost = mission.aircraft_lost
            mission_to_update.aircraft_damaged = mission.aircraft_damaged
            mission_to_update.aircraft_failed = mission.aircraft_failed
            session.commit()
            return Success(mission_to_update).value_or(None)
        except Exception as e:
            session.rollback()
            return Failure(str(e))


def delete_mission(mission_id) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
            session.delete(mission)
            session.commit()
            return Success(mission).value_or(None)
        except Exception as e:
            session.rollback()
            return Failure(str(e))