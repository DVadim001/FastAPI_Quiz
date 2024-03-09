from fastapi import APIRouter
from database.userservice import register_user_db, user_answer_db, plus_point_user_db, get_all_users_db
from database.testservice import get_questions_db, add_question_db

user_router = APIRouter(prefix='/users', tags=['Работа с пользователями'])


# Регистрация
@user_router.post('/register')
async def register(name: str, phone_number: int, level: str):
    register_user = register_user_db(name, phone_number, level)
    return f'Вы успешно прошли регистрацию, {register_user}'


# Ответы пользователя
@user_router.get('/leaders')
async def get_leader(user_id: int, q_id: int, user_answer: str, level: str):
    get_leaders = user_answer_db(user_id, user_answer, q_id, level)
    return f'Лидеры: {get_leaders}'


# Увеличение баллов пользователя
@user_router.post('/plus')
async def plus_points(user_id: str, correct_answers: int):
    users_points = plus_point_user_db(user_id, correct_answers)
    return f'{users_points}'


# получить всех польхователей
@user_router.get('/all')
async def users_all():
    return get_all_users_db()
