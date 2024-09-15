from abc import ABC, abstractmethod
from typing import Union

from fastapi import APIRouter, Request, Form
from starlette.templating import Jinja2Templates

from chat.schemas.chat import MessageRequest


class BaseRouter(ABC):
    prefix: str = ""
    tags: list[str] = []

    def __init__(self):
        self.router = APIRouter(prefix=self.prefix, tags=self.tags)
        self.router.post("/ask/")(self.ask)
        self.router.post("/article/{article_id}")(self.get_full_article)

    async def ask(self, message: MessageRequest):
        response = self.ask_model(message.text)
        return {"response": response}

    @abstractmethod
    def ask_model(self, text: str) -> dict:
        pass

    async def get_full_article(
        self, request: Request, article_id: Union[int, str], fragment: str = Form()
    ):
        response = await self.get_article(article_id)
        templates = Jinja2Templates(directory="static/templates")

        return templates.TemplateResponse(
            "full_text.html",
            {"request": request, "response": response, "fragment": fragment},
        )

    async def get_article(self, article_id: Union[int, str]) -> str:
        pass


class ResourceRouter(APIRouter):
    def add_resource(self, router_cls: BaseRouter):
        return self.include_router(router_cls.router)
