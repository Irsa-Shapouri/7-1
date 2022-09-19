from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from databse import Base


class Category(Base):
    __tablename__ = "category"
    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, index=True)



# class User(Base):
#     user_id = int
#     user_name: str
#     user_last_name: str
#     user_password : str
#     user_phone_number : str


# class Brand(Base):
#     pass



