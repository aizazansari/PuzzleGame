m=''
x=0
def setup():
    global m 
    size(800,600)
    m=loadImage('test.png')
    
def draw():
    global m,x
    background(0)
    #image(m,400,300)
    #image(m,0,0,304,400)
    image(m,50+x,450,100,100,0,0,152,176)
    image(m,100+x,400,100,100,304,176,152,0)
    x=x+1