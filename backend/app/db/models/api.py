import random
import string
from sqlalchemy import UniqueConstraint, text
from sqlmodel import Field
import uuid as uuid_pkg
import OpenSSL


from .common import UUIDModel, TimestampModel


def gen_uuid():
    return str(uuid_pkg.uuid4()).replace("-", "")


class ApiKey(UUIDModel, TimestampModel, table=True):
    __tablename__ = "api_keys"
    __table_args__ = (UniqueConstraint("api_key"),)

    api_key: str = Field(
        default_factory=gen_uuid,
        index=True,
        nullable=False,
    )
    user_id: uuid_pkg.UUID = Field(foreign_key="users.id")

    def __repr__(self):
        return f"api_key: {self.key}"
