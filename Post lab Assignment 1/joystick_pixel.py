
from se
nse_hat import SenseHat
from time import sleep

sense=SenseHat()
sense.clear()
c = (239, 79, 121)
blank = (0,0,0)
x = 3
y = 5
sense.set_pixel(x, y, c)
while True:
    for event in sense.stick.get_events():

        sense.set_pixel(x, y, blank)
        if event.action == 'pressed' and event.direction == 'up':
            if y > 0:
                y -= 1
        if event.action == 'pressed' and event.direction == 'down':
            if y < 7:
                y += 1
        if event.action == 'pressed' and event.direction == 'right':
            if x < 7:
                x += 1
        if event.action == 'pressed' and event.direction == 'left':
            if x > 0:
                x -= 1
        if event.action == 'pressed' and event.direction == 'middle':
            sense.clear()
            exit()
         
        sense.set_pixel(x, y, c)

            
            
