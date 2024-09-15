import os

from dotenv import load_dotenv


load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
SWAGGER = os.environ.get("SWAGGER")

DATASET = os.environ.get("DATASET")


class FirstDb:
    user = os.environ.get("FIRST_DB_POSTGRES_USER")
    password = os.environ.get("FIRST_DB_POSTGRES_PASSWORD")
    host = os.environ.get("FIRST_DB_DB_HOST")
    port = os.environ.get("FIRST_DB_INTERNAL_DB_PORT")
    db_name = os.environ.get("FIRST_DB_POSTGRES_DB")
    collection_name = os.environ.get("FIRST_DB_COLLECTION_NAME")


class ConfigDataBaseFirstExample:
    emb_model = os.environ.get("DataBaseFirstExample_EMBEDDINGS_MODEL_NAME")
    search_kwargs = eval(os.environ.get("DataBaseFirstExample_SEARCH_KWARGS"))
    temperature = float(os.environ.get("DataBaseFirstExample_TEMPERATURE"))
    chat_model = os.environ.get("DataBaseFirstExample_CHAT_MODEL_NAME")
    chain_type = os.environ.get("DataBaseFirstExample_CHAIN_TYPE")
    template = os.environ.get("DataBaseFirstExample_TEMPLATE")


class SecondDb:
    user = os.environ.get("SECOND_DB_POSTGRES_USER")
    password = os.environ.get("SECOND_DB_POSTGRES_PASSWORD")
    host = os.environ.get("SECOND_DB_DB_HOST")
    port = os.environ.get("SECOND_DB_INTERNAL_DB_PORT")
    db_name = os.environ.get("SECOND_DB_POSTGRES_DB")
    collection_name = os.environ.get("SECOND_DB_COLLECTION_NAME")


class ConfigDataBaseSecondExample:
    emb_model = os.environ.get("DataBaseSecondExample_EMBEDDINGS_MODEL_NAME")
    search_kwargs = eval(os.environ.get("DataBaseSecondExample_SEARCH_KWARGS"))
    temperature = float(os.environ.get("DataBaseSecondExample_TEMPERATURE"))
    chat_model = os.environ.get("DataBaseSecondExample_CHAT_MODEL_NAME")
    chain_type = os.environ.get("DataBaseSecondExample_CHAIN_TYPE")
    template = os.environ.get("DataBaseSecondExample_TEMPLATE")

