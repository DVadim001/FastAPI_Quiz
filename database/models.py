from sqlalchemy import Column, DateTime, String, Boolean, ForeignKey, Integer, Time
from sqlalchemy.orm import relationship
from database import Base


# Таблице пользователей
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    phone_number = Column(Integer, unique=True)
    level = Column(String, default="None")
    created_at = Column(DateTime)


# Таблица вопросов
class Questions(Base):
    __tablename__ = "questions"
    id = Column(Integer, autoincrement=True, primary_key=True)
    q_text = Column(String)
    v1 = Column(String)
    v2 = Column(String)
    v3 = Column(String)
    v4 = Column(String)
    correct_answer = Column(Integer, nullable=False)
    timer = Column(Time)
    created_at = Column(DateTime)


# Таблица результатов и для лидеров
class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    correct_answer = Column(Integer, default=0)
    level = Column(String)

    user_fk = relationship(User, lazy='subquery')


# Ответы пользователя на вопрос
class UserAnswers(Base):
    __tablename__ = "user_answers"
    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    q_id = Column(Integer, ForeignKey('questions.id'))
    level = Column(String, ForeignKey('users.level'))
    corectness = Column(Boolean, default=False)
    user_answer = Column(Integer)
    timer = Column(Time)

    user_fk = relationship(User, foreign_keys=[user_id], lazy='subquery')
    question_fk = relationship(Questions, foreign_keys=[q_id], lazy='subquery')
