import json
import pathlib
import random
import uuid
from typing import List

from faker import Faker
from pydantic import parse_file_as

from app.models.user import User
from app.patterns.singleton import Singleton


class JsonDBRepository(metaclass=Singleton):
    _users: List[User]

    def __init__(self):
        self.json_file_path = "app/repository/users.json"
        self.fetch_data_from_json_file()

    # section Get all
    def get_all_users(self) -> List[User]:
        return self._users

    # section Create
    def create_user(self, user: User) -> User:
        self._users.append(user)
        self.save_all_users_to_file()
        return user

    def fetch_data_from_json_file(self) -> List[User]:
        self._users = parse_file_as(List[User], self.json_file_path)
        return self._users

    def save_all_users_to_file(self):
        f = open(self.json_file_path, "w")
        json_string = json.dumps([user.dict() for user in self._users])
        f.write(json_string)
        f.close()

    def generate_fake_users(self, number: int = 5):
        fake = Faker()

        self._users = []
        for _ in range(number):
            self._users.append(
                User.parse_obj({
                    "full_name": {
                        "first_name": fake.first_name(),
                        "last_name": fake.last_name(),
                    },
                    "age": random.randint(10, 20),
                    "id": str(uuid.uuid4()),
                    "address": fake.address(),
                })
            )
