from tortoise import fields, models

class Book(models.Model):
    id = fields.IntField(pk=True)  # Primary key, auto-increment by default
    name = fields.CharField(max_length=100, null=False)
    author = fields.CharField(max_length=100, null=False)

    class Meta:
        table = "books"  # Optional: specify table name
