
class Ball():
    def __init__ (self,x,y,xs,ys,size):
        self.x=x
        self.y=y
        self.xs=xs
        self.ys=ys
        self.size=size
    def draw(self,ballColor):
        fill(ballColor)
        noStroke()
        ellipse(self.x,self.y,self.size,self.size)
    def move(self):
        self.x+=self.xs
        self.y+=self.ys
        
        
