from board import *
from mario import *
from objects import *
from getch import _getChUnix as getChar
from os import system
from time import sleep
import sys




a=board()
a.makeArray()
move = Mario()
b=Badal()
enemyList=[]
sEnemyList=[]
PtsBrk=[]
a.array=b.generateBadal(a.array)
c=Bricks()
a.array=c.generateBricks(a.array)
d=Coins()
a.array=d.generateCoins(a.array)
e=Pipe()
a.array=e.generatePipe(a.array)
f=Pits()
a.array=f.generatePits(a.array)
for x in range(50,1990,2):
	if randint(0,100) < 2:
		sEnemyList.append(smartEnemy(x))
for x in range(50,1990,2):
	if randint(0, 100) < 3:
		enemyList.append(Enemy(x))
for x in range(50,1990,2):
	if randint(0, 100) < 2:
		y=randint(27,32)
		PtsBrk.append(PointsBrick(x,y))
		a.array=PointsBrick(x,y).generateBricks(a.array)
while True:
	system('clear')
	a.array=move.spawn(a.array)
	x,y=move.sendCoords()
	d.collision(a.array,x,y)
	for i in enemyList:
		a.array=i.moveEnemies(a.array)
		returnVal=i.checkCollision(x,y)
		if returnVal == 1:
			i.clearEnemy(a.array,i.x)
			enemyList.remove(i)
	for i in sEnemyList:
		a.array=i.moveEnemies(a.array,x,y)
		returnVal=i.checkCollision(x,y)
		if returnVal == 1:
			i.clearEnemy(a.array,i.x)
			sEnemyList.remove(i)
	for i in PtsBrk:
		returnVal=i.checkCollision(x,y,a.array)
		if returnVal == 1:
			a.array=i.clearBrick(a.array)
			PtsBrk.remove(i)
	a.getPrint(move.a)
	a.array=move.moveMario(a.array)
