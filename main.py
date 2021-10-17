from bs4.element import TemplateString
from bs4 import BeautifulSoup
import requests

import time
import csv
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = requests.get(url)
print(browser)

def Scrape():
    Headers = ["Name", "Distance", "Mass" "Radius"]

    Soup = BeautifulSoup(browser.text, "html.parser")
    
    Table = Soup.find("table")
    TableRows = Table.find_all("tr")

    tempList = []

    data = []

    for trTags in TableRows:
        tdTags = trTags.find_all("td")
        
        row = [i.text.rstrip() for i in tdTags]
        tempList.append(row)

        Name = []
        Distance = []
        Mass = []
        Radius = []
        
        for i in range(1, len(tempList)):
            Name.append(tempList[i][1])
            Distance.append(tempList[i][3])
            Mass.append(tempList[i][5])
            Radius.append(tempList[i][6])
    
    df2 = pd.DataFrame(list(zip(Name, Distance, Mass, Radius)), columns=["Name", "Distance", "Mass", "Radiuss"])
    print(df2)
    df2.to_csv("Output.csv")

Scrape()