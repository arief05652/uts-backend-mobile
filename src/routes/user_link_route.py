import io
from datetime import datetime

import qrcode
from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from tortoise.functions import Count as CountFunc

from src.models import Count, Urls

router = APIRouter()


class UserLink(BaseModel):
    user_id: str
    url_id: str
    original_link: str
    cut_link: str
    password: str | None = None
    total_click: int
    create_at: datetime
    modified_at: datetime


class Detail(BaseModel):
    total: int
    limit: int
    offset: int
    link_detail: list[UserLink]


@router.get("/get_user_link/", response_model=Detail)
async def get_user_link(device_id: str, limit: int = 2, offset: int = 0):
    query = Urls.filter(user__user_device_id=device_id)

    total = await query.count()

    if total == 0:
        raise HTTPException(404, "Data tidak ditemukan.")

    data = (
        await query.select_related("user")
        .annotate(total_click=CountFunc("counts"))
        .order_by("-create_at")
        .limit(limit)
        .offset(offset)
    )

    result = [
        UserLink(
            user_id=url.user.user_id,
            url_id=url.url_id,
            original_link=url.original_link,
            cut_link=url.cut_link,
            password=url.password,
            total_click=url.total_click,
            create_at=url.create_at,
            modified_at=url.modified_at,
        )
        for url in data
    ]

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "link_detail": result,
    }


@router.get("/get_link_detail")
async def get_detail_link(url_id: str, limit: int = 2, offset: int = 0):
    data = await Count.filter(url__url_id=url_id).limit(limit).offset(offset)

    return {
        "total": len(data),
        "limit": limit,
        "offset": offset,
        "data": data,
    }


@router.delete("/delete_link", status_code=200)
async def delete_link(url_id: str):
    url = await Urls.get_or_none(url_id=url_id)

    if url is None:
        raise HTTPException(status_code=404, detail="URL tidak ditemukan")

    await url.delete()

    return {"message": "Url berhasil dihapus"}


@router.patch("/update_link/{url_id}/")
async def update_link_detail(url_id: str, new_pass: str):
    data = await Urls.get_or_none(url_id=url_id)

    if data is None:
        raise HTTPException(status_code=404, detail="URL tidak ditemukan")

    data.password = new_pass
    await data.save()

    return {"message": "Berhasil update password"}


@router.get("/gen_qr")
async def generate_qrcode(url_id: str):
    data = await Urls.get_or_none(url_id=url_id)

    if data is None:
        raise HTTPException(detail="Url tidak ditemukan", status_code=404)

    qr = qrcode.QRCode(error_correction=qrcode.ERROR_CORRECT_L)
    qr.add_data(f"https://chunk.my.id/{data.cut_link}")
    qr.make()

    img = qr.make_image()

    buff = io.BytesIO()
    img.save(buff)
    buff.seek(0)

    return StreamingResponse(buff, media_type="image/png")
