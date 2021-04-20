import csv
import requests 
from bs4 import BeautifulSoup
for i in range(907):      # Number of pages plus one 
    url = "http://www.pga.com/golf-courses/search?page={}&searchbox=Course+Name&searchbox_zip=ZIP&distance=50&price_range=0&course_type=both&has_events=0".format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.content)

    # Your code for each individual page here 
