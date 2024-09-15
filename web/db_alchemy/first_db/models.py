from sqlalchemy import Column, Integer, select
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base

from db_alchemy.first_db.connect import db

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(JSONB)

    @classmethod
    async def get_str_count_abs(cls):
        data = await cls.get_data_abs()
        return map(lambda x: x.get("view"), data)

    @classmethod
    async def get_data_abs(cls):
        try:
            await db.connect()
            return await db.session.scalars(select(cls.data))
        finally:
            await db.disconnect()

    @classmethod
    async def get_article(cls, id):
        try:
            await db.connect()
            return await db.session.scalar(
                select(cls.data).where(cls.data.contains({"id": id}))
            )

        finally:
            await db.disconnect()
