from Paddle import Paddle
from Ball import Ball
from Brick import Brick
from powerUP import PowerUP
from NoBreakBrick import NoBreakBrick

paddleWidth=120
bx=0
by=0
bxs=0
bys=0
bSize=20
moving=False
bricks=[]
noBreakBricks=[]
gameStarted=False
lives=5
lifeTimer=0
level=1
infoTimer=0
hitCounter=0
power=0
powerSpawn=42
ps=1
ballColor=color(50,50,50)
powerOn=False
py=random(150,350)
px=random(100,900)


def setup():
    global wallpaper,bricks, startScreen,f
    wallpaper=loadImage("background.jpg")
    startScreen=loadImage("start.png")
    f=loadFont("Trench-Thin-200.vlw")

    size(1051,591)
    Level(level)
    
def Level(level):
    if level==2:
        for i in range (5,12):
            
            bricks.append(Brick(40+i*60,150,random(20,40)))
            bricks.append(Brick(40+i*60,450,random(20,40)))
        for k in range (5,9):
            bricks.append(Brick(340,-100+k*60,random(20,40)))
            bricks.append(Brick(700,-100+k*60,random(20,40)))
        bricks.append(Brick(width/2,height/2,250))
    
    if level==3:
        for i in range (5,12):
            noBreakBricks.append(NoBreakBrick(40+i*60,150,30))
            noBreakBricks.append(NoBreakBrick(40+i*60,450,30))
        for k in range (5,9):
            noBreakBricks.append(NoBreakBrick(340,-100+k*60,30))
            noBreakBricks.append(NoBreakBrick(700,-100+k*60,30))
        for i in range(0,8):
            for k in range(0,7):
                bricks.append(Brick(380+i*40,180+k*40,random(20,40)))
            
    if level==1:    
        for i in range (5,12):
            for k in range (0,2):
                bricks.append(Brick(40+i*60,250+(40*sin(20*i))+k*40,random(20,40)))
    if level==4:    
        for i in range (-3,17):
            for k in range (-5,8):
                bricks.append(Brick(40+i*60,250+(40*sin(20*i))+k*40,random(10,50)))
    

def draw():
    print(level)
    global gameStarted,lives,lifeTimer,level,infoTimer,power
    
    image(wallpaper,0,0)

    paddle()
    ball()
    brick()
    powers(power)
    getPower()
    nextLevel()
    playing()
    
    if level>4:
        textAlign(CENTER,CENTER)
        textSize(100)
        text("Wow, nice",width/2,height/2)
        infoTimer=1000

    
    
    
def paddle():
    global paddleWidth,moving, b1,bx,by,bxs,bys,bSize,bricks,p1,p2
    p1=Paddle(mouseX-paddleWidth/2,551,paddleWidth,20,10)
    if power==2:
        p2x=(width-mouseX)-paddleWidth/2
    else:
        p2x=mouseX-paddleWidth/2
    p2=Paddle(p2x,20,paddleWidth,20,10)
    p2.draw()
    p1.draw()


def ball():
    global paddleWidth,moving, b1,bx,by,bxs,bys,bSize,bricks,lives,lifeTimer,p1,p2,ballColor
    b1=Ball(bx,by,bxs,bys,bSize)
    b1.draw(ballColor)
    if power==4:
        ballColor=color(245,173,40)
    else:
        ballColor=color(50,50,50)
    tx=500-(500-mouseX)*2
    
    if gameStarted==True:
        if mousePressed and mouseButton==LEFT and moving==False and mouseY<550:
            moving=True
            bxs=(mouseX-tx)/-50
            bys=(540-mouseY)/-50
            
    if moving==True:
        b1.move()
        bx+=bxs
        by+=bys
        if bx-bSize/2<0:
            bxs*=-1
            bys+=(random(-0.2,0.2))
        if bx+bSize/2>1051:
            bxs*=-1
            bys+=(random(-0.2,0.2))
    
        if by<550+bSize/2 and by>550-bSize/2 and bx+bSize/2>p1.x and bx-bSize/2<p1.x+paddleWidth:   
            bxs=(((p1.x+paddleWidth/2)-bx)*-1)/5
            bys*=-1
        if by>40-bSize/2 and by<40+bSize/2 and bx+bSize/2>p2.x and bx-bSize/2<p2.x+paddleWidth:
            bxs=(((p2.x+paddleWidth/2)-bx)*-1)/5
            bys*=-1
        
        if by<-bSize/2 or by>591+bSize/2:
            moving=False
            lifeTimer=0
            lives-=1
    if moving==False:
        bx=mouseX
        by=550-bSize/2
    if moving==False and mouseY<520:
        noFill()
        stroke(0)
        line(tx-5,mouseY,tx+5,mouseY)
        line(tx,mouseY-5,tx,mouseY+5)
        ellipse(tx,mouseY,10,10)
    
def brick():
    global paddleWidth,moving, b1,bx,by,bxs,bys,bSize,bricks,hitCounter,noBreakBricks
    for Brick in bricks:

        
        if Brick.size<35:
            fill(50,50,50)
            
        if Brick.size>=35:
            fill(255,0,0)
        
        if moving==False:
            noFill()
        Brick.draw()
        if dist(Brick.x,Brick.y,bx,by)<((Brick.size/2)+(bSize/2)) and Brick.size<35:
            Brick.x=-10000
            Brick.y=-10000
            hitCounter+=1
            if power!=4:
                bxs = (((bxs * (20/2-30/2) + (2 * 30/2 * 0.01)) / (20/2+30/2))*5)+(random(-0.2,0.2))
                bys = (((bys * (20/2-30/2) + (2 *  30/2 * 0.01)) / (20/2+30/2))*5)+(random(-0.2,0.2))
        if dist(Brick.x,Brick.y,bx,by)<((Brick.size/2)+(bSize/2)) and Brick.size>=35:
           
           bxs = (((bxs * (20/2-30/2) + (2 * 30/2 * 0.01)) / (20/2+30/2))*5)+(random(-0.2,0.2))
           bys = (((bys * (20/2-30/2) + (2 *  30/2 * 0.01)) / (20/2+30/2))*5)+(random(-0.2,0.2))
           Brick.size-=10
           
        for NoBreakBrick in noBreakBricks:
            NoBreakBrick.draw()
            if dist(NoBreakBrick.x,NoBreakBrick.y,bx,by)<((NoBreakBrick.size/2)+(bSize/2)):
                NoBreakBrick.x=random(100,900)
                NoBreakBrick.y=random(150,350)
                bxs = (((bxs * (20/2-30/2) + (2 * 30/2 * 0.01)) / (20/2+30/2))*5)+(random(-0.2,0.2))
                bys = (((bys * (20/2-30/2) + (2 *  30/2 * 0.01)) / (20/2+30/2))*5)+(random(-0.2,0.2))
def nextLevel():
    global hitCounter,level,moving,lifeTimer,bricks,noBreakBricks,lives
    if hitCounter==len(bricks):
        moving=False
        for Brick in bricks:
            bricks=[]
        for NoBreakBrick in noBreakBricks:
            noBreakBricks=[] 
        level+=1
        Level(level)
        lifeTimer=0
        hitCounter=0
        lives+=3
        
def powers(power):
    global paddleWidth,ps,bSize,moving,bx,by
    
    if power==0:
        frameRate(60)
        bSize=20
        paddleWidth=120
    
    if power==1:
        if by>500 or by<100:
            frameRate(15)
        else:
            frameRate(60)
    if power==2:
        p2x=(width-mouseX)-paddleWidth/2
    if power==3:
        paddleWidth+=ps
        if paddleWidth>240:
            ps*=-1
        if paddleWidth<80:
            ps*=-1
    if power==4:
        ballColor=color(245,173,40)
    if power==5:
        bSize=100
    if power==6 and by<550+bSize/2 and by>550-bSize/2 and bx+bSize/2>p1.x and bx+bSize/2<p1.x+paddleWidth: 
        moving=False

    
def getPower():
    global powerSpawn,powerOn,py,px,p,power,paddleWidth,p1,p2
    if powerSpawn==int(random(0,500)) and powerOn==False and moving==True:
        py=(random(150,350))
        px=(random(100,900))
   
        
        powerOn=True
        
    
    if powerOn==True:
        p=(PowerUP(px,py))
        py+=4
        p.draw()
    if py>600:
        powerOn=False
        power=0
    if py<550+50/2 and py>550-50/2 and px+50/2>p1.x and px-50/2<p1.x+paddleWidth:   
        power=int(random(1,7))
        px=-10000
        py=-2000
    print(powerOn)
    
def playing():
    global gameStarted,lives,lifeTimer,level,infoTimer,power,bricks,hitCounter,power,noBreakBricks
    if gameStarted==False:
        cursor()
        pushMatrix()
        scale(0.6)
        image(startScreen,-150,0)
        popMatrix()
        textAlign(CENTER,CENTER)
        textFont(f,200)
        fill(0)
        text("Breakout",width/2,height/2)
        textSize(30)
        text("By Tom--Right Click to Play",width/2,height/2+100)
    else:
        noCursor()
        lifeTimer+=1
        infoTimer+=1
    if gameStarted==False and mousePressed and mouseButton==RIGHT:
        gameStarted=True
    if lifeTimer>1 and lifeTimer<50:
        textAlign(CENTER,CENTER)
        textFont(f,400)
        fill(0)
        text(str(level)+":"+str(lives),width/2+25,height/2)
    if infoTimer>1 and infoTimer<50:
        textSize(60)
        text("Lvl:Lvs",width/2-20,height/2-150)
        text("Left Click",width/2-20,height/2+150)
    if lives<1:
        for Brick in bricks:
            bricks=[]
        for NoBreakBrick in noBreakBricks:
            noBreakBricks=[]
        hitCounter=0
        level=1
        Level(level)
        power=0
        moving=False
        
        gameStarted=False
        lives=5
        lifeTimer=0
        level=1
        infoTimer=0
