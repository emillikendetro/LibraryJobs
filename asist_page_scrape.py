from bs4 import BeautifulSoup
import requests, json, time

#import json links file
with open('asist_urls.json', 'r') as data:
    links = json.load(data)

#create list
asist_job_list = []

#loop through links in json file
for url in links:
    #go to url
    job_page = requests.get(url)
    print("Scraping " + url)
    #get html
    page_html = job_page.text
    #bring in beautiful soup to read html
    all_html = BeautifulSoup(page_html, "html.parser")
    #go to relevant part of html (job detail box)
    job_detail = all_html.find_all("li", attrs = {"class":"clearfix"})

    #open dictionary that will go in existing list (asist_job_list)
    asist_job = {}
    #loop through each item in the list
    for catagory in job_detail:
        #find 'label' in html
        label = catagory.find("label")

        #find 'span' in html
        info = catagory.find("span")
        #organize label and info into dictionary

        asist_job[label.text.strip(": ")] = info.text.strip()

    #add finished dictionary entries (asist_job) to list (asist_job_links)
    if asist_job not in asist_job_list:
        asist_job_list.append(asist_job)
    json.dump(asist_job_list, open('asist_job_list.json','w'), indent=2)

    time.sleep(1)
