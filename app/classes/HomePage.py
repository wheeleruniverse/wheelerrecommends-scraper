
import datetime

from typing import List

from classes.Movie import Movie
from utilities.json_utility import to_json


class HomePage:
    """
    An object that contains data found on the Home page.
    """

    def __init__(
            self,
            page_url: str,
            recommendations: List[Movie],
            view_more_clicks: int,
    ):
        """
        Creates a HomePage object.

        Args:
            page_url (str): the url of the page.
            recommendations (List[Movie]): a List[Movie] object.
            view_more_clicks (int): the number of times to click the 'View More' button.

        Returns:
            HomePage: a HomePage object.
        """

        self.datetime = datetime.datetime.now()
        self.page_url = page_url
        self.recommendations = recommendations
        self.view_more_clicks = view_more_clicks

    def __str__(self) -> str:
        """
        Returns:
            str: a JSON string representation of the HomePage object.
        """
        return to_json(self)
