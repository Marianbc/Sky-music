import time, os, utils, abc
from PIL import Image

lastShot= 0
shotTimer= 5

class CheckDriver(abc.ABC):
	@property
	def client(self): raise NotImplementedError
	@property
	def device(self): raise NotImplementedError
	@property
	def id(self): raise NotImplementedError

	@abc.abstractmethod
	def __init__(self, id): pass

	def getScreen(self, live=False):
		global lastShot
		if live or time.time()-lastShot > shotTimer:
			adbCmd= f"adb -s 127.0.0.1:{self.id} "
			os.system(adbCmd + f"exec-out screencap -p > {utils.cacheDir}screen{self.id}.png")
			lastShot= time.time()
		return Image.open(f'{utils.cacheDir}screen{self.id}.png')

	# Inventory full message check
	def fullCheck(self):
		im= self.getScreen(live=True)
		#isFull= im.getpixel((902,305))[:3] == (255,255,0)
		isFull= im.getpixel((451, 153))[:3] == (255,255,0)

		return isFull

	def getColor(self, tup):
		im= self.getScreen(live=True)
		print(im.getpixel(tup))

	def check(self, color, loc, tup=None, live=False):
		if not tup: tup= (0,0, 960, 540) #1920,1080)
		loc= (loc[0]-tup[0], loc[1]-tup[1])

		im= self.getScreen(live=False)
		print(loc, im.getpixel(loc)[:3])
		return im.getpixel(loc)[:3] == color