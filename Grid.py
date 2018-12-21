from math import *
from easyCanvasLight import *


class Cube():
	def __init__(self, arqs):
		self.pos = ( arqs[0], arqs[1] )
		self.allPoints = self.getPointsInCube( self.pos, arqs[2] )

	def getPointsInCube(self, start, size):
		"""
		get all the points which is inside a cube starts from x, y
		"""	
		startX = int(start[0])
		startY = int(start[1])
		return [ (x,y) for y in range( startY, startY + size ) for x in range( startX, startX + size ) ]


class Grid():
	canvas = EasyCanvas()
	rc = canvas.randomColor()
	def __init__(self, shape, size, gap, box, path):
		self.path = path
		self.size = int(size)
		self.gap = int(gap)
		self.sizeGap = gap + size
		self.startX, self.startY, self.width, self.height = box
		self.cubes = [ Cube( (x,y, self.size) ) for y in range( int(self.startY), int(self.height), int(self.sizeGap) ) for x in range( int(self.startX), int(self.width), int(self.sizeGap) ) if path.pointInside( (x,y) )]
		self.shape = shape



	def go(self, fillColor=None, strokeColor=None, strokeWeight = 1, fillOpacity = 1, strokeOpacity = 1 ):
		useRandomForFill =  fillColor is None
		useRandomForStroke =  strokeColor is None
		# newPage()
		for cube in self.cubes:
			if useRandomForFill:
				fillColor = self.rc.rgb()

			if useRandomForStroke:
				strokeColor = self.rc.rgb()

			if self.shape == "circle":
				cubeElem = self.canvas.circle(x=cube.pos[0],y=cube.pos[1],size= self.size,fillColor=fillColor,fillOpacity= fillOpacity, strokeColor=strokeColor, strokeOpacity = strokeOpacity, strokeWeight=strokeWeight )
			if self.shape == "square":
				cubeElem = self.canvas.square(x=cube.pos[0],y=cube.pos[1],size= self.size,fillColor=fillColor,fillOpacity= fillOpacity, strokeColor=strokeColor, strokeOpacity = strokeOpacity, strokeWeight=strokeWeight )
			self.canvas.draw( cubeElem )
