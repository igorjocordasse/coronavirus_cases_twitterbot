import requests
from bs4 import BeautifulSoup

r = requests.get(
    "https://www.worldometers.info/coronavirus/country/mozambique/")
soup = BeautifulSoup(r.text, "html.parser")

content = soup.findAll("div", {"class:", "maincounter-number"})
case = content[0].text.strip()
death = content[1].text.strip()
recovered = content[2].text.strip()

print(case)
print(death)
print(recovered)
