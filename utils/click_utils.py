import utils, time, random, abc
# https://www.kernel.org/doc/html/v4.14/input/multi-touch-protocol.html
# Origionally by Literal Genie
defRand= 20

# (0,1), (0,2), ..., (5,4), (5,5)
cartProd= []
for i in range(6):
	for j in range(6):
		cartProd.append( (i,j) )

sendCmd= "su -c sendevent /dev/input/event2 "
#sendCmd= "sendevent /dev/input/event2 "

class ClickDriver(abc.ABC):
	@property
	def client(self): raise NotImplementedError
	@property
	def device(self): raise NotImplementedError


	@abc.abstractmethod
	def __init__(self, id): pass

	def dumpInv(self, rng=range(36), delay=0.2):
		self.press(*utils.dct['int'])
		time.sleep(.5)

		for i in rng:
			x,y= utils.dct['stor0']
			x+= utils.dct['r'] * cartProd[i][1]
			y+= utils.dct['r'] * cartProd[i][0]

			randX= random.randint(0,10)-20
			randY= random.randint(0,10)-20
			x+= randX
			y+= randY

			self.press(x, y)
			time.sleep(delay)
		self.clickInt()


	def press(self, x,y, rand=defRand, num=1):
		if rand is not None:
			x+= random.randint(0,rand)- int(rand/2)
			y+= random.randint(0,rand)- int(rand/2)

		for i in range(num):
			# print('tapping',x,y)
			self.tapDown(x,y)
			self.tapUp()

	def pressHold(self, x,y,wait, rand=defRand, num=1):
		if rand is not None:
			x+= random.randint(0,rand)- int(rand/2)
			y+= random.randint(0,rand)- int(rand/2)

		for i in range(num):
			# print('tapping',x,y)
			self.tapDown(x,y)
			time.sleep(wait)
			self.tapUp()

	def clickInv(self):
		self.press(*utils.dct['inv'])

	def clickInt(self):
		self.press(*utils.dct['int'])

	def smelt(self):
		self.press(620, 400)#1240, 800)
		self.press(700, 400)#1400, 800)

	# ONE-INDEXED
	def clickSlot(self, i, num=1, inv=False, rStor=False):
		i-=1

		if inv: x,y= utils.dct['inv0']
		elif rStor: x,y= utils.dct['stor00']
		else: x,y= utils.dct['stor0']

		x+= utils.dct['r'] * cartProd[i][1]
		y+= utils.dct['r'] * cartProd[i][0]

		self.press(x,y, num=num)

	def tapDown(self, x,y): self.mtDown([(x,y)])
	def tapUp(self): self.mtUp()

	def mtDown(self, lst):
		self.tpDown()
		for coord in lst: self.tp(*coord)
		self.tpSend()
	def mtUp(self):
		self.tpUp()
		self.tpSend()

	def tpDown(self): self.device.shell("su -c " + sendCmd + "3 57 374")
	def tpUp(self): self.device.shell(sendCmd + "3 57 -1")#4294967295")
	def tpSend(self): self.device.shell(sendCmd + "0 0 0")
	def tp(self, x,y, rand=defRand):
		#print("please work")
		if rand is not None:
			x+= random.randint(0,rand)- int(rand/2)
			y+= random.randint(0,rand)- int(rand/2)
		events= [
			 f"3 54 {x}",
			 f"3 53 {1080-y}",
			 "0 0 0",
		]
		for x in events: self.device.shell(sendCmd + x)

 			#f"3 53 {x}",
			# f"3 54 {y}",
			# "0 2 0",
