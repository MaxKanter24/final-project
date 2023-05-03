# file created by Max Kanter
# followed Andrew Negrut 

from bs4 import BeautifulSoup
import requests

city = input("City:")
state = input("State:")

# if city is two words, add dash: san-jose
# short abreviation of state: ca
url = f"https://www.wunderground.com/weather/us/{state}/{city}"

request = requests.get(url)

bs = BeautifulSoup(request.content, features= 'lxml')

high_temp = bs.find("span", attrs={'class':'hi'}).text
low_temp = bs.find("span", attrs={'class':'lo'}).text

print("HIGH:", high_temp)
print("LOW:", low_temp)
