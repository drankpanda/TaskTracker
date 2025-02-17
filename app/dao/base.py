from sqlalchemy import select, update as sa_update, delete as sa_delete
from sqlalchemy.exc import SQLAlchemyError

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def find_all(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def add(cls, **values):
        async with async_session_maker() as session:
            async with session.begin():
                new_instance = cls.model(**values)
                session.add(new_instance)
                try:
                    await session.commit()
                except SQLAlchemyError as err:
                    await session.rollback()
                    raise err
                return new_instance

    @classmethod
    async def update(cls, filter_by, **values):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    sa_update(cls.model)
                    .where(*[getattr(cls.model, k) == v for k, v in filter_by.items()])
                    .values(**values)
                    .execution_options(synchronize_session='fetch')
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as err:
                    await session.rollback()
                    raise err
                return result.rowcount

    @classmethod
    async def delete(cls, delete_all: bool = False, **filter_by):
        if not delete_all and not filter_by:
            raise ValueError('Must be given at least one parameter: delete_all=True or some keyword filter')

        async with async_session_maker() as session:
            async with session.begin():
                query = sa_delete(cls.model).filter_by(**filter_by if not delete_all else None)
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as err:
                    await session.rollback()
                    raise err
                return result.rowcount
