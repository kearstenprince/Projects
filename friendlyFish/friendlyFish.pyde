def setup():
    size (600,600)
    background(66, 98, 244)
def draw():
    friendly_fish(66, random(185, 244), random(165,244),300,300)
    friendly_fish(random(135,255), random(0, 33), random(0,33),100,100)
    friendly_fish(random(247,255), random(178, 196), random(0,76),500,500)
    
def friendly_fish (r,g,b,x,y):
    fill(r,g,b)
    #top fin
    triangle(x-100,y-50,  x-100,y-150,   x+100,y-50)
    #bottom fin
    triangle(x-100,y+150,  x-100,y+50,   x+100,y+50)
    #tail fin
    triangle(x-100,y,   x-250,y-100,   x-250,y+70)
    fill(r,g,b)
    #body
    ellipse(x,y,300,150)
    #eye
    fill(0)
    ellipse(x+100,y-20,10,10)
    #mouth
    arc(x+90,y+20,100,2,0,PI)
