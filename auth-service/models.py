from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=320, unique=True)
    hashed_password = fields.CharField(max_length=100)
    LoginHistorys= fields.ManyToManyField('models.LoginHistory', related_name='users')

class LoginHistory(Model):
    id = fields.IntField(pk=True)
    user_agent = fields.CharField(max_length=255)
    datetime = fields.DatetimeField()
