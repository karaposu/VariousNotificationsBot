from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(String, unique=True)
    email = Column(String, nullable=True)
    api_keys = relationship("APIKey", back_populates="user")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class APIKey(Base):
    __tablename__ = 'api_keys'
    api_key_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    api_key = Column(String, unique=True)
    user = relationship("User", back_populates="api_keys")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

# Global engine and session factory
engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def save_new_user_to_database(telegram_id, email, generated_api_key):
    with Session() as session:
        try:
            new_user = User(telegram_id=telegram_id, email=email)
            new_api_key = APIKey(api_key=generated_api_key, user=new_user)
            session.add(new_user)
            session.add(new_api_key)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
