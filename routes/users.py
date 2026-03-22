from fastapi import APIRouter, HTTPException
from config.db import engine
from config.models.users import users
from schemas.users import User

router = APIRouter()



@router.get("/")
async def get_all_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()
        return [row._asdict() for row in result]



@router.get("/{id}")
async def get_user(id: int):
    with engine.connect() as conn:
        result = conn.execute(
            users.select().where(users.c.id == id)
        ).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="User not found")

        return result._asdict()



@router.post("/")
async def create_user(user_data: User):
    with engine.connect() as conn:
        try:
            conn.execute(users.insert().values(
                name=user_data.name,
                email=user_data.email,
                password=user_data.password
            ))
            conn.commit()
            return {"message": "User created successfully"}
        except Exception as e:
            conn.rollback()
            raise HTTPException(status_code=400, detail=str(e))



@router.put("/{id}")
async def update_user(id: int, user_data: User):
    with engine.connect() as conn:
        check = conn.execute(
            users.select().where(users.c.id == id)
        ).fetchone()

        if not check:
            raise HTTPException(status_code=404, detail="User not found")

        conn.execute(users.update().where(users.c.id == id).values(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password
        ))
        conn.commit()

        return {"message": "User updated successfully"}



@router.delete("/{id}")
async def delete_user(id: int):
    with engine.connect() as conn:
        check = conn.execute(
            users.select().where(users.c.id == id)
        ).fetchone()

        if not check:
            raise HTTPException(status_code=404, detail="User not found")

        conn.execute(users.delete().where(users.c.id == id))
        conn.commit()

        return {"message": "User deleted successfully"}