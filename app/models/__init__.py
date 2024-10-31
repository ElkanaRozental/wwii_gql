from sqlalchemy.orm import declarative_base
Base = declarative_base()
from .City import City
from .Country import Country
from .Mission import Mission
from .Target import Target
from .TargetType import TargetType
