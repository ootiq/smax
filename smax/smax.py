from bs4 import BeautifulSoup

from .request import request_wrapper


class Smax:
    def __init__(self, website: str) -> None:
        self.website = website
        self.__html = request_wrapper(website).text
        self._soup = BeautifulSoup(self.__html, "lxml")

    @property
    def title(self) -> str:
        """
        Return the scrape'd website's title
        """
        return self._soup.title.get_text()