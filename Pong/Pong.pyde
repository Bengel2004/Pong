#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718
from BallTab import Ball
from RectTab import Rect
from ScoreTab import Score

frameXSize = 800
frameYSize = 600

xSpeedDefiner = random(0, 5)
ySpeedDefiner = random(0, 15)

xSpeed = -4
ySpeed = 0

rectYSpeed = 5
rectWidth = 33
rectHeight = 100

ballRadius = 33

Player1 = Rect((frameXSize / 6), (frameYSize/2), rectYSpeed, rectWidth, rectHeight, 1)
Player2 = Rect((frameXSize - (frameXSize / 6)), (frameYSize/2), rectYSpeed, rectWidth, rectHeight, 1)
usedBall = Ball((frameXSize / 2), (frameYSize / 2), xSpeed, ySpeed, ballRadius)
thisScore = Score((frameXSize / 2), 100)

#Vergeet niet de speed goed te randomizen en niet dat het 2 bij 6 word maar gewoon 6 bij 6 bijv 4 is optimale speed. bij 4x collide verander speed x 1.5?
#Fix de collision aan de linker kant op de x pos
#Fix de y pos collision aan de onderkant


Playerlist = []

def setup():
    size(frameXSize, frameYSize)
    frameRate(60)
    Playerlist.append(Player1)
    Playerlist.append(Player2)
    
    
def draw():
    background(0)
    thisScore.display()
    for item in range(0, len(Playerlist)):
        Playerlist[item].display()
        usedBall.display()
        usedBall.move()
        usedBall.checkCollision(Playerlist[item], thisScore)
        
        
    if keyPressed:
        if key == CODED: #Player 2
            if keyCode == UP:
                Playerlist[1].y += Playerlist[1].ySpeed
            elif keyCode == DOWN:
                Playerlist[1].y -= Playerlist[1].ySpeed
        else: #Player 1
            if key == 'w':
                Playerlist[0].y += Playerlist[0].ySpeed
            elif key == 's':
                Playerlist[0].y -= Playerlist[0].ySpeed
