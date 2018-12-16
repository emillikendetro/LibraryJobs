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

    job_title = all_html.find("h1", attrs = "bti-jd-title")
    #assign variable to text of job title
    position = job_title["title"]

    job_company = all_html.find("h2", attrs = "bti-jd-employer-title")
    company = job_company.text.strip()

    date_posted = all_html.find("div", attrs = "bti-jd-detail-text")
    date = date_posted.text

    job_location = all_html.find("div", attrs = "bti-jd-details-action-container")
    location = job_location.find("span").text

    other_details = all_html.find("div", attrs = "bti-jd-details-other")

    for info in other_details:
        salary = other_details.text
        type_exp = other_details.text
        if type_exp is "Entry Level":
            entry_level = "Yes"
        else:
            entry_level = "No"
        job_func_setting = other_details.text
        edu = other_details.text

    saa_job = {
        "Posted" : date,
        "Location" : location,
        "Entry Level" : entry_level,
        "Company Name" : company,
        "Position Title" : position,
        "Job Function/Setting" : job_func_setting,
        "Job Type/Min Experience" : type_exp,
        "Min Education" : edu,
        "Salary" : salary,
        }
    saa_job_list.append(saa_job)
    #print(saa_job_list)
    json.dump(saa_job_list, open('saa_job_list.json','w'), indent=2)

time.sleep(1)
