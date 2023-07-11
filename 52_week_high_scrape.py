import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.moneycontrol.com/stocks/marketstats/nsehigh/index.php"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.find("table", {"width": "100%"})
heading = table.find_all("th")
rows = table.find_all("tr")

data = []

heading_rem = heading[-1]
heading.remove(heading_rem)
data.append([cell.text for cell in heading])
    
for row in rows:
    #row_rem = row[-1]
    #row.remove(row_rem)
    cells = row.find_all("td")
    #cell_rem = cells[-1]
    #cells.remove(cell_rem)
    data.append([cell.text for cell in cells if cell != cells[-1]])

with open("52_Week_High.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
