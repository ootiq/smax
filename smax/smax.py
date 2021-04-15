from bs4 import BeautifulSoup
from bs4.element import ResultSet

from .request import request_wrapper


class Smax:
    def __init__(self, website: str) -> None:
        self.website = website
        self.__html = request_wrapper(website).text
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
        return self._soup

    def find_all_links(self, limit=None | int) -> ResultSet:
        """
        Return all links found on the document.
        """
        return self._soup.find_all("a", limit=limit)