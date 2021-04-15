from __future__ import annotations
import pytest

from smax import Smax


@pytest.fixture()
def smaxx():
    return Smax("https://www.google.com")


def test_get_title(smaxx: Smax):
    a = smaxx.title

    assert a == "Google"