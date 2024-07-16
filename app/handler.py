import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from tempfile import mkdtemp

from services.home_page_scraper import scrape as scrape_home_page
from services.movie_details_page_scraper import scrape as scrape_movie_details_page


def initialize_headless_driver():
    """
    Creates a headless Chrome webdriver instance.

    Returns:
        webdriver: Chrome webdriver instance.
    """

    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument("--single-process")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-pipe")
    options.add_argument("--verbose")
    options.add_argument("--log-path=/tmp")
    options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    service = ChromeService(
        executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
        service_log_path="/tmp/chromedriver.log"
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )
    
    return driver


def main(event, context):
    driver = initialize_headless_driver()

    movie_id = event['movie_id'] if 'movie_id' in event else 'tt1431045'

    page = event['page'] if 'page' in event else 'home'

    view_more_clicks = event['view_more_clicks'] if 'view_more_clicks' in event else 1

    if page == 'home':
        print(f"scrape_home_page --view_more_clicks '{view_more_clicks}'")
        data = scrape_home_page(driver, view_more_clicks)

    elif page == 'movie_details':
        print(f"scrape_movie_details_page {movie_id}")
        data = scrape_movie_details_page(driver, movie_id)

    else:
        print(f"page '{page}' is invalid")
        data = {}

    print(json.dumps(data, default=lambda o: o.__dict__, indent=4, sort_keys=True))
