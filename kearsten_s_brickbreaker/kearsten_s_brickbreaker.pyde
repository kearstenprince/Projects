def setup():
    size(1000,1000)
    # global img
    # img = loadImage("KBB.jpg")
    # image(img, 0, 0, 1000, 1000)
    background(255, 173, 220)
    global ellipse_x, speedX, speedY, ellipse_y, block1, block2, block3, block4
    global block5, block6, block7, block8, block9, block10, block11, block12, block13
    global block14, block15, block16, block17, block18, block19, block20
    global block21, block22, block23, block24, block25, block26
    ellipse_x = random(1000)
    ellipse_y = random(300,500)
    speedY = 5
    speedX = 5
    block1 = True
    block2 = True
    block3 = True
    block4 = True
    block5 = True 
    block6 = True 
    block7 = True 
    block8 = True
    block9 = True
    block10 = True
    block11 = True
    block12 = True
    block13 = True
    block14 = True
    block15 = True
    block16 = True
    block17 = True
    block18 = True
    block19 = True
    block20 = True
    block21 = True
    block22 = True
    block23 = True
    block24 = True
    block25 = True
    block26 = True

def draw():
    global ellipse_x,speedX, speedY, ellipse_y, block1, block2, block3, block4
    global block5, block6, block7, block8, block9, block10, block11, block12
    global block13, block14, block15, block16, block17, block18, block19, block20
    global block21, block22, block23, block24, block25, block26
    background(255, 173, 220)
    fill(249, 14, 152)
    textSize(70)
    text ("Kearsten's Brick Breaker", 100,800)
    # global img
    # image(img, 0, 0, 1000, 1000)
#controlling speed of ball
    x = mouseX
    fill(249, 14, 152)
    ellipse(ellipse_x,ellipse_y,10,10)
    ellipse_x = ellipse_x + speedX
    ellipse_y = ellipse_y + speedY
    if ellipse_x >= 1000 or ellipse_x <= 0:
        speedX= -speedX
    if ellipse_y <=0:
        speedY = -speedY
    if ellipse_y >= 1000:
        ellipse_x = random(1000) 
        ellipse_y = random (300,500)
    # if ellipse_x > x:
    #     ellipse_x = 900
    #     ellipse_y = 200
    
#What to do if all blocks have been hit.
    if not (block1 or block2 or block3 or block4 or block5 or block6 or 
                block7 or block8 or block9 or block10 or block11 or 
                block12 or block13 or block14 or block15 or block16 or block17 or
                block18 or block19 or block20 or block21 or block22 or block23 or
                block24 or block25 or block26):
        background (random(255))
        fill(255,255,0)
        textSize(50)
        text ("WINNER", 380,500)
        return

#paddle
    fill(249, 14, 152)
    rect(x,990,100,10)
    if ellipse_x >= x and ellipse_x <= x +100 and ellipse_y >990:
       print "ballhit"
       speedY = -6
    #elif ellipse_y >980:
        #print "miss"
#blocks
    fill(249, 14, 152)
    if block1 == True:
        rect(100,100,100,30)
    fill(0,255,0)
    if block2 == True:
        rect(200,100,100,30)
    fill(249, 14, 152)
    if block3 == True:
        rect(300,100,100,30)
    fill(0,255,0)
    if block4 == True:
        rect(400,100,100,30)
    fill(249, 14, 152)
    if block5 == True:
        rect(500,100,100,30)
    fill(0,255,0)
    if  block6 == True:
        rect(600,100,100,30)
    fill(249, 14, 152)
    if block7 == True: 
        rect(700,100,100,30)
    fill(0,255,0)
    if block8 == True:
        rect(800,100,100,30)
    fill(249, 14, 152)
    if block9 == True:
        rect(100,200,100,30)
    fill(0,255,0)
    if block10 == True:
        rect(200,200,100,30)
    fill(249, 14, 152)
    if block11 == True:
        rect(300,200,100,30)
    fill(0,255,0)
    if block12 == True:
        rect(400,200,100,30)
    fill(249, 14, 152)
    if block13 == True:
        rect(500,200,100,30)
    fill(0,255,0)
    if block14 == True:
        rect(600,200,100,30)
    fill(249, 14, 152)
    if block15 == True:
        rect(700,200,100,30)
    fill(0,255,0)
    if block16 == True:
        rect(800,200,100,30)
    fill(249, 14, 152)
    if block17 == True:
        rect(200,130,100,30)
    fill(0,255,0)
    if block18 == True:
        rect(300,130,100,30)
    fill(249, 14, 152)
    if block19 == True:
        rect(400, 130,100,30)
    fill(0,255,0)
    if block20 == True:
        rect(500,130,100,30)
    fill(249, 14, 152)
    if block21 == True:
        rect(600,130,100,30)
    fill(0,255,0)
    if block22 == True:
        rect(700,130,100,30)
    fill(249, 14, 152)
    if block23 == True:
        rect(300,160,100,30)
    fill(0,255,0)
    if block24 == True:
        rect(400,160, 100,30)
    fill(249, 14, 152)
    if block25 == True:
        rect(500,160,100,30)
    fill(0,255,0)
    if block26 == True:
        rect(600,160,100,30)
#making blocks disappear
    if ellipse_x >= 100 and ellipse_x <=200 and ellipse_y>= 100 and ellipse_y <= 130:
        block1 = False
    if ellipse_x >= 200 and ellipse_x <=300 and ellipse_y>= 100 and ellipse_y <= 130:
        block2 = False
    if ellipse_x >= 300 and ellipse_x <=400 and ellipse_y>= 100 and ellipse_y <= 130:
        block3 = False
    if ellipse_x >= 400 and ellipse_x <=500 and ellipse_y>= 100 and ellipse_y <= 130:
        block4 = False
    if ellipse_x >= 500 and ellipse_x <=600 and ellipse_y>= 100 and ellipse_y <= 130:
        block5 = False
    if ellipse_x >= 600 and ellipse_x <=700 and ellipse_y>= 100 and ellipse_y <= 130:
        block6 = False
    if ellipse_x >= 700 and ellipse_x <=800 and ellipse_y>= 100 and ellipse_y <= 130:
        block7 = False
    if ellipse_x >= 800 and ellipse_x <=900 and ellipse_y>= 100 and ellipse_y <= 130:
        block8 = False
    if ellipse_x >= 100 and ellipse_x <=200 and ellipse_y>= 200 and ellipse_y <= 230:
        block9 = False
    if ellipse_x >= 200 and ellipse_x <=300 and ellipse_y>= 200 and ellipse_y <= 230:
        block10 = False
    if ellipse_x >= 300 and ellipse_x <=400 and ellipse_y>= 200 and ellipse_y <= 230:
        block11 = False
    if ellipse_x >= 400 and ellipse_x <=500 and ellipse_y>= 200 and ellipse_y <= 230:
        block12 = False
    if ellipse_x >= 500 and ellipse_x <=600 and ellipse_y>= 200 and ellipse_y <= 230:
        block13 = False
    if ellipse_x >= 600 and ellipse_x <=700 and ellipse_y>= 200 and ellipse_y <= 230:
        block14 = False
    if ellipse_x >= 700 and ellipse_x <=800 and ellipse_y>= 200 and ellipse_y <= 230:
        block15 = False
    if ellipse_x >= 800 and ellipse_x <=900 and ellipse_y>= 200 and ellipse_y <= 230:
        block16 = False
    if ellipse_x >= 200 and ellipse_x <=300 and ellipse_y>= 130 and ellipse_y <= 160:
        block17 = False
    if ellipse_x >= 300 and ellipse_x <=400 and ellipse_y>= 130 and ellipse_y <= 160:
        block18 = False
    if ellipse_x >= 400 and ellipse_x <=500 and ellipse_y>= 130 and ellipse_y <= 160:
        block19 = False
    if ellipse_x >= 500 and ellipse_x <=600 and ellipse_y>= 130 and ellipse_y <= 160:
        block20 = False
    if ellipse_x >= 600 and ellipse_x <=700 and ellipse_y>= 130 and ellipse_y <= 160:
        block21 = False
    if ellipse_x >= 700 and ellipse_x <=800 and ellipse_y>= 130 and ellipse_y <= 160:
        block22 = False
    if ellipse_x >= 300 and ellipse_x <=400 and ellipse_y>= 160 and ellipse_y <= 190:
        block23 = False
    if ellipse_x >= 400 and ellipse_x <=500 and ellipse_y>= 160 and ellipse_y <= 190:
        block24 = False
    if ellipse_x >= 500 and ellipse_x <=600 and ellipse_y>= 160 and ellipse_y <= 190:
        block25 = False
    if ellipse_x >= 600 and ellipse_x <=700 and ellipse_y>= 160 and ellipse_y <= 190:
        block26 = False
