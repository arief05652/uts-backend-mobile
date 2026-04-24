from typing import Optional

from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.models import Urls

router = APIRouter()

template = Jinja2Templates(directory="src/templates")


@router.get("/{cut_url}", response_class=HTMLResponse)
async def redirect_web(req: Request, cut_url: str, status: Optional[str] = None):
    url = await Urls.get_or_none(cut_link=cut_url)

    if url is None:
        return template.TemplateResponse(request=req, name="not_found.html")

    else:
        if url.password:
            return template.TemplateResponse(
                request=req,
                name="lock.html",
                context={
                    "cut_url": cut_url,
                    "url_id": url.url_id,
                    "detail": "Password Salah" if status else status,
                },
            )
        else:
            return RedirectResponse(url=url.original_link)


@router.post("/unlock/{cut_url}/", response_class=HTMLResponse)
async def locked_reference(
    cut_url: str, url_id: str, password: str | None = Form(None)
):
    valid = await Urls.get(url_id=url_id)

    if password is None or password != valid.password:
        return RedirectResponse(f"/{cut_url}?status=salah", 303)

    return RedirectResponse(valid.original_link, 303)
