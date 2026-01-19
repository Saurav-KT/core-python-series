from dataclasses import dataclass
import json
from fastapi.encoders import jsonable_encoder


@dataclass
class Person:
    id: int
    name: str
    contact: str
    email: str
    gender: str
    nationality: str
    address: str
    profession: str


obj = Person(id=1, name="saurav",
             contact="9731099682", email="saurav@gmail.com", gender="M", nationality="indian", address="HYD",
             profession="tech")

obj1 = Person(id=1, name="saurav",
              contact="9731099682", email="saurav@gmail.com", gender="M", nationality="indian", address="HYD",
              profession="tech")

print(obj == obj1)

addr = {"name": "saurav", "contact": "3473477", "address": "BLR"}
print(type(json.dumps(addr)))
