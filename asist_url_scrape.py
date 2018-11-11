#use beautiful soup to parse HTML from bs4 module
from bs4 import BeautifulSoup
#requests to navigate pages, json to create files
import requests, time, json, re

page = 1

asist_urls = []

while page <= 300:

    url = "https://asist-jobs.careerwebsite.com/jobs/?str=" + str(page) + "&max=100&vnet=0&long=1"

    job_page = requests.get(url)

    page_html = job_page.text

    all_html = BeautifulSoup(page_html, "html.parser")

    #now can look for certain things within the page (url and title)

    all_listings = all_html.find_all("div", attrs = {"class":"job-summary-top-left clearfix"})

    for a_link in all_listings:

        the_a_link = a_link.find("a")

        the_link = the_a_link["href"]

        if "http" in the_link:

            linkedin_urls = []

            linkedin_urls = the_link

            linkedin_urls.append(the_link)

        if "http" not in the_link:
            the_link = "https://asist-jobs.careerwebsite.com" + the_link

            job_url = []

            job_url = the_link

            asist_urls.append(job_url)

        #print(the_link)

    page = page + 100

    json.dump(asist_urls,open('asist_urls.json','w'), indent=2)

    json.dump(linkedin_urls,open('linkedin_urls.json','w'), indent=2)

    time.sleep(1)
