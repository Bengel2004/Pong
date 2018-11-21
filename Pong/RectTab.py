#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718

class Rect:
    def __init__(self, xPos, yPos, ySpeed, xRadius, yRadius, playerID):
        self.x = xPos
        self.y = yPos
        self.ySpeed = ySpeed
        self.xRadius = xRadius
        self.yRadius = yRadius
        self.playerID = playerID
        
    def display(self):
        fill(255,255,255)
        stroke(0)
        rect(self.x, self.y, self.xRadius, self.yRadius)
        
