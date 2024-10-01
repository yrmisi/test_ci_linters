from pathlib import Path

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, declared_attr

BASE_PATH = Path(__file__).parent
FILE_PATH = BASE_PATH.joinpath("cookbook.db")
DATABASE_URL = f"sqlite+aiosqlite:///{FILE_PATH}"

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)
session: AsyncSession = async_session()


class Base(DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
