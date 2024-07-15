import argparse
import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from app.classes.HomePage import HomePage
from app.classes.Movie import Movie


def click_view_more(driver: webdriver.Chrome):
    """
    Finds the 'View More' button on the page and clicks it to load more movies.

    Args:
        driver (webdriver): Webdriver instance.
    """

    view_more_button = driver.find_element(By.CSS_SELECTOR, '.content-container .more-container button')
    view_more_button.click()


def scrape(view_more_clicks: int):
    """
    Scrapes the 'wheelerrecommends' home page and returns the results as a HomePage object.

    Args:
        view_more_clicks (int): the number of times to click the 'View More' button.

    Returns:
        HomePage: a HomePage object.
    """

    # create driver
    driver = webdriver.Chrome()

    # load and maximize website
    driver.get('https://wheelerrecommends.com/')
    driver.maximize_window()

    # wait because website is dynamically loaded
    time.sleep(5)

    for _ in range(view_more_clicks):
        time.sleep(1)
        click_view_more(driver)

    # scrape the website
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    posters = soup.select('.content-container .movies-container:not(.hidden) .poster')

    movies = []
    for idx, poster in enumerate(posters):
        movies.append(
            Movie(
                movie_id=poster['id'],
                movie_idx=idx,
                movie_name=poster.select_one('.movie-name').get_text(),
                movie_poster=poster.select_one('img')['src'],
                details_link=poster.select_one('a')['href'],
            ))

    return HomePage(
        page_url=driver.current_url,
        recommendations=movies,
        view_more_clicks=view_more_clicks
    )


if __name__ == '__main__':
    parser = argparse.ArgumentParser('home-page-scraper')
    parser.add_argument(
        '--view_more_clicks',
        default=1,
        help='the number of times to click the "View More" button',
        required=False,
        type=int
    )

    args = parser.parse_args()

    data = scrape(args.view_more_clicks)
    print(json.dumps(data, default=lambda o: o.__dict__, indent=4, sort_keys=True))
