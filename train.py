from pydantic import BaseModel
from datetime import datetime
from typing import Annotated
class User(BaseModel):
    id :int
    name :str = "jhon doe"
    sign_ts : datetime | None =None
    friend :list[int] = []

person={
    "id" :"1",
    "sign_ts" :"2023-06-21 12:22",
    "friend" : [1, "2", b"3"]
    
}

user = User(**person)
print(user)


def say_hello(name:Annotated[str,"je suis une metadat"]) -> str:
    return f"hello {name}"


print(say_hello(int(4)))