
import argparse
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from classes.HomePage import HomePage
from services.generic_page_scraper import scrape_recommendations
from utilities.csv_utility import write_home_page
from utilities.json_utility import to_json


def click_view_more(driver: webdriver.Chrome) -> None:
    """
    Finds the 'View More' button on the page and clicks it to load more movies.

    Args:
        driver (webdriver): Webdriver instance.
    """

    view_more_button = driver.find_element(By.CSS_SELECTOR, '.content-container .more-container button')
    view_more_button.click()


def scrape(driver: webdriver.Chrome, view_more_clicks: int) -> HomePage:
    """
    Scrapes the 'wheelerrecommends' home page and returns the results as a HomePage object.

    Args:
        driver (webdriver): Chrome webdriver instance.
        view_more_clicks (int): the number of times to click the 'View More' button.

    Returns:
        HomePage: a HomePage object.
    """

    driver.get('https://wheelerrecommends.com/')
    driver.maximize_window()

    time.sleep(5)

    for _ in range(view_more_clicks):
        time.sleep(1)
        click_view_more(driver)

    return HomePage(
        page_url=driver.current_url,
        recommendations=scrape_recommendations(driver.page_source),
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

    data = scrape(webdriver.Chrome(), args.view_more_clicks)

    print(to_json(data))

    write_home_page(data)
