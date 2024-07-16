
import json

from services.home_page_scraper import scrape as scrape_home_page
from services.movie_details_page_scraper import scrape as scrape_movie_details_page


def main(event, context):

    movie_id = event['movie_id'] if 'movie_id' in event else 'tt1431045'

    page = event['page'] if 'page' in event else 'home'

    view_more_clicks = event['view_more_clicks'] if 'view_more_clicks' in event else 1

    if page == 'home':
        print(f"scrape_home_page --view_more_clicks '{view_more_clicks}'")
        data = scrape_home_page(view_more_clicks)

    elif page == 'movie_details':
        print(f"scrape_movie_details_page {movie_id}")
        data = scrape_movie_details_page(movie_id)

    else:
        print(f"page '{page}' is invalid")
        data = {}

    print(json.dumps(data, default=lambda o: o.__dict__, indent=4, sort_keys=True))


if __name__ == '__main__':
    main({}, None)
