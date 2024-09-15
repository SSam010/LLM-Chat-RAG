from chat.resources._base import ResourceRouter
from chat.resources.start_page import router as start_router
from config import DATASET

router = ResourceRouter()
router.include_router(start_router)


if DATASET == "first_db_rag":
    from chat.resources.first_db_rag import Router as first_sourse_router

    router.add_resource(first_sourse_router())

elif DATASET == "second_db_rag.py":
    from chat.resources.second_db_rag import Router as second_sourse_router

    router.add_resource(second_sourse_router())
