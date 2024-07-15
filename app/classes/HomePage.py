import json


class HomePage:
    """
    An object that contains data found on the Home page.
    """

    def __init__(
            self,
            page_url=None,
            recommendations=None,
            view_more_clicks=None,
    ):
        """
        Creates a HomePage object.

        Args:
            page_url (str): the url of the page.
            recommendations (Movie[]): a Movie[] object.
            view_more_clicks (int): the number of times to click the 'View More' button.

        Returns:
            HomePage: a HomePage object.
        """

        self.page_url = page_url
        self.recommendations = recommendations
        self.view_more_clicks = view_more_clicks

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)
