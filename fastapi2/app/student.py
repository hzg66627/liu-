from fastapi.exceptions import HTTPException
from models import *
from pydantic import BaseModel
from typing import List, Union
from fastapi import APIRouter

student_api = APIRouter()
group_api = APIRouter()

class GroupModel(BaseModel):
    id: int
    name: str

class studentmodel(BaseModel):
    name:str
    id:int
    sno:int
    group_id:Union[int,None]=None

class GroupModel(BaseModel):
        id: int
        student_ids: List[int]

class RemoveStudentModel(BaseModel):
        student_ids: List[int]

class StudentResponseModel(BaseModel):
    id: int
    name: str
    sno: int

class TransferStudentModel(BaseModel):
    student_id: int
@student_api.get("/")
async def getallstudent():
    students = await Student.all()
    return students


@student_api.get("/{id}")
async def get_student(id: int):
    student = await Student.get(id=id)
    return student

@student_api.post("/")
async def create_Student(student_model: studentmodel):
    student = await Student.create(name=student_model.name, sno=student_model.sno, id=student_model.id,group_id=student_model.group_id)
    return student

@student_api.delete("/{id}")
async def deleteStudent(id: int):
    deletestudent = await Student.filter(id = id).delete()
    if not deletestudent:
        raise HTTPException(status_code=404)
    return("success")

@student_api.post("/groups/{group_id}/students/")
async def add_students_to_group(group_id: int, group_model: GroupModel):
    group = await Group.get(id=group_id)

    students = await Student.filter(id__in=group_model.student_ids)
    await group.students.add(*students)

    return {"message": "Students added to group successfully."}

@student_api.delete("/groups/{group_id}/students/")
async def remove_students_from_group(group_id: int, remove_model: RemoveStudentModel):
    group = await Group.get(id=group_id)
    students_to_remove = await Student.filter(id__in=remove_model.student_ids)
    await group.students.remove(*students_to_remove)
    return {"message": "Students removed from group successfully."}

@student_api.get("/groups/{group_id}/students/", response_model=List[StudentResponseModel])
async def get_students_in_group(group_id: int):
    group = await Group.get(id=group_id).prefetch_related('students')
    students = await group.students.all()
    return [StudentResponseModel(id=student.id, name=student.name, sno=student.sno) for student in students]

@student_api.post("/groups/{from_group_id}/transfer/{to_group_id}/")
async def transfer_student(from_group_id: int, to_group_id: int, transfer_model: TransferStudentModel):

    from_group = await Group.get(id=from_group_id).prefetch_related('students')
    to_group = await Group.get(id=to_group_id)

    student = await Student.get(id=transfer_model.student_id)

    if student not in from_group.students:
        raise HTTPException(status_code=400, detail="Student not found in the source group.")

    await from_group.students.remove(student)
    await to_group.students.add(student)

    return {"message": "Student transferred successfully."}


@group_api.get("/", response_model=List[GroupModel])
async def get_all_groups():
    groups = await Group.all()
    return groups


@group_api.get("/{id}", response_model=GroupModel)
async def get_group(id: int):
    group = await Group.get(id=id)
    return group


@group_api.post("/", response_model=GroupModel)
async def create_group(group_model: GroupModel):
    group = await Group.create(name=group_model.name, id=group_model.id)
    return group


@group_api.delete("/{id}")
async def delete_group(id: int):
    deleted_group = await Group.filter(id=id).delete()
    if not deleted_group:
        raise HTTPException(status_code=404, detail="Group not found")
    return {"message": "Group deleted successfully"}









