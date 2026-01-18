from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.core.database import Base




class Category(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    products = relationship('Product', back_populates='category')