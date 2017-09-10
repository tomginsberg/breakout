class Brick():
    def __init__(self,x,y,size):
        self.x=x
        self.y=y
        self.size=size
    def draw(self):
        ellipse(self.x,self.y,self.size,self.size)
