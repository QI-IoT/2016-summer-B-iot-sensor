from neo import Gpio
from time import sleep
import threading

gpio = Gpio()

class ledThread(threading.Thread):
	def _init_(self, pinNumber , counter):
		threading.Thread._init_(self)
		self.thredID = threadID
		self.name = name
		self.counter = counter
	def run(self)
				
