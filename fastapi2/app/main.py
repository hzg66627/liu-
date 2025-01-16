
import uvicorn
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM
from student import student_api,group_api


app = FastAPI()
app.include_router(student_api, prefix="/students")
app.include_router(group_api, prefix="/groups")


register_tortoise(
    app,
    config=TORTOISE_ORM,
    generate_schemas=True,
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True,
               workers=1)
