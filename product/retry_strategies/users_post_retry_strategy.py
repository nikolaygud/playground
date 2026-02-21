from typing import Protocol, Any


class UsersPostRetryStrategy(Protocol):

    def __init__(
        self,
        max_attempts: int,
        retryable_statuses: set[int],
        base_delay: float = 0.5,
    ):
        self._max_attempts = max_attempts
        self._retryable_statuses = retryable_statuses
        self._base_delay = base_delay

    def should_retry(self, attempt, response, error):
        if attempt >= self._max_attempts:
            return False

        if error:
            return True

        if response and response.status_code in self._retryable_statuses:
            return True

        return False

    def get_delay(self, attempt):  # где этот delay используется?
        return self._base_delay * (2 ** (attempt - 1))