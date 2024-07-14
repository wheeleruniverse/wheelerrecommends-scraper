import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class ScrapeResult:
    def __init__(self, container_idx=None, movie_id=None, movie_name=None, page_url=None, poster_src=None):
        self.container_idx = container_idx
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.page_url = page_url
        self.poster_src = poster_src

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)


# create driver
driver = webdriver.Chrome()

# load and maximize website
driver.get("https://wheelerrecommends.com/")
driver.maximize_window()

# wait because website is dynamically loaded
time.sleep(5)

for _ in range(5):
    time.sleep(1)
    view_more_button = driver.find_element(By.CSS_SELECTOR, '.content-container .more-container button')
    view_more_button.click()

# scrape website
soup = BeautifulSoup(driver.page_source, 'html.parser')

# scrape movies container
movies_containers = soup.select('.content-container .movies-container:not(.hidden)')

results = []
for idx, container in enumerate(movies_containers):
    for poster in container.select('.poster'):
        results.append(
            ScrapeResult(
                container_idx=idx,
                movie_id=poster['id'],
                movie_name=poster.select_one('.movie-name').get_text(),
                page_url=driver.current_url,
                poster_src=poster.select_one('img')['src']
            ))

print(json.dumps(results, default=lambda o: o.__dict__, indent=4, sort_keys=True))
print(len(results))

# close driver
driver.quit()
