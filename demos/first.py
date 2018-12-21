import easyCanvasLight
reload( easyCanvasLight )
from easyCanvasLight import *
from datetime import datetime

import Grid
reload( Grid )
from Grid import *

canvas = EasyCanvas()
rndCol = canvas.randomColor()

size(1000, 1000)
_fontSize = 600
cubeSize =40
gap = 10


Variable([
    dict(name="font", ui="Slider", args=dict( value=0, minValue=-20, maxValue=40) ),
    dict(name="cubeSize", ui="Slider", args=dict( value=30, minValue=1, maxValue=100) ),
 dict(name="shape", ui="Slider", args=dict( value=0, minValue=0, maxValue=2) ),
    dict(name="gap", ui="Slider", args=dict( value= 0, minValue= -2, maxValue= 100) ),
    dict(name="_fontSize", ui="Slider", args=dict( value=500, minValue=50, maxValue=500) ),
    dict(name="fillOpacity", ui="Slider", args=dict( value=1, minValue=0, maxValue=1) ),
    dict(name="strokeOpacity", ui="Slider", args=dict( value=1, minValue=0, maxValue=1) ),
    dict(name="strokeWeight", ui="Slider", args=dict( value=1, minValue=0, maxValue=500) ),
    dict(name="useRandomFillColor", ui="CheckBox"),
    dict(name="useRandomStrokeColor", ui="CheckBox"),
    dict(name="fillColor", ui="ColorWell"),
    dict(name="strokeColor", ui="ColorWell"),
    ], globals() )

if useRandomFillColor:
    fillColor = None
if useRandomStrokeColor:
    strokeColor = None

def draw(txt):
    canvas = EasyCanvas()
    path = BezierPath()
    
    if int(shape) is 0:
        newshape = "circle"
    else:
        newshape = "square"
    
    path.text(  txt, 
                font = installedFonts()[ int(31) ], 
                fontSize = _fontSize,
                offset= offset 
            )
            
    grid = Grid( 
                shape= newshape,
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
    fontSize(20)
    fill(0)
    stroke()
    text(installedfonts()[ int(_fontSize) ], (100, 100))
    
    
ttl = "FLYINGDUTCHMENGOTOPSY-TURVY"


offset = (100,300)  
draw("Re-")

#for t in ttl:  
    #offset = (300,300)  
    #draw(t)


