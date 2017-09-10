class Paddle():
    def __init__(self,x,y,width,height,radius):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.radius=radius
    def draw(self):
        fill(255,110,39)
        noStroke()
        rect(self.x,self.y,self.width,self.height,self.radius)

