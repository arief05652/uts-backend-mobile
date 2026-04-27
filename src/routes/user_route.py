from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel

from src.models import Urls, Users

router = APIRouter()


class AddedLink(BaseModel):
    device_id: str
    original_link: str
    password: str | None


# insert ke table urls
async def link_added(
    url_id: str,
    user_id: str,
    original_link: str,
    cut_link: str,
    password: str | None,
):
    await Urls.create(
        url_id=url_id,
        user_id=user_id,
        original_link=original_link,
        cut_link=cut_link,
        password=password,
    )


@router.post("/add_link", status_code=201)
async def add_link(body: AddedLink):
    unique_id = str(uuid4())

    user_exist = await Users.get_or_none(user_device_id=body.device_id)

    # jika user ga ada
    if user_exist is None:
        user = await Users.create(user_id=unique_id, user_device_id=body.device_id)
        await link_added(
            url_id=str(uuid4()),
            user_id=user.user_id,
            original_link=body.original_link,
            password=body.password,
            cut_link=str(uuid4()).lower()[:8],
        )
    # user ada
    else:
        await link_added(
            url_id=str(uuid4()),
            user_id=user_exist.user_id,
            original_link=body.original_link,
            password=body.password,
            cut_link=str(uuid4()).lower()[:8],
        )

    return {"message": "Url berhasil didaftarkan."}
