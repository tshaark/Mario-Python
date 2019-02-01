import objects
import sys
from os import system

class board:
	def __init__(self):	
		self.array = [[] for x in range(42)]
	def makeArray(self):
		for i in range(0,42):
			for j in range(0,2000):
				if i == 0 or i >= 38:
					self.array[i].append('\x1b[4;33;43m'+'X'+'\x1b[0m')
				else:
					self.array[i].append('\x1b[3;34;44m'+' '+'\x1b[0m')
	def getPrint(self,a):
		system('clear')
		print('SCORE'+'-',objects.game.score,end='         ')
		print('COINS'+'-',objects.game.coins)
		for i in range(0,42):
			for j in range(0+a,200+a):
				# print(self.array[i][j],end='')
				sys.stdout.write(str(self.array[i][j]))
			print('\n',end='')


