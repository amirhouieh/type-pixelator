from random import random
from drawBot import *
from AppKit import NSColor


class dotDict(dict):
	"""dot.notation access to dictionary attributes"""
	def __getattr__(self, attr):
		return self.get(attr)
	__setattr__= dict.__setitem__
	__delattr__= dict.__delitem__






class Element(object):

	rgbStack = {"black":(0,0,0), "white":(255,255,255), "blue":(100,100,255), "green":(0,200,0), "red":(200,0,50), "yellow":(255,255,0), "orange":(255,165,0), "purple":(200,100,255), "brown":(150,100,50), "aqua":(0,150,150), "gray":(175,175,175), "grey":(175,175,175), "magenta":(255,0,255), "pink":(255,100,100), "gold":(200,200,0), "rose":(200,150,200), "darkblue":(0,0,255), "darkgreen":(0,255,0), "darkred":(255,0,0), "darkgray":(111,111,111), "darkgrey":(111,111,111) }

	def __init__(self, clasName, x, y, w, h, fillColor, strokeColor, strokeWeight, fillOpacity, strokeOpacity ):
		self._pos  = 	dotDict( dict(x=x, y=y) )
		fillColor = self.parseColor(fillColor, fillOpacity)
		strokeColor = self.parseColor(strokeColor, strokeOpacity)
		self._style = 	dotDict( dict( fillColor = fillColor, strokeColor = strokeColor, strokeWeight = strokeWeight ) )
		self.x = 		x
		self.y = 		y
		self.width = 	w
		self.height = 	h
		self.center = False
		self.clasName = clasName

	def getOrSet(self, attrSetName, props):
		attrSet = self.__dict__[ attrSetName ]
		if type( props ) is dict:
			attrSet.update( props )
		elif props is None:
			return attrSet
		elif type( props ) is str:
			return attrSet[ props ]

	def style(self, props=None):
		return self.getOrSet('_style', props)

	def position(self, props=None):
		return self.getOrSet('_pos', props)

	def get_rgba_from_nsColor(self, color):
		c = color.getRed_green_blue_alpha_
		try:
		    return c()
		except TypeError:
		    return c(None, None, None, None)


	def parseColor(self, color, opacity):
		# if isinstance(color, tuple):
		# 	....
		# elif isinstance(color, NSColor):
		# 	...
		# elif isinstance(color, basestring):
		# 	...
		# else:
		# 	?????

		typeName = type(color).__name__ 

		if typeName == "NSCalibratedRGBColor":
			color = self.get_rgba_from_nsColor( color )
			return color

		if ( typeName == "tuple" and len(color) == 4 ) or color is None:
			return color

		if type(color) is str and color in self.rgbStack:
			color = self.rgbStack[ color ]

		return color + (opacity, )

class EasyCanvas:
	"""
	"""
	def __init__(self):
		pass


	def square(self, x=None, y=None, size=None, fillColor=None, strokeColor=None, strokeWeight=None, fillOpacity=1, strokeOpacity=1, center=False):
		this = Element('square', x, y, size, size, fillColor, strokeColor, strokeWeight, fillOpacity, strokeOpacity)
		return this

	def circle(self, x=None, y=None, size=None, fillColor=None, strokeColor=None, strokeWeight=None, fillOpacity=1, strokeOpacity=1, center=False):
		this = Element('circle', x, y, size, size, fillColor, strokeColor, strokeWeight, fillOpacity, strokeOpacity)
		return this

	def rect(self, x=None, y=None, width=None, height=None, fillColor=None, strokeColor=None, strokeWeight=None, fillOpacity=1, strokeOpacity=1, center=False):
		this = Element('rect', x, y, width, height, fillColor, strokeColor, strokeWeight, fillOpacity, strokeOpacity)
		return this

	class randomColor():
	    def __init__(self):
	        pass

	    def rgb(self, opacity = 1):
	        return random(), random(), random()

	    def gray(self, opacity = 1):
	        c = random()
	        return c, c, c


	def centerToEelement( self, x, y):
		translate( (width()-x) / 2, (height() - y ) / 2)

	def draw(self, elem):
		style = elem.style()
		shapeKind = elem.clasName

		if style.strokeColor is not None:
			stroke( *style.strokeColor )
		
		if style.fillColor is not None:
			fill( *style.fillColor )

		if style.strokeWeight is not None:
			strokeWidth( style.strokeWeight )


		if elem.center:
			if elem.width == elem.height:
				elem.x-=elem.size/2
				elem.y-=elem.size/2
			else:
				elem.x-=elem.w/2
				elem.y-=elem.h/2

		if shapeKind is "rect":
			rect(elem.x, elem.y, elem.width, elem.height)
		elif shapeKind is "square":
			rect(elem.x, elem.y, elem.width, elem.width)
		elif shapeKind is "circle":
			oval(elem.x, elem.y, elem.width, elem.width)

