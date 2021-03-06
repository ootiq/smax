from __future__ import annotations
from typing import Optional

import requests
import cloudscraper


from .errors import RequestError


def request_wrapper(website: str, headers: Optional[dict]) -> str:
    """
    Just a simple wrapper for the `requests` module.
    """
    try:
        r = requests.get(website, headers=headers)
    except Exception:
        raise RequestError(
            "There was a problem with your request, please try again later."
        )

    return r.text


def cfscrape_wrapper(website: str, headers: Optional[dict]) -> str:
    """
    Just a simple wrapper for the `cloudscraper` module.
    """

    # TODO: better implementation
    # , allow_brotli: bool = True

    scraper = cloudscraper.create_scraper()

    try:
        r = scraper.get(website, headers=headers)

    except Exception:
        raise RequestError(
            "There was a problem with your request, please try again later."
        )

    return r.text  # type: ignore
