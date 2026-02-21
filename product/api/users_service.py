from common.clients.base_client import ApiClientProtocol


class UsersService:
    def __init__(self, client: ApiClientProtocol):
        self.client = client

    def create_user(self):
        return self.client.post(body={"first_name": "name", "last_name": "surname"})
