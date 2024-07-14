import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


class MovieData:
    def __init__(
            self,
            container_idx=None,
            movie_id=None,
            movie_link=None,
            movie_name=None,
            movie_poster_src=None,
            page_url=None,
            details=None,
    ):
        self.container_idx = container_idx
        self.movie_id = movie_id
        self.movie_link = movie_link
        self.movie_name = movie_name
        self.movie_poster_src = movie_poster_src
        self.page_url = page_url
        self.details = details

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4, sort_keys=True)


class MovieDetails:
    def __init__(
            self,
            movie_id=None,
            movie_name=None,
            movie_genres=None,
            movie_rating=None,
            movie_votes=None,
            movie_link_imdb=None,
            movie_link_google=None,
            page_url=None,
    ):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.movie_genres = movie_genres
        self.movie_rating = movie_rating
        self.movie_votes = movie_votes
        self.movie_link_imdb = movie_link_imdb
        self.movie_link_google = movie_link_google
        self.page_url = page_url


class MovieRecommendationData:
    def __init__(
            self,
            movie_id=None,
            page_url=None,
            recommendation_id=None,
            recommendation_link=None,
            recommendation_name=None,
            recommendation_poster_src=None,
    ):
        self.movie_id = movie_id
        self.page_url = page_url
        self.recommendation_id = recommendation_id
        self.recommendation_link = recommendation_link
        self.recommendation_name = recommendation_name
        self.recommendation_poster_src = recommendation_poster_src


def scrape_posters():
    # scrape web page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # get page
    page_url = driver.current_url

    if 'title' in page_url:
        title_query_param = page_url[page_url.find('title=') + 6]
    else:
        title_query_param = None

    # scrape details container (if present)
    details_container = soup.select_one('.content-container .details-container')
    if details_container:
        details = MovieDetails(
            movie_id=title_query_param,
            movie_name=details_container.select_one('.name-container .label').get_text(),
            movie_genres=details_container.select_one('.genres-container .value').get_text(),
            movie_rating=len(details_container.select('.rating-container .value .fill')),
            movie_votes=details_container.select_one('.votes-container .value').get_text(),
            movie_link_imdb=details_container.select('.icon-container a')[0]['href'],
            movie_link_google=details_container.select('.icon-container a')[1]['href'],
            page_url=driver.current_url,
        )
    else:
        details = None

    # scrape movies container
    movies_containers = soup.select('.content-container .movies-container:not(.hidden)')

    data = []
    for idx, container in enumerate(movies_containers):
        for poster in container.select('.poster'):
            data.append(
                MovieData(
                    container_idx=idx,
                    movie_id=poster['id'],
                    movie_link=poster.select_one('a')['href'],
                    movie_name=poster.select_one('.movie-name').get_text(),
                    movie_poster_src=poster.select_one('img')['src'],
                    page_url=driver.current_url,
                    details=details
                ))

    return data


# create driver
driver = webdriver.Chrome()

# load and maximize website
driver.get("https://wheelerrecommends.com/")
driver.maximize_window()

# wait because website is dynamically loaded
time.sleep(5)

# scrape home page
for _ in range(5):
    time.sleep(1)
    view_more_button = driver.find_element(By.CSS_SELECTOR, '.content-container .more-container button')
    view_more_button.click()

results = scrape_posters()

# print(json.dumps(results, default=lambda o: o.__dict__, indent=4, sort_keys=True))
print(len(results))

if len(results) > 0:
    driver.get(results[0].movie_link)
    driver.maximize_window()

    time.sleep(3)

    recommendations = []
    for rec in scrape_posters():
        recommendations.append(
            MovieRecommendationData(
                movie_id=results[0].movie_id,
                page_url=rec.page_url,
                recommendation_id=rec.movie_id,
                recommendation_link=rec.movie_link,
                recommendation_name=rec.movie_name,
                recommendation_poster_src=rec.movie_poster_src
            ))

    print(results[0])
    print(json.dumps(recommendations, default=lambda o: o.__dict__, indent=4, sort_keys=True))

# close driver
driver.quit()
