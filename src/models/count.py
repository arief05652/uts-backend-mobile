from typing import TYPE_CHECKING
from uuid import uuid4

from tortoise import Model, fields

if TYPE_CHECKING:
    from .urls import Urls


class Count(Model):
    count_id = fields.CharField(max_length=36, default=uuid4(), primary_key=True)
    url: fields.ForeignKeyRelation["Urls"] = fields.ForeignKeyField(
        "models.Urls", related_name="counts"
    )
    user_agent = fields.CharField(max_length=255)
    timestamp = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "count"
        description = "hitung seluruh aktivitas pada link"
