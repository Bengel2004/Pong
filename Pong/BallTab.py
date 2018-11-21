#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718

class Ball:
    def __init__(self, xPos, yPos, xSpeed, ySpeed, radius, playerID):
        self.x = xPos
        self.y = yPos
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.radius = radius
        self.playerID = playerID
        
    def display(self):
        fill(255,255,255)
        stroke(0)
        ellipse(self.x, self.y, self.radius, self.radius)
        
    def move(self):
        self.x += self.xSpeed
        self.y += self.ySpeed
    
    def checkCollision(self):
        if self.x < (0 + self.radius / 2) or self.x > (width - self.radius / 2):
            self.xSpeed = -self.xSpeed
        if self.y < (0 + self.radius / 2) or self.y > (height - self.radius / 2):
            self.ySpeed = -self.ySpeed
