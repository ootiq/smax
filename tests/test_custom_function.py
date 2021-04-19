import pytest

import requests

from smax import Smax


def customfunction(website: str):
    print(website)  # print the website, this is not included on the default wrappers

    return requests.get(website)


def test_custom_function(capsys):
    _ = Smax("https://example.com", customfunction)

    captured = capsys.readouterr()

    # assert printed output as it is defined from the customfunction
    assert captured.out == "https://example.com\n"
