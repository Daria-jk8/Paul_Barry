# p 583 -> Tk interface - library turtle

from turtle import *

color('green', 'orange')
begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break

end_fill()
done()    