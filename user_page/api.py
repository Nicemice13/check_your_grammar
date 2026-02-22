from ninja import NinjaAPI, Schema
from django.contrib.auth.models import User
from django.db import connection
from .models import UserInfo
from typing import Optional

api = NinjaAPI()

class UserInfoSchema(Schema):
    phone: Optional[str] = None
    birthday: Optional[str] = None
    gender: Optional[bool] = None
    photo: Optional[str] = None

class UserSchema(Schema):
    id: int
    username: str
    email: str
    userinfo: Optional[UserInfoSchema] = None

@api.get("/users", response=list[UserSchema])
def list_users(request):
    users = User.objects.all()
    result = []
    for user in users:
        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }
        try:
            info = user.userinfo
            user_data["userinfo"] = {
                "phone": info.phone,
                "birthday": str(info.birthday) if info.birthday else None,
                "gender": info.gender,
                "photo": info.photo.url if info.photo else None,
            }
        except UserInfo.DoesNotExist:
            user_data["userinfo"] = None
        result.append(user_data)
    return result

@api.get("/users/{user_id}", response=UserSchema)
def get_user(request, user_id: int):
    user = User.objects.get(id=user_id)
    user_data = {
        "id": user.id,
        "username": user.username,
        "email": user.email,
    }
    try:
        info = user.userinfo
        user_data["userinfo"] = {
            "phone": info.phone,
            "birthday": str(info.birthday) if info.birthday else None,
            "gender": info.gender,
            "photo": info.photo.url if info.photo else None,
        }
    except UserInfo.DoesNotExist:
        user_data["userinfo"] = None
    return user_data

@api.get("/search_word")
def search_word(request, word: str):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM search_word(%s)", [word])
        rows = cursor.fetchall()
        results = [
            {
                "id": row[0],
                "user_id": row[1],
                "username": row[2],
                "language": row[3],
                "corrected_text": row[4],
                "created_at": row[5].isoformat() if row[5] else None
            }
            for row in rows
        ]
    return {"results": results}

@api.get("/search_container")
def search_container(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM searh_container")
        rows = cursor.fetchall()
        results = [{"corrected_text": row[0]} for row in rows]
    return {"results": results}
