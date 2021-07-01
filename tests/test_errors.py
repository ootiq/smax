import pytest

from smaxpy import Smax
from smaxpy.errors import RequestError


# test error handling
def test_error_handling():
    with pytest.raises(RequestError):
        _ = Smax("nonexistentwebsite")
