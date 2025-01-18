from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
import datetime
from database import Base


# City model
class City(Base):
    __tablename__ = "city"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False, unique=True)
    additional_info: str = Column(String(1000), nullable=False)


# Temperature model
class Temperature(Base):
    __tablename__ = "temperature"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    city_id: int = Column(Integer, ForeignKey("city.id"), nullable=False)
    datetime: datetime = Column(
        DateTime,
        default=datetime.datetime.now(datetime.timezone.utc),
        nullable=False,
    )
    temperature: float = Column(Float, nullable=False)
