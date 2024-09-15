from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from logger import config as logger
from chat.router import router
from config import SWAGGER

logger.setup_logger()

app = FastAPI(
    title="OnlyTalk",
    docs_url="/docs" if int(SWAGGER) else None,
    redoc_url="/redoc" if int(SWAGGER) else None,
)

app.include_router(router)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(404)
async def not_found_handler(request: Request, exc: Exception):
    return RedirectResponse(url="/")
