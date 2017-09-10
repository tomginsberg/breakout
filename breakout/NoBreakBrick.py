class NoBreakBrick():
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
    def draw(self):
        fill(172,195,201)
    
        ellipse(self.x,self.y,self.size,self.size)
