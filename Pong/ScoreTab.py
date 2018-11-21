#Gemaakt Door Niels Poelder en Luuk Langenhorst
#Klas G&I1C
#Studentnr 3028718

class Score:
    def __init__(self, xPos, yPos):
        self.x = xPos
        self.y = yPos
        self.P1score = 0
        self.P2score = 0
        self.playerScoreID = 0
        self.score = 0
        
    def display(self):
        return(False)
        
    def updateScore(self):
        if self.playerScoreID == 1:
            self.P1score += self.score
        elif self.playerScoreID == 2:
            self.P2score += self.score
        print(str(self.P1score) + " Player1Score   " + str(self.P2score) + " Player2Score")
            
        
    
    
