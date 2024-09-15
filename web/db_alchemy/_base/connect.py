import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


class Database:
    """
    THis class creates instance db connection.
    You need to specify the parameters for connecting to the database,
     in ENV names as string.
    """

    def __init__(self, user, password, host, port, db_name, collection_name=None):
        self.connect_parameters = self._get_db_connect_parameters(
            user, password, host, port, db_name
        )
        self.SYNC_CONNECTION_STRING = f"postgresql+psycopg2://{self.connect_parameters}"
        self.ASYNC_CONNECTION_STRING = f"postgresql+asyncpg://{self.connect_parameters}"
        self.COLLECTION_NAME = (
            os.environ.get(collection_name) if collection_name else None
        )
        self.engine = create_async_engine(self.ASYNC_CONNECTION_STRING)
        self.async_session = async_sessionmaker(self.engine)
        self.session = None

    @classmethod
    def _get_collection_name(cls, collection_name):
        return os.environ.get(collection_name) if collection_name else None

    @classmethod
    def _get_db_connect_parameters(cls, user, password, host, port, db_name):
        DB_HOST = os.environ.get(host)
        DB_PORT = os.environ.get(port)
        DB_DB = os.environ.get(db_name)
        DB_USER = os.environ.get(user)
        DB_PASSWORD = os.environ.get(password)
        return f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DB}"

    async def connect(self):
        if self.session is None:
            self.session = self.async_session()

    async def disconnect(self):
        if self.session is not None:
            await self.session.close()
            self.session = None
