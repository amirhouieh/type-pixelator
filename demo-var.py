from easyCanvasLight import *
from datetime import datetime

from grid import *

canvas = EasyCanvas()
rndCol = canvas.randomColor()

size(1000, 1000)
_fontSize = 600
gap = 10
useRandomFillColor = True
useRandomStrokeColor = True
fonts = [x for x in installedFonts() if not x.startswith(".") and "-" not in x ]
print(len(fonts))

print(fonts)

sliderFontIndexArgs = dict( value=0, minValue=0, maxValue=len(fonts)-1, tickMarkCount=len(fonts)-1, stopOnTickMarks=True)
sliderPixelSizeArgs = dict( value=40, minValue=1, maxValue=101, tickMarkCount=25, stopOnTickMarks=True)
sliderShapeArgs = dict( value=0, minValue=0, maxValue=1, tickMarkCount=2, stopOnTickMarks=True)
sliderGapArgs = dict( value= 0, minValue= -20, maxValue= 100, tickMarkCount=30, stopOnTickMarks=True)
sliderFontSizeArgs = dict( value=200, minValue=100, maxValue=800, tickMarkCount=50, stopOnTickMarks=True)
sliderFillOpacityArgs = dict( value=1, minValue=0, maxValue=1, tickMarkCount=0.05)
sliderStrokeOpacityArgs = dict( value=1, minValue=0, maxValue=1, tickMarkCount=0.05)
sliderStrokeWeightArgs = dict( value=1, minValue=0, maxValue=500, tickMarkCount=250)

Variable([
    dict(name="fontIndex", ui="Slider", args=sliderFontIndexArgs),
    dict(name="pixelSize", ui="Slider", args=sliderPixelSizeArgs),
    dict(name="shape", ui="Slider", args=sliderShapeArgs),
    dict(name="gap", ui="Slider", args=sliderGapArgs),
    dict(name="sliderFontSize", ui="Slider", args=sliderFontSizeArgs),
    dict(name="fillOpacity", ui="Slider", args=sliderFillOpacityArgs),
    dict(name="strokeOpacity", ui="Slider", args=sliderStrokeOpacityArgs),
    dict(name="strokeWeight", ui="Slider", args=sliderStrokeWeightArgs),
    dict(name="useRandomFillColor", ui="CheckBox", args=dict(value=True)),
    dict(name="useRandomStrokeColor", ui="CheckBox", args=dict(value=True)),
    dict(name="fillColor", ui="ColorWell"),
    dict(name="strokeColor", ui="ColorWell"),
    ], globals() )

print(useRandomFillColor)
print(useRandomStrokeColor)

if useRandomFillColor:
    fillColor = None

if useRandomStrokeColor:
    strokeColor = None

def draw(txt):
    canvas = EasyCanvas()
    path = BezierPath()
    font = fonts[ int(fontIndex) ]

        
    print(fillColor)
    if int(shape) is 0:
        newshape = "circle"
    else:
        newshape = "square"

    path.text(  txt, 
                font = font, 
                fontSize = int(sliderFontSize),
                offset= offset 
            )
            
    grid = Grid( 
                shape= newshape,
                size = int(pixelSize), 
                gap = int(gap), 
                box= path.bounds(), 
                path = path)

    grid.go( 
        fillColor=fillColor, 
        strokeColor=strokeColor,
        strokeWeight=strokeWeight, 
        fillOpacity= fillOpacity, 
        strokeOpacity = strokeOpacity )
    
    info = font+"\nfont-size: "+str(int(sliderFontSize))+"\ngap: "+str(int(gap))+"\npixel-size: "+ str(int(pixelSize))
    fontSize(12)
    fill(0)
    stroke()
    text(info, (100, 100))
    
    
ttl = "FLYINGDUTCHMENGOTOPSY-TURVY"


offset = (100,300)  
draw("H")

#for t in ttl:  
    #offset = (300,300)  
    #draw(t)


