from tortoise import fields, models

class Book(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100, null=False)
    author = fields.CharField(max_length=100, null=False)
    create_at = fields.DatetimeField(auto_now_add= True)

    class Meta:
        table = "books"
