#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718
from RectTab import Rect
from ScoreTab import Score

class Ball:
    def __init__(self, xPos, yPos, xSpeed, ySpeed, radius):
        self.x = xPos
        self.y = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.radius = radius
        
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
            if dx > dy:
                self.xSpeed = -self.xSpeed
            else:
                self.ySpeed = -self.ySpeed
                
        if self.y < (0 + self.radius / 2) or self.y > (height - self.radius / 2):
            self.ySpeed = -self.ySpeed
            
        if self.x < (0 + self.radius / 2):
            Score.playerScoreID = 1
            Score.score = 1
            Score.updateScore()
        if self.x > (width - self.radius / 2):
            Score.playerScoreID = 2
            Score.score = 1
            Score.updateScore()
            
