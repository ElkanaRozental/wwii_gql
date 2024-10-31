from typing import List

from returns.maybe import Maybe, Some, Nothing

from app.db.database import session_maker
from app.models import TargetType, Mission


def get_plains_by_target_type_name(type) -> List[Maybe[TargetType]]:
    with session_maker() as session:
        missions = (session.query(TargetType)
                    .filter(TargetType.Target.mission_id == Mission.mission_id)
                    .filter(TargetType.target_type_name == type)
                    .all())
        return Some(missions) if missions else Nothing

