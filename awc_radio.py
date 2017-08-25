# Author: Tang Yew Seng
# School: Dunman High School
# Email: tang.yewseng@dhs.sg

from microbit import *
import radio

radio.on()

while True:
    if button_a.was_pressed():
        radio.send('reset')
