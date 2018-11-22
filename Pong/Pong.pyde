#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718
from BallTab import Ball
from RectTab import Rect
from ScoreTab import Score

frameXSize = 1920
frameYSize = 1080

xSpeedDefiner = random(0, 1)
ySpeedDefiner = random(0, 1)

defaultBallSpeed = 4

if(xSpeedDefiner < 0.5):
    xSpeed = -defaultBallSpeed
else:
    xSpeed = defaultBallSpeed
if(ySpeedDefiner < 0.5):
    ySpeed = -defaultBallSpeed
else:
    ySpeed = defaultBallSpeed

playerSpeed = 20
rectWidth = 32
rectHeight = 100

ballRadius = 32

Player1 = Rect((frameXSize / 4), (frameYSize/2), playerSpeed, rectWidth, rectHeight, 1)
Player2 = Rect((frameXSize - (frameXSize / 4)), (frameYSize/2), playerSpeed, rectWidth, rectHeight, 2)
usedBall = Ball((frameXSize / 2), (frameYSize / 2), xSpeed, ySpeed, ballRadius)
thisScore = Score((frameXSize / 2), 100)

Playerlist = []

def setup():
    fullScreen()
    size(frameXSize, frameYSize)
    frameRate(60)
    Playerlist.append(Player1)
    Playerlist.append(Player2)
    
    
def draw():
    textSize(62)
    textAlign(CENTER)
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
                if Playerlist[1].y > 0: 
                    Playerlist[1].y -= Playerlist[1].ySpeed
            elif keyCode == DOWN:
                if Playerlist[1].y < (height - Playerlist[1].yRadius):
                    Playerlist[1].y += Playerlist[1].ySpeed
    if keyPressed:
        if key == 'w':
            if Playerlist[0].y > 0: 
                Playerlist[0].y -= Playerlist[0].ySpeed
        elif key == 's':
            if Playerlist[0].y < (height - Playerlist[0].yRadius):
                Playerlist[0].y += Playerlist[0].ySpeed
