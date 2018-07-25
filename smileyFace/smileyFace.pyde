def setup():
    size (600,600)
    background(255,255,255)
    smiley_face(255,255,0,275,275)
    
def smiley_face (r,g,b,x,y):
    fill(r,g,b)
    
    #Head
    ellipse(x,y, 400, 400)
    
    #ellipse(250,250, 400, 400)
    
    #mouth
    arc(280,250,300,300,0,PI)
    
    #eyes
    fill(0)
    ellipse(170,150,10,10)
    ellipse(370, 150, 10, 10)
