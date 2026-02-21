from typing import Protocol

from common.clients.base_client import ApiClientProtocol
from retry_strategy import SimpleRetryStrategy


class RetryingClient(Protocol):
    def __init__(self, client: ApiClientProtocol, strategy: SimpleRetryStrategy):
        self._client = client
        self._strategy = strategy
