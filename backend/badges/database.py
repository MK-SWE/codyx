from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)

class Challenge(Base):
    __tablename__ = "challenges"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))

class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255))

class UserBadge(Base):
    __tablename__ = "user_badges"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    badge_id = Column(Integer, ForeignKey("badges.id"), primary_key=True)

# Relationship between models
User.badges = relationship("Badge", secondary_table=UserBadge, backref="users")
Challenge.awarded_badges = relationship("Badge", secondary_table="challenge_badge_association", backref="challenges")  # Add another association table for challenge-badge relation

# Create the database engine
engine = create_engine("mysql://root:password@localhost/badges")
Base.metadata.create_all(engine)



