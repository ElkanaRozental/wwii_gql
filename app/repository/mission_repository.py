from typing import List

from returns.maybe import Maybe, Nothing, Some
from returns.result import Result, Success, Failure

from app.db.database import session_maker
from app.models import Mission, Target, Country, City, TargetType


def get_mission_by_id(mission_id) -> Maybe[Mission]:
    with session_maker() as session:
        mission = session.query(Mission).filter(Mission.mission_id == mission_id).first()
        return Some(mission) if mission else Nothing


def get_mission_type_name(target_type) -> List[Mission]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .join(Mission.targets)
                    .join(Target.target_type)
                    .filter(TargetType.target_type_name == target_type)
                    .all())
        return missions


def get_mission_between_date(start_date, end_date) -> List[Mission]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .filter(start_date <= Mission.mission_date <= end_date)
                    .all())
        return missions


def get_mission_by_country_name(country_name) -> List[Mission]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .join(Mission.targets)
                    .join(Target.city)
                    .join(City.country)
                    .filter(Country.country_name == country_name)
                    .all())
        return missions


def get_mission_by_target_industry(target_industry) -> List[Mission]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .join(Mission.targets)
                    .filter(Target.target_industry == target_industry)
                    .all())
        return missions


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