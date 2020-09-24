from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

while True:
  sense.set_pixel(randint(0,7), randint(0,7), randint(60,200), randint(60,200), randint(60,200))
  sleep(0.01)
