from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
while True:
    
 x=400
 while x<800:
    clear_canvas_now()
    grass.draw_now(400, 90)
    character.draw_now(x,140)
    x += 3
    delay(0.01)
 y=140
 while y<600:
    clear_canvas_now()
    grass.draw_now(400, 90)
    character.draw_now(800,y)
    y += 3
    delay(0.01)
 while x>0:
    clear_canvas_now()
    grass.draw_now(400, 90)
    character.draw_now(x,600)
    x -= 3
    delay(0.01)
 while y>140:
    clear_canvas_now()
    grass.draw_now(400, 90)
    character.draw_now(0,y)
    y-= 3
    delay(0.01)
 while x<400:
    clear_canvas_now()
    grass.draw_now(400, 90)
    character.draw_now(x,140)
    x += 3
    delay(0.01)
 for i in range(270, 360+271):
    clear_canvas_now()
    x= 400+235*math.cos(i/360*2*math.pi)
    y= 325+235*math.sin(i/360*2*math.pi)
    grass.draw_now(400, 90)
    character.draw_now(x,y)
    delay(0.01)
    
delay(3)

close_canvas()
