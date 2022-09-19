from pydantic import BaseModel

class create_category(BaseModel):
    category_id : int
    category_name: str

    