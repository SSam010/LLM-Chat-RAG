from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from config import DATASET
from logger import config as logger_conf

logger = logger_conf.setup_logger()


"""
If there is a source link, you need to put it into PRIMARY_SOURCES. You also need to return
 article id as a dict key "id" in metadata.
"""
PRIMARY_SOURCES = {
    "first_db_rag": "https://your-first-resource-link",
    "second_db_rag": "https://your-second-resource-link",
}

PRIMARY_SOURCES_PAGE = {
    "first_db_rag": "main_page_v2.html",
    "second_db_rag": "main_page_v2.html",
}

PRESETS = {
    "first_db_rag": [
        "What can you do?",
        "Tell me about Ai",
        "What do you think about Elon Musk",
    ],
    "second_db_rag": [
        "How are you?",
        "What would be better: an icecream or an apple?",
        "What's the weather today?",
    ],
}

BANNERS = {
    "first_db_rag": [
        "ChatWithFirstSource: Interactive Review and Response",
        '"Let\'s start"',
    ],
    "second_db_rag": [
        "ChatWithSecondSource: Interactive Review and Response",
        '"Let\' speak about everything in the world!"',
    ],
}

router = APIRouter(prefix="", tags=["chat"])


@router.get("/")
async def get_chat(request: Request):
    templates = Jinja2Templates(directory="static/templates")
    return templates.TemplateResponse(
        PRIMARY_SOURCES_PAGE.get(DATASET, "main_page.html"),
        {
            "request": request,
            "dataset": DATASET,
            "primary_source": PRIMARY_SOURCES.get(DATASET, "None"),
            "presets": PRESETS.get(DATASET, []),
            "banner": BANNERS.get(
                DATASET,
                [
                    "",
                ],
            ),
        },
    )
