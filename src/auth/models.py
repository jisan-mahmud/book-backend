from tortoise import models, fields
import uuid

class User(models.Model):
    id = fields.UUIDField(pk= True, default= uuid.uuid4)
    username = fields.CharField(max_length= 50, unique= True, blank= True, null= True)
    email = fields.CharField(max_length= 250, unique= True)
    hashed_password = fields.CharField(max_length=255)
    full_name = fields.CharField(max_length= 200, blank= True, null= True)

    is_active = fields.BooleanField(default= True)
    is_superuser = fields.BooleanField(default= True)

    joining_date = fields.DatetimeField(auto_now_add= True)
    last_login = fields.DatetimeField(blank= True, null= True)


    class Meta:
        table = "users"
        ordering = ["-joining_date"]