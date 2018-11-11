from bs4 import BeautifulSoup

import requests, time, json

saa_urls = []

url = "http://careers.archivists.org/jobs/"

job_page = requests.get(url)

page_html = job_page.text

all_html = BeautifulSoup(page_html, "html.parser")

all_listings = all_html.find_all("div", attrs = {"class":"bti-ui-job-result-detail-title"})

for a_link in all_listings:

    the_a_link = a_link.find("a")

    the_link = the_a_link["href"]

    the_link = "http://careers.archivists.org" + the_link

    job_url = []

    job_url = the_link

    saa_urls.append(job_url)

json.dump(saa_urls,open('saa_urls.json','w'), indent=2)

time.sleep(1)
