from bs4 import BeautifulSoup
import requests, json, time, re

#import json links file
with open('ala_urls.json', 'r') as data:
    links = json.load(data)

#create list
ala_job_list = []

#loop through links in json file
for url in links:
    #go to url
    job_page = requests.get(url)
    # print("Scraping " + url)
    #get html
    page_html = job_page.text
    #bring in beautiful soup to read html
    all_html = BeautifulSoup(page_html, "html.parser")
    #go to relevant part of html (job detail box)
    job_detail = all_html.find_all("li", attrs = {"class":"clearfix"})

    #open dictionary that will go in existing list (ala_job_list)
    ala_job = {}
    #loop through each item in the list
    for catagory in job_detail:

        #find 'label' in html
        label = catagory.find("label")
        #find 'span' in html
        info = catagory.find("span")
        #use label and info to create dictionary content
        ala_job[label.text.strip(": ")] = info.text.strip()
    #only add job listing to json file if it isn't already there
    if ala_job not in ala_job_list:
        ala_job_list.append(ala_job)

    json.dump(ala_job_list, open('ala_job_list.json','w'), indent=2)


time.sleep(1)
