from random import random
from random import randint

import easyCanvasLight
from easyCanvasLight import *
from datetime import datetime

import Grid
from Grid import *

canvas = EasyCanvas()
rndCol = canvas.randomColor()

letters = [["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]]

shapse=["circle", "square"]


size(1000, 1000)
_fontSize = 300


def draw(i):
    canvas = EasyCanvas()
    path = BezierPath()

    fillColors = [None, (0,0,0)]
    strokeColors = [None, (0,0,0)]
    #fillColor = fillColors[randint(0,1)]
    fillColor = None
    #strokeColor = strokeColors[randint(0,1)]
    print(fillColor)
    strokeColor = (0,0,0)
    #cubeSize = randint(0, 40)
    cubeSize = 24
    #gap = randint( -2, int(cubeSize/2) )
    gap = i
    #strokeWeight = randint(0,70)
    strokeWeight = 14
    #fillOpacity = random()
    fillOpacity = 1
    #strokeOpacity = random()
    strokeOpacity = 0.8
    fontIndex  = randint(0,20)
    string = letters[ randint(0,1) ][ randint(0,22) ]
    #string = "Re-"
    #shape = shapse[ randint(0,1) ]
    shape = shapse[1]


    #fontFamily = installedFonts()[int(fontIndex)]
    fontFamily = ".AlNilePUA-Bold"

    path.text(  string, 
                font = fontFamily, 
                fontSize = _fontSize,
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
                strokeWeight=strokeWeight, 
                fillOpacity= fillOpacity, 
                strokeOpacity = strokeOpacity )
    fill(0)
    stroke()
    fontSize(20)
    textBox(fontFamily,
                (0, 20, 1000, 100), align="center")
    textBox("cubeSize: " + str(cubeSize),
                (0, 900, 1000, 100), align="center")
    textBox("gap: " + str(gap),
                (0, 880, 1000, 100), align="center")
    textBox("strokeWeight: " + str(strokeWeight),
                (0, 860, 1000, 100), align="center")
    textBox("_fontSize: " + str(_fontSize),
                (0, 840, 1000, 100), align="center")

offset = (110,350)
for i in range(0, 4):
    draw(i)
    newPage(1000,1000)



#saveImage(["~/Desktop/pixelator.gif"])


"""
for l in range( 0, len(caps) ):
    draw( lows[l] ) 


saveImage(["~/Desktop/drawbot/" + fontName + "_lows_" + str(datetime.now().time()) + ".pdf"])
"""
