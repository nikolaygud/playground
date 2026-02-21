from typing import Protocol

import httpx

from config.config import ConfigApi

config_api = ConfigApi()


class HttpsApiClient(Protocol):
    def __init__(self, **kwargs):
        self.client = httpx.Client(base_url=config_api.app_url, **kwargs)
        self.post_attempts = 0

    def get(self, **kwargs):
        return self.client.get("/user", **kwargs)

    def post(self, **kwargs):
        if self.post_attempts < 3:
            raise RuntimeError("First and second attempts have to be failed")
        self.client.post("/user", **kwargs)

    def put(self, **kwargs):
        self.client.put("/user", **kwargs)

    def delete(self, **kwargs):
        self.client.delete("/user", **kwargs)
