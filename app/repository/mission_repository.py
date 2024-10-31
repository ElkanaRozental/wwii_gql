from typing import List

from returns.maybe import Maybe, Nothing, Some
from returns.result import Result, Success, Failure

from app.db.database import session_maker
from app.models import Mission, Target, Country


def get_mission_by_id(mission_id) -> Maybe[Mission]:
    with session_maker() as session:
        mission = session.query(Mission).filter(Mission.id == mission_id).first()
        return Some(mission) if mission else Nothing


def get_mission_between_date(start_date, end_date) -> List[Maybe[Mission]]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .filter(start_date <= Mission.mission_date <= end_date)
                    .all())
        return Some(missions) if missions else Nothing


def get_mission_by_country_name(country_name):
    with session_maker() as session:
        missions = (session.query(Mission)
                    .filter(Mission.Target.City.Country.country_name == country_name)
                    .all())
        return Some(missions) if missions else Nothing


def get_mission_by_target_industry(target_industry) -> List[Maybe[Mission]]:
    with session_maker() as session:
        missions = (session.query(Mission)
                    .filter(Mission.Target.target_industry == target_industry)
                    .all())
        return Some(missions) if missions else Nothing


def create_mission(mission: Mission) -> Result[Mission, str]:
    with session_maker() as session:
        try:
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except Exception as e:
            session.rollback()
            return Failure(str(e))