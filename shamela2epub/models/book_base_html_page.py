from bs4 import BeautifulSoup, Tag
from http import get_url_text  # Import the get_url_text function from http.py

class BookBaseHTMLPage:
    BOOK_PAGE_CONTENT_SELECTOR = "div.nass"

    def __init__(self, url: str):
        """Base class for HTML pages."""
        self.url = url
        self._html_text: str = get_url_text(self.url)  # Fetch HTML content using get_url_text
        self._html: BeautifulSoup = BeautifulSoup(self._html_text, "html.parser")
        self.content: Tag = self._html.select_one(self.BOOK_PAGE_CONTENT_SELECTOR)
