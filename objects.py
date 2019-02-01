from random import randint
import sys
import time
from globalVars import *
game=gameplay()


class Enemy():
	def __init__(self,x):
		self.matrix=[[] for i in range(0,2)]
		self.x=x
		self.y=36
		self.flag=0
	def generateEnemy(self,array,x):
		self.x=x
		self.array=array
		self.matrix[0]=['\x1b[0;30;40m'+'<'+'\x1b[0m','\x1b[0;30;40m'+'<'+'\x1b[0m']
		self.matrix[1]=['\x1b[3;37;47m'+'0'+'\x1b[0m','\x1b[3;37;47m'+'0'+'\x1b[0m']
		for i in range(0,2):
			for j in range(0,2):
				self.array[self.y+i][self.x+j]=self.matrix[i][j]
		return self.array
	def clearEnemy(self,array,x):
		self.x=x
		self.array=array
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		for i in range(0,2):
			for j in range(0,2):
				self.array[self.y+i][self.x+j]=self.matrix[i][j]
		return self.array
	def moveEnemies(self,array):
		self.array=array
		self.array=self.clearEnemy(self.array,self.x)
		if self.array[self.y][self.x-1] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 0:
			self.flag = 1
		elif self.array[self.y][self.x+1] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 1:
			self.flag = 0
		elif self.array[self.y][self.x+2] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 1:
			self.flag = 0

		if self.flag == 0:
			self.x -= 1
		elif self.flag == 1:
			self.x += 1
		if self.x > 1960:
			self.flag = 0
		self.array=self.generateEnemy(self.array,self.x)
		return self.array
	def checkCollision(self,xCoord,yCoord):
		self.xCoord=xCoord
		self.yCoord=yCoord
		for i in range(0,3):
			if self.array[self.yCoord+3][self.xCoord+i] == '\x1b[0;30;40m'+'<'+'\x1b[0m':
				game.score+=50
				return 1
			if self.array[self.yCoord+1][self.xCoord+i] == '\x1b[0;30;40m'+'<'+'\x1b[0m':
				print('GAME OVER')
				sys.exit(0)



class smartEnemy():
	def __init__(self,x):
		self.matrix=[[] for i in range(0,2)]
		self.x=x
		self.y=36
		self.flag=0
	def generateEnemy(self,array,x):
		self.x=x
		self.array=array
		self.matrix[0]=['\x1b[4;35;45m'+'<'+'\x1b[0m','\x1b[4;35;45m'+'<'+'\x1b[0m']
		self.matrix[1]=['\x1b[3;37;47m'+'0'+'\x1b[0m','\x1b[3;37;47m'+'0'+'\x1b[0m']
		for i in range(0,2):
			for j in range(0,2):
				self.array[self.y+i][self.x+j]=self.matrix[i][j]
		return self.array
	def clearEnemy(self,array,x):
		self.x=x
		self.array=array
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		for i in range(0,2):
			for j in range(0,2):
				self.array[self.y+i][self.x+j]=self.matrix[i][j]
		return self.array
	def moveEnemies(self,array,xCoord,yCoord):
		self.xCoord=xCoord
		self.yCoord=yCoord
		self.array=array
		self.flag1=1
		self.flag = 0
		self.array=self.clearEnemy(self.array,self.x)
		if self.array[self.y][self.x-1] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 0:
			self.flag = 1
			self.flag1 =0
		elif self.array[self.y][self.x] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 0:
			self.flag1 =0
			self.flag = 1
		elif self.array[self.y][self.x+1] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 1:
			self.flag1 =0
			self.flag = 0
		elif self.array[self.y][self.x+2] == '\x1b[4;32;42m'+'|'+'\x1b[0m' and self.flag == 1:
			self.flag1 =0
			self.flag = 0

		if self.flag1 == 0:
			if self.flag == 1:
				self.x-=10
			else:
				self.x+=10
		else:
			if self.x > self.xCoord:
				self.x -= 1
				self.flag = 0
			else:
				self.x += 1
				self.flag = 1
		if self.x > 1960:
			self.flag = 0
		self.array=self.generateEnemy(self.array,self.x)
		return self.array
	def checkCollision(self,xCoord,yCoord):
		self.xCoord=xCoord
		self.yCoord=yCoord
		for i in range(0,3):
			if self.array[self.yCoord+3][self.xCoord+i] == '\x1b[4;35;45m'+'<'+'\x1b[0m':
				game.score+=100
				return 1
			if self.array[self.yCoord+1][self.xCoord+i] == '\x1b[4;35;45m'+'<'+'\x1b[0m':
				print('GAME OVER')
				sys.exit(0)



class Pipe():
	def __init__(self):
		self.matrix=[[] for i in range(0,7)]
		self.y=37
		self.flag=1
		self.matrix[0]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
		self.matrix[1]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
		self.matrix[2]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
		self.matrix[3]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
		self.matrix[4]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
		self.matrix[5]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
		self.matrix[6]=['\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m','\x1b[4;32;42m'+'|'+'\x1b[0m']
	def generatePipe(self,array):
		self.array=array
		for x in range(8,1900,8):
			if randint(0, 100) < 5:
				for i in range(0,7):
					for j in range(0,7):
						if self.array[self.y-i][x+j] != '\x1b[3;34;44m'+' '+'\x1b[0m':
							self.flag=0
				if self.flag == 1:
					for i in range(0,7):
						for j in range(0,7):
							self.array[self.y-i][x+j]=self.matrix[i][j]
				self.flag = 1		
		return self.array


class Coins():
	def __init__(self):
		pass
	def generateCoins(self,array):
		self.array=array
		for x in range(8,1900,8):
			if randint(0, 100) < 20:
				self.y=randint(20,34)
				self.array[self.y][x]='\x1b[2;33;43m'+'*'+'\x1b[0m'
		return self.array
	def collision(self,array,x,y):
		self.array=array
		for i in range(-1,4):
			for j in range(-1,6):
				if self.array[y+i][x+j] == '\x1b[2;33;43m'+'*'+'\x1b[0m':
					game.coins+=1




class Badal():
	def __init__(self):
		self.matrix=[[] for i in range(0,4)]
		self.y=4
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m','\x1b[3;37;47m'+' '+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[2]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+' '+'\x1b[0m','\x1b[3;37;47m'+' '+'\x1b[0m','\x1b[3;37;47m'+' '+'\x1b[0m','\x1b[3;37;47m'+' '+'\x1b[0m','\x1b[3;37;47m'+' '+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[3]=['\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+'_'+'\x1b[0m','\x1b[3;37;47m'+'_'+'\x1b[0m','\x1b[3;37;47m'+'_'+'\x1b[0m','\x1b[3;37;47m'+'_'+'\x1b[0m','\x1b[3;37;47m'+'('+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m','\x1b[3;37;47m'+')'+'\x1b[0m']
	def generateBadal(self,array):
		self.array=array
		for x in range(8,1900,8):
			if randint(0, 100) < 15:
				for i in range(0,4):
					for j in range(0,9):
						self.array[self.y+i][x+j]=self.matrix[i][j]
		return self.array




class PointsBrick():
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.matrix=[[] for i in range(0,2)]
		self.matrix[0]=['\x1b[1;33;40m'+'$'+'\x1b[0m','\x1b[1;33;40m'+'$'+'\x1b[0m']
		self.matrix[1]=['\x1b[1;33;40m'+'$'+'\x1b[0m','\x1b[1;33;40m'+'$'+'\x1b[0m']
	def generateBricks(self,array):
		self.array=array
		for i in range(0,2):
			for j in range(0,2):
					self.array[self.y+i][self.x+j]=self.matrix[i][j]
		return self.array
	def clearBrick(self,array):
		self.array=array
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		for i in range(0,2):
			for j in range(0,2):
					self.array[self.y+i][self.x+j]=self.matrix[i][j]
		return self.array	
	def checkCollision(self,x,y,array):
		self.array=array
		self.x=x
		self.y=y
		for j in range(0,3):
			if self.array[self.y-1][self.x+j] == '\x1b[1;33;40m'+'$'+'\x1b[0m':
				game.score+=50
				return 1


class Bricks():
	def __init__(self):
		self.matrix=[[] for i in range(0,2)]
		self.matrix[0]=['\x1b[3;31;41m'+'B'+'\x1b[0m','\x1b[3;31;41m'+'B'+'\x1b[0m']
		self.matrix[1]=['\x1b[3;31;41m'+'B'+'\x1b[0m','\x1b[3;31;41m'+'B'+'\x1b[0m']
	def generateBricks(self,array):
		self.array=array
		for x in range(2,1900,2):
			if randint(0,100)<10:
				self.y=32
				for i in range(0,2):
					for j in range(0,2):
						self.array[self.y+i][x+j]=self.matrix[i][j]
		return self.array

class Pits():
	def __init__(self):
		self.matrix=[[] for i in range(0,4)]
		self.y=38
		self.flag=1
		self.matrix[0]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[1]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[2]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
		self.matrix[3]=['\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m','\x1b[3;34;44m'+' '+'\x1b[0m']
	def generatePits(self,array):
		self.array=array
		for x in range(10,1990,10):
			if randint(0,200) < 2:
				for i in range(0,4):
					if self.array[self.y - 1][x+i] != '\x1b[3;34;44m'+' '+'\x1b[0m':
						self.flag == 0
				if self.flag == 1:
					for i in range(0,4):
						for j in range(0,5):
							self.array[self.y+i][x+j]=self.matrix[i][j]
			self.flag=1
		return self.array
