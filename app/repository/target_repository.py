
from returns.result import Result, Success, Failure

from app.db.database import session_maker
from app.models import Target


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
