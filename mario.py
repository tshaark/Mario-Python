from getch import _getChUnix as getChar
from alarmexception import AlarmException
from os import system
import sys
import signal
from time import sleep
import objects
from random import randint

# objects.game.score



class Mario():
	def __init__(self):
		self.x=1
		self.y=35
		self.jump= False
		self.a=0
		self.temp=self.y
		self.moveL=1
		self.moveR=1
		self.matrix=[[] for i in range(0,3)]
	def showMario(self):
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[1;37;40m'+'o'+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[4;32;42m'+'-'+'\x1b[0m','\x1b[4;32;42m'+'I'+'\x1b[0m','\x1b[4;32;42m'+'-'+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[2]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[0;37;47m'+'M'+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		for i in range(0,3):
			for j in range(0,5):
				self.array[self.y+i][self.x+j]=self.matrix[i][j]
	def sendCoords(self):
		return self.x,self.y
	def clearMario(self):
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[2]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		for i in range(0,3):
			for j in range(0,5):
				self.array[self.y+i][self.x+j]=self.matrix[i][j]
	def checkCollision(self):
		for j in range(0,5):
			if self.array[self.y-1][self.x+j] != '\x1b[3;34;44m'+' '+'\x1b[0m' and self.array[self.y-1][self.x+j] != '\x1b[2;33;43m'+'*'+'\x1b[0m':
				self.flag=1
			if self.array[self.y+3][self.x+j] != '\x1b[3;34;44m'+' '+'\x1b[0m' and self.array[self.y+3][self.x+j] != '\x1b[2;33;43m'+'*'+'\x1b[0m':
				self.jump=False
		if self.array[self.y+3][self.x] == '\x1b[3;34;44m'+' '+'\x1b[0m':
			if self.array[self.y+3][self.x+1] == '\x1b[3;34;44m'+' '+'\x1b[0m':
				if self.array[self.y+3][self.x+2] == '\x1b[3;34;44m'+' '+'\x1b[0m':
					if self.array[self.y+3][self.x+3] == '\x1b[3;34;44m'+' '+'\x1b[0m':
						if self.array[self.y+3][self.x+4] == '\x1b[3;34;44m'+' '+'\x1b[0m' and self.jump == False:
							self.jump=True
							self.flag=1
		if self.y+4 >= 40:
			print('GAME OVER')
			sys.exit(0)
		for i in range(-1,3):
			if self.array[self.y+i][self.x-1] == '\x1b[3;31;41m'+'B'+'\x1b[0m' or self.array[self.y+i][self.x] == '\x1b[3;31;41m'+'B'+'\x1b[0m':
					self.moveL=0
			if self.array[self.y+i][self.x+5] == '\x1b[3;31;41m'+'B'+'\x1b[0m' or self.array[self.y+i][self.x+4] == '\x1b[3;31;41m'+'B'+'\x1b[0m':
					self.moveR=0
			if self.array[self.y+i][self.x-1] == '\x1b[1;33;40m'+'$'+'\x1b[0m' or self.array[self.y+i][self.x] == '\x1b[1;33;40m'+'$'+'\x1b[0m':
					self.moveL=0
			if self.array[self.y+i][self.x+5] == '\x1b[1;33;40m'+'$'+'\x1b[0m' or self.array[self.y+i][self.x+4] == '\x1b[1;33;40m'+'$'+'\x1b[0m':
					self.moveR=0
			if self.array[self.y+i][self.x-1] == '\x1b[4;32;42m'+'|'+'\x1b[0m' or self.array[self.y+i][self.x] == '\x1b[4;32;42m'+'|'+'\x1b[0m':
					self.moveL=0
			if self.array[self.y+i][self.x+5] == '\x1b[4;32;42m'+'|'+'\x1b[0m' or self.array[self.y+i][self.x+4] == '\x1b[4;32;42m'+'|'+'\x1b[0m':
					self.moveR=0

	def spawn(self,array):
		self.array=array
		self.showMario()
		return self.array
	def jumpMario(self):
		if self.jump == True:
			if self.y == self.temp - 10 or self.flag == 1:
				self.clearMario()
				self.y += 1
				self.showMario()
				self.flag = 1
			elif self.flag == 0:
				self.clearMario()
				self.y -= 1
				self.showMario()
	def moveMario(self,array):
		self.array=array
		def alarmhandler(signum, frame):
			''' input method '''
			raise AlarmException
		def input(timeout=0.6):
			''' input method '''
			signal.signal(signal.SIGALRM, alarmhandler)
			signal.setitimer(signal.ITIMER_REAL, timeout)
			try:
				text = getChar()()
				signal.alarm(0)
				return text
			except AlarmException:
				pass
			signal.signal(signal.SIGALRM, signal.SIG_IGN)
			return ''
		char = input()
		self.checkCollision()
		if char == 'q':
			print('GAME OVER')
			sys.exit(0)
		if char == 'd' and self.moveR == 1:
			self.clearMario()
			self.a+=1
			if self.x >= 100:
				self.x+=1
			else:
				self.x+=2
			self.showMario()
		if char == 'a' and self.moveL == 1:
			self.a-=1
			self.clearMario()
			if self.x <= 100:
				self.x -= 1
			else:
				self.x-=2
			self.showMario()	
		if char =='w' and self.jump== False:
			self.jump = True
			self.flag=0
			self.temp=self.y
		if self.jump == True:
			self.jumpMario()
		self.moveR=1
		self.moveL=1


		return self.array


