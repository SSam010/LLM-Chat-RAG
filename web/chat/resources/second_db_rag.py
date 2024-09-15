from chat.core.second_db_rag import qa_chain
from chat.resources._base import BaseRouter
from chat.tools.text_wraps import process_llm_response
from logger import config as logger_conf


logger = logger_conf.setup_logger()


class Router(BaseRouter):
    prefix = "/second_db_rag"
    tags = ["chat"]

    def ask_model(self, text):
        llm_response = qa_chain(text)
        return process_llm_response(llm_response)
