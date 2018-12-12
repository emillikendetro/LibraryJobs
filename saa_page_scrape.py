from bs4 import BeautifulSoup
import requests, json, time, re

#import json links file
with open('saa_urls.json', 'r') as data:
    links = json.load(data)

#create list
saa_job_list = []

#loop through links in json file
for url in links:
    #go to url
    job_page = requests.get(url)
    print("Scraping " + url)
    #get html
    page_html = job_page.text
    #bring in beautiful soup to read html
    all_html = BeautifulSoup(page_html, "html.parser")
    #go to job title in html
    job_title = all_html.find_all("h1", attrs = {"class":"bti-jd-title"})
    #go to employer name in html
    job_inst = all_html.find_all("h2", attrs = {"class" : "bti-jd-employer-title"})
    #go to relevant part of html (job detail box)
    #job_detail = all_html.find_all("div", attrs = {"class":"bti-jd-details-container"})
    #loop through each item in the list
    #for catagory in job_detail:
        #find date 'info' in html
        #date_info = catagory.find("bti-jd-detail-text")
        #find 'location' in html
        #location = catagory.find("span")
        #open dictionary that will go in existing list
    saa_job = {"Title" : job_title.text}
        #, "Posted" : date_info.text, "Location" : location.text
    saa_job_list.append(saa_job)

    json.dump(saa_job_list, open('saa_job_list.json','w'), indent=2)

    time.sleep(1)
