import requests
from bs4 import BeautifulSoup
import xlwt
#website = requests.get("https://techfee.washington.edu/proposals/")
DATA = [["Proposal ID", "Department", "Category", "Total Requested", "Total Funded", "Link"]]
wb = xlwt.Workbook()
ws = wb.add_sheet("Test Sheet")
for i, row in enumerate(DATA):      
    for j, col in enumerate(DATA[i]):
         ws.write(i,j, col)
wb.save("testWbk.xls")
#for numb in ("1"): #,"2","3","4","5","6","7","8","9","10","11","12","13"):
   # address = "https://techfee.washington.edu/proposals/?page=" + numb
   # soup = BeautifulSoup(requests.get(address).content)
    # for prop in soup.find_all("td", {"class": "proposal-id"}):
       #  print prop.text
    # for dept in soup.find_all("td", {"class": "proposal-department"}):
       # print dept.text
    # for category in soup.find_all("td", {"class": "proposal-category"}):
       # print category.text
   # for title in soup.find_all("td", {"class": "proposal-title"}):
       # subSoup = BeautifulSoup(requests.get("https://techfee.washington.edu" + title.find('a').get("href")).content)
       # totalRequested = subSoup.find("div", {"class": "well"}).find("h4").text.split(":")[1].strip()
       # print totalRequested
       # status = subSoup.find("table", {"class": "condensed-table no-top-border"}).find('tr').find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find("td").text.strip()
       # if status == "Partially Funded" or status == "Fully Funded":
       #     totalRequested = subSoup.find("div", {"class": "well"}).find("h4").text.split(":")[1].strip()
       #     totalFunded = subSoup.find("div", {"class": "well"}).find("h4").find_next_sibling().text.split(":")[1].strip()
       #     print status
