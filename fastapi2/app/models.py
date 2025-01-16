from tortoise.models import Model
from tortoise import fields

class Student(Model):
    id=fields.IntField(pk=True)
    name=fields.CharField(max_length=32)
    sno = fields.IntField(description='sno')
    groups = fields.ManyToManyField('models.Group', related_name='students')
class Group(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=32)


