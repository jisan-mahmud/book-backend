from tortoise import fields, models

class Book(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, null=False)
    author = fields.CharField(max_length=100, null=False)

    created_by = fields.ForeignKeyField('auth.User', on_delete= fields.CASCADE, related_name= 'books', null=  False)
    created_at = fields.DatetimeField(auto_now_add= True)

    class Meta:
        table = "books"
