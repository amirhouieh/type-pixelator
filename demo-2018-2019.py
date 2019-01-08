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
    fill(1, 1, 1, 1)
    rect(0, 0, 1000, 1000)
    canvas = EasyCanvas()
    path = BezierPath()

    fillColor = None
    strokeColor = None
    gap = 0
    fillOpacity = 1
    strokeOpacity = 0.4
    shape = shapse[0]

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
puls = 10
for i in range(0, 30):
    draw(i, i*puls, _fontSize, 17)

text = "2019"
for i in reversed(range(0, 30)):
    draw(i, i*puls, _fontSize, 17)

saveImage("~/Desktop/pixelator-white-18-19.gif")
    
