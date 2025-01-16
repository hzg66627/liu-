
import jwt
from fastapi import FastAPI, HTTPException, Depends, Request
from tortoise.contrib.fastapi import register_tortoise
from passlib.context import CryptContext
from datetime import datetime, timedelta
from models import User, LoginHistory
from auth import get_password_hash, verify_password, encode_auth_token, decode_token
import redis

app = FastAPI()


redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)


register_tortoise(
    app,
    db_url='mysql://root:Liu94326@127.0.0.1:3306/auth',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.post("/register")
async def register(email: str, password: str):
    user = await User.get_or_none(email=email)
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(password)
    new_user = await User.create(email=email, hashed_password=hashed_password)

    return {"message": "User created successfully"}


@app.post("/login")
async def login(email: str, password: str, request: Request):
    user = await User.get_or_none(email=email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = encode_auth_token(user.id)
    refresh_token = encode_auth_token(user.id)


    user_agent = request.headers.get("User-Agent")
    await LoginHistory.create(user=user, user_agent=user_agent)

    return {"access_token": access_token, "refresh_token": refresh_token}


@app.post("/refresh")
async def refresh(refresh_token: str):
    user_id = decode_token(refresh_token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid refresh token")


    if redis_client.exists(f"invalid_refresh_token:{refresh_token}"):
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    access_token = encode_auth_token(user_id)
    return {"access_token": access_token}


@app.put("/user/update")
async def update_user(email: str, password: str, user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.email = email
    user.hashed_password = get_password_hash(password)
    await user.save()

    return {"message": "User updated successfully"}


@app.get("/user/history")
async def get_login_history(user_id: int):
    history = await LoginHistory.filter(user_id=user_id).all()
    return [{"user_agent": h.user_agent, "datetime": h.datetime} for h in history]


@app.post("/logout")
async def logout(user_id: int, access_token: str, refresh_token: str):

    redis_client.set(f"invalid_access_token:{access_token}", "invalid", ex=3600)  # 1小时过期
    redis_client.set(f"invalid_refresh_token:{refresh_token}", "invalid", ex=3600)  # 1小时过期

    return {"message": "Logged out successfully"}



def is_token_invalid(token: str) -> bool:
    return redis_client.exists(f"invalid_access_token:{token}") or redis_client.exists(f"invalid_refresh_token:{token}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app",host='127.0.0.1',port=8080,reload=True,workers=1)