# file created by Max Kanter
# create code that takes local weather and gives clothing advice
# uses zip code
#"I installed bs4 and requests"

import webbrowser
import os   
import requests
from bs4 import BeautifulSoup


print("Hello there, please input a valid zipcode of your choosing:")
zip_code = input("Enter your zip code: ")

# checks for exactly 5 digits
if len(zip_code) != 5 or not zip_code.isdigit():
    print("Invalid zip code. Please enter a valid 5-digit zip code.")
else:
    # Construct the URL for the zip code's weather forecast page
    url = f"https://www.weather.gov/{zip_code}"
    response = requests.get(url)
    # Use BeautifulSoup to parse the HTML content of the page
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the section of the page containing the weather data
    weather_section = soup.find(id="seven-day-forecast")

    # Extract the weather forecast for the next 7 days
    days = weather_section.select(".tombstone-container .period-name")
    short_descs = weather_section.select(".tombstone-container .short-desc")
    temps = weather_section.select(".tombstone-container .temp")

    # Print the weather forecast for each of the next 7 days
    for i in range(7):
        day = days[i].get_text()
        short_desc = short_descs[i].get_text()
        temp = temps[i].get_text()

        print(f"{day}: {short_desc}, {temp}")