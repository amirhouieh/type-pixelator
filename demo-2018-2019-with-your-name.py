from random import random
from random import randint

from easyCanvasLight import *
from grid import *

from datetime import datetime


canvas = EasyCanvas()
rndCol = canvas.randomColor()

shapse=["circle", "square"]
text = "2018"


size(1000, 1000)
_fontSize = 342



def draw(i, sw, fs, cubeSize):
    print(fs)
    #fill(0, 0, 0, 1)
    #rect(0, 0, 1000, 1000)
    canvas = EasyCanvas()
    path = BezierPath()

    fillColor = (0,0,0)
    strokeColor = None
    gap = 0
    fillOpacity = 0
    strokeOpacity = 1
    shape = shapse[1]

    #fontFamily = ".AlNilePUA-Bold"
    fontFamily = "ArimoForPowerline"

    path.text(  text, 
                font = fontFamily, 
                fontSize = fs,
                offset= offset 
            )
    grid = Grid( 
                shape= shape,
                size = cubeSize, 
                gap = gap, 
                box= path.bounds(), 
                path = path)

    grid.go( 
                fillColor=fillColor, 
                strokeColor=strokeColor, 
                strokeWeight=sw, 
                fillOpacity= fillOpacity, 
                strokeOpacity = strokeOpacity )
    newPage(1000,1000)



offset = (110,350)

for i in range(0, 35):
    draw(i, i+5, _fontSize, 17)

text = "2019"
for i in reversed(range(5, 35)):
    draw(i, i-5, _fontSize, 17)

offset = (180,450)
text = "your name"
for i in reversed(range(1, 35)):
    draw(i, 1, 100, 5) 

saveImage("~/Desktop/pixelator-white-"+ text +".gif")
    
