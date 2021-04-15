from __future__ import annotations
import pytest

from smax import Smax


@pytest.fixture()
def smaxx():
    return Smax("https://www.google.com")


def test_get_title(smaxx: Smax):
    a = smaxx.title

    assert a == "Google"


def test_find_all_links(smaxx: Smax):
    a = smaxx.find_all_links(limit=2)

    assert len(a) == 2