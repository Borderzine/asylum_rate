import requests
from bs4 import BeautifulSoup
import csv

url = "http://trac.syr.edu/immigration/reports/490/include/table2.html"
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html5lib")
table = soup.find('tbody', attrs={'class': None})

list_of_rows = []
for row in table.findAll('tr')[5:]:
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./data/trac_judge_asylum_2012_7.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["imm_ct", "judge", "decisions", "per_grants", "per_denials"])
writer.writerows(list_of_rows)
print("FINISHED YO")
