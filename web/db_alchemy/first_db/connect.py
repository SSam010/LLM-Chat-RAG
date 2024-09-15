from config import FirstDb as db_conf
from db_alchemy._base.connect import Database

db = Database(
    user=db_conf.user,
    password=db_conf.password,
    host=db_conf.host,
    port=db_conf.port,
    db_name=db_conf.db_name,
    collection_name=db_conf.collection_name,
)
