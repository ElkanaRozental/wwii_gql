from typing import List

from returns.maybe import Maybe, Some, Nothing
from returns.result import Result, Success, Failure

from app.db.database import session_maker
from app.models import TargetType, Mission, Target


def get_plains_by_target_type_name(target_type) -> List[Maybe[TargetType]]:
    with session_maker() as session:
        missions = (session.query(TargetType, Mission, Target)
                    .join(Target, TargetType.target_type_id == Target.target_type_id)
                    .join(Mission, Mission.mission_id == Target.mission_id)
                    .filter(TargetType.target_type_name == target_type)
                    .all())
        return Some(missions) if missions else Nothing


def create_target(target: Target) -> Result[Target, str]:
    with session_maker() as session:
        try:
            session.add(target)
            session.commit()
            session.refresh(target)
            return Success(target).value_or(None)
        except Exception as e:
            session.rollback()
            return Failure(str(e))
