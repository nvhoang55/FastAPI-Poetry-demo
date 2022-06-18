import uuid

from pydantic import BaseModel


class User(BaseModel):
    class FullName(BaseModel):
        first_name: str
        last_name: str

    full_name: FullName
    age: int
    id: str = uuid.uuid4()
    address: str
