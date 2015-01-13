import requests
from bs4 import BeautifulSoup
import xlwt
data = [["Proposal ID", "Department", "Category", "Total Requested", "Total Funded", "Link"]]
wb = xlwt.Workbook()
ws = wb.add_sheet("Test Sheet")
idx = 0
for numb in ("1","2","3","4","5","6","7","8","9","10","11","12","13"):
  address = "https://techfee.washington.edu/proposals/?page=" + numb
  soup = BeautifulSoup(requests.get(address).content)
  allProps = soup.find_all("td", {"class": "proposal-id"})
  allDepts = soup.find_all("td",{"class": "proposal-department"})
  allCategories = soup.find_all("td", {"class": "proposal-category"})
  for title in soup.find_all("td", {"class": "proposal-title"}):
    prop = allProps[idx].text
    dept = allDepts[idx].text
    category = allCategories[idx].text
    link = "https://techfee.washington.edu" + title.find('a').get("href")
    subSoup = BeautifulSoup(requests.get(link).content)
    status = subSoup.find("table", {"class": "condensed-table no-top-border"}).find('tr').find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling().find("td").text.strip()
    if status == "Partially Funded" or status == "Fully Funded":
        totalRequested = subSoup.find("div", {"class": "well"}).find("h4").text.split(":")[1].strip()
        totalFunded = subSoup.find("div", {"class": "well"}).find("h4").find_next_sibling().text.split(":")[1].strip()
        data.append([prop, dept, category, totalRequested, totalFunded, link])
    idx += 1
for i, row in enumerate(data):
    for j, col in enumerate(data[i]):
        ws.write(i,j,col)
wb.save("proposals.xls")
