from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

while True:
  sense.set_pixel(0, 0, randint(60,200), randint(60,200), randint(60,200))
  sense.set_pixel(0, 7, randint(60,200), randint(60,200), randint(60,200))
  sense.set_pixel(7, 0, randint(60,200), randint(60,200), randint(60,200))
  sense.set_pixel(7, 7, randint(60,200), randint(60,200), randint(60,200))
  sleep(0.01)

