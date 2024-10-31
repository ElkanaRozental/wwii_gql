from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.database import Base


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String)
    target_priority = Column(Integer)

    target_type_id = (Integer, ForeignKey('target_types.id'))
    city_id = Column(Integer, ForeignKey('cities.id'))
    mission_id = Column(Integer, ForeignKey('missions.id'))

    mission = relationship("Mission", back_populates='targets')
    target_type = relationship("TargetType", back_populates='target')
    city = relationship("City", back_populates='targets')