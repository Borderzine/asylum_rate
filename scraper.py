import requests
from bs4 import BeautifulSoup
import csv
# Get URL
url = "http://trac.syr.edu/immigration/reports/490/include/table2.html"
response = requests.get(url)
html = response.content
# Pass it through beautiful soup
soup = BeautifulSoup(html, "html5lib")
# Find the table of data we're looking for.
table = soup.find('tbody', attrs={'class': None})
# Start scraping the data
list_of_rows = []
for row in table.findAll('tr')[5:]: #skip 5 lines because the header is a bit messy, we can add them in later
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)
# Print into .csv and add proper headers.
outfile = open("./data/trac_judge_asylum_2012_7.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["imm_ct", "judge", "decisions", "per_grants", "per_denials"])
writer.writerows(list_of_rows)
print("FINISHED YO")
