from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class TargetType(Base):
    __tablename__ = 'target_types'
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String)

    target = relationship("Target", back_populates='target_type')