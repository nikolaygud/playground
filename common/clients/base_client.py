from typing import Protocol

from config.config import ConfigApi

config_api = ConfigApi


class BaseClient(Protocol):
    post_attempts: int

    def post(self, **kwargs):
        pass

    def put(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass

    def get(self, **kwargs):
        pass
