
class PowerUP():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    
    def draw(self):
        
        noStroke()
        fill(40,229,245)
        ellipse(self.x,self.y,50,50)
        textAlign(CENTER,CENTER)
        fill(20,145,216)
        textSize(54)
        text("P",self.x+5,self.y)

    
