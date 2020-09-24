from sense_hat import SenseHat
import time

sense = SenseHat()

blue = (0, 0, 255)
green = (0, 255, 0)

def show_Y():
  sense.show_letter("Y", back_colour = blue)

def show_L():
  sense.show_letter("L", back_colour = green)


####
# Intro Animation
####

show_Y()
current_letter = "Y"

####
# Main loop
####

while True:
  events = sense.stick.get_events()
  for event in events:
    # Skip releases
    if event.action != "released":
      if current_letter == "Y":
        show_L()
        current_letter = "L"
      else:
        show_Y()
        current_letter = "Y"
  