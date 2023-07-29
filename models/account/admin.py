from fastapi_admin.models import AbstractAdmin
from tortoise import fields


class UserAdmin(AbstractAdmin):

    id = fields.BigIntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255, unique=True)

    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)

    created = fields.DatetimeField(auto_now_add=True)
    modified = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk}#{self.username}"
