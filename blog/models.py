from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Define the Blog model, every model should inherit from Base
class Blog(Base):
    __tablename__ = 'blogs' # Tên bảng trong database
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
