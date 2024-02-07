import math

import classes
from selenium import webdriver
import time
import bs4


# returns a list of current courses being offered with the given category
def search(keyword):
    total_results = get_total_results(keyword)
    total_pages = math.ceil(total_results / 20)

    driver = webdriver.Chrome()

    # list of trips to return
    trips = []

    # For each page of results, and for each result on each page, scrape trip and create a trip object
    for num in range(total_pages):
        page_to_scrape = f'https://www.mountaineers.org/activities/activities#b_start={20 * num}&c4={keyword}'
        driver.get(page_to_scrape)
        time.sleep(3)
        page_source = driver.page_source
        html = bs4.BeautifulSoup(page_source, "html.parser")
        trip_names = html.select(".result-title")
        trip_dates = html.select(".result-date")
        trip_registration_statuses = html.select(".result-reg")
        trip_branches = html.select(".result-branch")
        trip_difficulties = html.select(".result-difficulty")

        for i in range(len(trip_names)):
            name = trip_names[i].text.strip()
            date = trip_dates[i].text.strip()
            registration_status = trip_registration_statuses[i].text.strip()
            branch = trip_branches[i].text.strip()

            try:
                difficulty = trip_difficulties[i].text.strip()
            except IndexError:
                difficulty = "Not listed"

            try:
                link = trip_names[i].find('a')['href']
            except KeyError:
                link = "Webpage coming soon"

            trip = classes.Course(name, link, date, registration_status, branch, difficulty)

            trips.append(trip)

    return trips


# Function that determines how many pages of trips there are to scrape
def get_total_results(keyword):
    first_page_results = f'https://www.mountaineers.org/activities/activities#b_start=0&c4={keyword}'
    driver = webdriver.Chrome()
    driver.get(first_page_results)
    time.sleep(3)
    page_source = driver.page_source
    html = bs4.BeautifulSoup(page_source, "html.parser")
    results = html.select_one("#faceted-result-count").text
    return int(results.strip().split()[0])
