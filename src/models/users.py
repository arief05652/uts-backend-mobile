from typing import TYPE_CHECKING

from tortoise import Model, fields

if TYPE_CHECKING:
    from .urls import Urls


class Users(Model):
    user_id = fields.CharField(max_length=36, null=False, primary_key=True)
    user_device_id = fields.CharField(max_length=36, null=False)

    urls: fields.ReverseRelation["Urls"]

    class Meta:
        table = "users"
        description = "user yang memakai akan didaftarkan dengan device id"
