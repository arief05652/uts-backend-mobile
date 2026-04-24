from typing import TYPE_CHECKING

from tortoise import Model, fields

if TYPE_CHECKING:
    from .count import Count
    from .users import Users


class Urls(Model):
    url_id = fields.CharField(max_length=36, primary_key=True)
    user: fields.ForeignKeyRelation["Users"] = fields.ForeignKeyField(
        "models.Users", related_name="urls"
    )
    original_link = fields.TextField()
    cut_link = fields.TextField()
    password = fields.CharField(max_length=255, null=True)
    create_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)

    counts: fields.ReverseRelation["Count"]

    class Meta:
        table = "urls"
        description = "menampung seluruh url yang dikirim user"
