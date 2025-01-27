import utils
from ppadb.client import Client as AdbClient
# https://pypi.org/project/pure-python-adb/

class Driver(utils.ClickDriver, utils.MoveDriver, utils.CheckDriver):
	id=device=client=None

	def __init__(self, id):
		self.client = AdbClient()
		self.devices= self.client.devices()
		self.id= id
		for d in self.devices:
			self.device = d
