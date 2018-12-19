# Scraping for Library Jobs
For this project, I used Python to attempt to scrape job listings from three popular professional associations' websites:

1. Society of American Archivists (SAA)
2. American Library Association (ALA)
3. Association for Information Science and Technology (ASIS&T)  

I first scraped the websites for links to detailed job postings and stored the URLs in a JSON file. Then I scraped each detailed job page (with different code to suit each websites' format), and saved this data in a JSON file. I successfully scraped the ASIS&T and ALA websites, but couldn't scrape the SAA website, so my dataset only includes jobs from the last two professional associations.

For this project I used four modules:

1. Requests  (An HTTP library that provides a shortcut for making HTML requests)
2. Beautiful Soup  (Helps with searching and pulling data from websites structured with HTML or XML)
3. JSON  (Used to create and edit .json file types)
4. Time  (Used to add time between executions of the code)
