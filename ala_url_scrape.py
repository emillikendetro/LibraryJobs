#use beautiful soup to parse HTML from bs4 module
from bs4 import BeautifulSoup
#requests to navigate pages, json to create files
import requests, time, json

page = 1

ala_urls = []

while page <= 300:

    url = "https://joblist.ala.org/jobs/?str=" + str(page) + "&max=100&long=1&vnet=0"

    job_page = requests.get(url)

    page_html = job_page.text

    all_html = BeautifulSoup(page_html, "html.parser")

    #now can look for certain things within the page (url and title)

    all_listings = all_html.find_all("div", attrs = {"class":"job-summary-top-left clearfix"})

    for a_link in all_listings:

        the_a_link = a_link.find("a")

        #the_title = the_a_link.text

        the_link = the_a_link["href"]

        the_link = "https://joblist.ala.org" + the_link

        job_url = []

        job_url = the_link

        ala_urls.append(job_url)
        #print(the_link)

    page = page + 100

    json.dump(ala_urls,open('ala_urls.json','w'), indent=2)

    time.sleep(1)
