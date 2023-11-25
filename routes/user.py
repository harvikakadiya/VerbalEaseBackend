from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

@user.get('/getUsers')
async def find_all_users():
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find())

@user.post('/registerUser')
async def create_user(user: User):
    print('here users============', user)
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())