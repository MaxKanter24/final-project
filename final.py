# file created by Max Kanter
# followed Andrew Negrut 

from bs4 import BeautifulSoup
import requests
import pygame

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

#initialises pygame
pygame.init()

screen_width, screen_height = 680, 480
font = pygame.font.SysFont('TimesNewRoman', 30)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Weather")
# Loop to keep the window open
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  
            
    screen.fill((255, 255, 255))

    # Render weather information as text and display in the center of the screen
    high_text = font.render(f"HIGH: {high_temp}", True, (0, 0, 0))
    low_text = font.render(f"LOW: {low_temp}", True, (0, 0, 0))
    screen.blit(high_text, ((screen_width - high_text.get_width()) // 2, (screen_height - high_text.get_height()) // 2 - 50))
    screen.blit(low_text, ((screen_width - low_text.get_width()) // 2, (screen_height - low_text.get_height()) // 2 + 50))

    # Update the display
    pygame.display.update()
