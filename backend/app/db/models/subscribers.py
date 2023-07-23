from db.models.common import TimestampModel, UUIDModel


class Subscriber(UUIDModel, TimestampModel, table=True):
    __tablename__ = "subscribers"

    email: str
