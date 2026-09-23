from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.database import Base

class OfferImage(Base):
    __tablename__ = "offer_image"
    id = Column(Integer, primary_key=True)
    offer_id = Column(Integer,
        ForeignKey(
            "offers.id",
            ondelete="CASCADE"
        ),
        nullable=False)
    original_url = Column(String)
    local_path = Column(String)

    offer = relationship(
        "Offer",
        back_populates="images"
    )
