#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718
from RectTab import Rect
from ScoreTab import Score

class Ball:
    def __init__(self, xPos, yPos, xSpeed, ySpeed, radius):
        self.x = xPos
        self.y = yPos
        self.defaultX = xPos
        self.defaultY = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.radius = radius
        self.speedXRandomizer = 0
        self.speedYRandomizer = 0
        self.defaultSpeed = abs(xSpeed)
        
    def display(self):
        fill(255,255,255)
        stroke(0)
        rect(self.x, self.y, self.radius, self.radius)
        
    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed
    
    def checkCollision(self, Rect, Score):
        dx = abs(self.x - Rect.x)
        dy = abs(self.y - Rect.y)   
        if(dx < ((self.radius / 2) + (Rect.xRadius / 2)) and dy < ((self.radius / 2) + (Rect.yRadius / 2))):
            self.xSpeed = -self.xSpeed
                
        if self.y < (0) or self.y > (height - self.radius):
            self.ySpeed = -self.ySpeed
            
        if self.x > (width - self.radius):
            Score.playerScoreID = 1
            Score.score = 1
            Score.updateScore()
            randomSpeed()


            
            self.x = self.defaultX
            self.y = self.defaultY

        if self.x < (0):
            Score.playerScoreID = 2
            Score.score = 1
            Score.updateScore()
            randomSpeed()
            

    
    def randomSpeed():
            self.speedXRandomizer = random(0, 1)
            self.speedYRandomizer = random(0, 1)
            
            if(self.speedXRandomizer < 0.5):
                self.xSpeed = -self.defaultSpeed
            else:
                self.xSpeed = self.defaultSpeed
            if(self.speedYRandomizer < 0.5):
                self.ySpeed = -self.defaultSpeed
            else:
                self.ySpeed = self.defaultSpeed
            
            self.x = self.defaultX
            self.y = self.defaultY
