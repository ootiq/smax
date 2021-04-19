import pytest

from smax import Smax
from smax.errors import RequestError

# test error handling
def test_error_handling():
    with pytest.raises(RequestError):
        _ = Smax("nonexistentwebsite")