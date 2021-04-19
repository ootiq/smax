from __future__ import annotations

from bs4 import BeautifulSoup
from bs4.element import ResultSet

from .request import cfscrape_wrapper, request_wrapper


class Smax:
    def __init__(
        self, website: str, headers: dict = None, cloudflare: bool = False
    ) -> None:
        self.website = website
        self.__html = (
            request_wrapper(website, headers).text
            if not cloudflare
            else cfscrape_wrapper(website, headers).text
        )
        self._soup = BeautifulSoup(self.__html, "lxml")

    @property
    def title(self) -> str:
        """
        Return the scraped website's title.
        """
        return self._soup.title.get_text()

    @property
    def soup(self) -> BeautifulSoup:
        """
        Return the BeautifulSoup itself.
        """
        return self._soups

    def find_all_links(self, limit: int = None) -> ResultSet:
        """
        Return all links found on the document.
        """
        return self._soup.find_all("a", limit=limit)