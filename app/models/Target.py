from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.models import Base


class Target(Base):
    __tablename__ = 'targets'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    target_industry = Column(String)
    target_priority = Column(Integer)

    target_type_id = (Integer, ForeignKey('targettypes.target_type_id'))
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    mission_id = Column(Integer, ForeignKey('missions.mission_id'))

    mission = relationship("Mission", back_populates='targets')
    target_type = relationship("TargetType", back_populates='targets')
    city = relationship("City", back_populates='targets')