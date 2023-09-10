import requests
import time
import csv
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver

# Configure the Selenium WebDriver (you need to download the appropriate driver for your browser)
driver = webdriver.Chrome()

# Selenium opens webpage
driver.get("https://www.moneycontrol.com/stocks/marketstats/nsehigh/index.php")


# Wait for a few seconds to ensure dynamic content is loaded (you can adjust the delay)
time.sleep(30)

# Get the page source after waiting for dynamic content to load
page_source = driver.page_source

# BeautifulSoup finds the table
soup = BeautifulSoup(page_source, "html.parser")

table = soup.find("table", {"width": "100%"})

# Write the data in <table> element in the 52_Week_High.csv file
with open("52_Week_High.csv", "w", newline="") as f:
    writer = csv.writer(f)
    heading = table.find_all("th")
    heading_rem = heading[-1]
    heading.remove(heading_rem)
    rows = table.find_all("tr")
    writer.writerow([cell.text for cell in heading])

    for row in rows:
        cells = row.find_all("td")
        writer.writerow([cell.text for cell in cells if cell != cells[-1]])


# Below Excel function removes extra part of sentence from each cell in Company Name column
# in 52_Week_High.csv file
# =IFERROR(LEFT(B5,FIND("Add",B5)-1),"")