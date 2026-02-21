from typing import Protocol, Any


class BaseRetryStrategy(Protocol):

    def should_retry(self, attempt: int, response: Any | None, error: Exception | None) -> bool:
        ...

    def get_delay(self, attempt: int) -> float:
        ...
