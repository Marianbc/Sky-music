import time, abc, utils, subprocess

keyCmd= "sendevent /dev/input/event4 "
fin= f"{keyCmd} 0 0 0"

class MoveDriver(abc.ABC):
	@property
	def client(self): raise NotImplementedError
	@property
	def device(self): raise NotImplementedError

	@abc.abstractmethod
	def __init__(self, id): pass

	def sendCodes(self, lst, delay=0.5):
		for x in lst:
			self.device.shell(f"{keyCmd} 1 {x} 1")
		self.device.shell(fin)

		time.sleep(delay)

		for x in lst:
			self.device.shell(f"{keyCmd} 1 {x} 0")
		self.device.shell(fin)


	def move(self, k,t):
		code= utils.dct[k]
		self.sendCodes([code], t)
		time.sleep(.1)

	def combo(self, k1,k2,t):
		lst= [utils.dct[k1], utils.dct[k2]]
		self.sendCodes(lst, t)
		time.sleep(.1)


	def u(self, t): self.move('up',t)
	def d(self, t): self.move('down',t)
	def r(self, t): self.move('right',t)
	def l(self, t): self.move('left',t)

	def ul(self, t): self.combo('up','left',t)
	def ur(self, t): self.combo('up','right',t)
	def dl(self, t): self.combo('down','left',t)
	def dr(self, t): self.combo('down','right',t)


	def c2f(self):
		self.r(2.5)
		self.u(.5)
		self.dr(.5)
		self.r(1)
		self.ur(2.5)

	def f2c(self):
		self.d(1)
		self.dl(1)
		self.ul(.4)
		self.l(3)

		self.ul(1.5)
		self.d(.7)
		self.cc2c()

	def cc2c(self):
		self.l(.15)
		self.d(.55)
		self.r(.25)
		self.u(.25)

	def mvDown(self, k): self.device.shell(f"{keyCmd} 1 {utils.dct[k]} 1")
	def mvUp(self, k): self.device.shell(f"{keyCmd} 1 {utils.dct[k]} 0")