from db.models.common import TimestampModel, UUIDModel


class ContactUs(TimestampModel, UUIDModel, table=True):
    __tablename__ = "contact_us"

    name: str
    email: str
    message: str

    class Config:
        arbitrary_types_allowed = True
        
    def __repr__(self):
        return f"<ContactUs (id: {self.id})>"
