# file created by Max Kanter
# followed Andrew Negrut 
"Resources:"
"https://www.youtube.com/watch?v=cta1yCb3vA8&t=20s"
"https://automatetheboringstuff.com/"
"https://www.youtube.com/watch?v=4XQHZIk9gxc"
"in class code"

from bs4 import BeautifulSoup
import requests
import pygame 
import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# Enter location:
# If city is two words, add a dash: 'san-jose'
# Short abbreviation of state: 'ca'
city = input("City:")
state = input("State:")

url = f"https://www.wunderground.com/weather/us/{state}/{city}"
request = requests.get(url)
bs = BeautifulSoup(request.content, features='lxml')
# Find specific high and low temperature
high_temp = bs.find("span", attrs={'class':'hi'}).text
low_temp = bs.find("span", attrs={'class':'lo'}).text
print("HIGH:", high_temp)
print("LOW:", low_temp)

# Initialize pygame
pygame.init()

# Settings for pygame window
WIDTH = 680
HEIGHT = 480
FPS = 30
font = pygame.font.SysFont('TimesNewRoman', 30)
#screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Weather")
#images load
shorts_image = pygame.image.load(os.path.join(game_folder, 'shorts.jpg')).convert()
tshirt_image = pygame.image.load(os.path.join(game_folder, 'tshirt.jpg')).convert()

# Loop to keep the window open
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()  
         
    screen.fill((255, 255, 255))

    # Render weather information as text and display in the center of the screen
    # Display images
    high_text = font.render(f"HIGH: {high_temp}", True, (0, 0, 0))
    low_text = font.render(f"LOW: {low_temp}", True, (0, 0, 0))
    screen.blit(high_text, ((WIDTH - high_text.get_width()) // 2, (HEIGHT - high_text.get_height()) // 5 - 15))
    screen.blit(low_text, ((WIDTH - low_text.get_width()) // 2, (HEIGHT - low_text.get_height()) // 4 + 15))
    screen.blit(shorts_image, (2, 2))
    screen.blit(tshirt_image, (15,250))

    # Update the display
    pygame.display.update()
