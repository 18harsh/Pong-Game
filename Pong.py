from tkinter import *
import pygame
import time
pygame.init()
class Pong:
	root = Tk()
	thisWidth = 500
	thisHeight = 500
	paddlesize = 80
	paddleabove = 30
	paddlethick = 20
	diameter = 15
	run = True
	xb = thisWidth/2
	yb = thisHeight/2
	x1 = thisWidth/2 - paddlesize/2
	y1 = thisHeight - paddleabove
	x2 = thisWidth/2 - paddlesize/2
	y2 = paddleabove
	xn = 1
	yn = 1
	vel = 10
	time = 75
	sound =	pygame.mixer.Sound("pongball.wav")
	i=0
	best = 0

	canvas=Canvas(root)
	canvas.place(x=0,y=0)


	def __init__(self,**kwargs):
		try:
			self.root.wm_iconbitmap("pong.ico")
		except:
			pass
		self.root.title("Pong")
		screenWidth = self.root.winfo_screenwidth() 
		screenHeight = self.root.winfo_screenheight() 

		try:
			self.thisWidth = kwargs['width']+15	
		except KeyError:
			pass
		try:
			self.thisHeight = kwargs['height']
		except KeyError:
			pass	
		self.canvas.config(width =self.thisWidth,height=self.thisHeight,bg='black')
		self.xb=self.thisWidth/2
		self.yb=self.thisHeight/2
		self.x1=self.thisWidth/2 - self.paddlesize/2
		self.y1=self.thisHeight - self.paddleabove
		self.x2=self.thisWidth/2 - self.paddlesize/2
		self.y2=self.paddleabove

		
		left = (screenWidth/2)-(self.thisWidth/2)
		top = (screenHeight/2)-(self.thisHeight/2)		

		self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))
			


	def draw(self):

		self.canvas.delete('all')
		paddle1 = self.canvas.create_rectangle(self.x1, self.y1, self.x1 + self.paddlesize, self.y1 + self.paddlethick,fill="red")
		paddle2 = self.canvas.create_rectangle(self.x2, self.y2, self.x2 + self.paddlesize, self.y2 + self.paddlethick,fill="red")
		ball = self.canvas.create_oval(self.xb, self.yb, self.xb + self.diameter, self.yb + self.diameter,fill="blue")
		pong.score()
		self.canvas.update()	
		self.canvas.after(self.time-self.i//2)
	def score(self):
		self.canvas.create_text(self.thisWidth-100,10, text="Score: "+str(self.i),fill="white",font=("Purisa",15))
		self.canvas.create_text(35,10, text="Best: "+str(self.best),fill="white",font=("Purisa",15))
	def gameover(self,event):
		self.canvas.create_text(self.thisWidth/2,self.thisHeight/2-50, text="Game Over",fill="white",font=("Purisa",25,'bold'))
		self.canvas.create_text(self.thisWidth/2,self.thisHeight/2, text="press enter to continue...",fill="white",font=("Purisa",15,'bold'))
		pygame.mixer.pause()	
		
	def move(self,event):
		while(self.run):
			pong.draw()
			if self.xb+self.diameter >= self.thisWidth:
				self.xn *= -1
				self.sound.play()
			if self.xb<=5:
				self.xn *= -1	
				self.sound.play()
			if (self.yb<=self.y2+self.paddlethick and self.yb+self.diameter>=self.y2+self.paddlethick) or (self.y2<=(self.yb+self.diameter/2)<=self.y2+self.paddlethick):
				if  self.x2 <= self.xb <=self.x2+self.paddlesize or self.x2<=(self.xb+self.diameter/2)<=self.x2+self.paddlesize: 	
					self.i+=1
					self.yn*=-1	
					self.sound.play()
			if (self.yb+self.diameter>=self.y1 and self.yb<self.y1) or (self.y1<=(self.yb+self.diameter/2)<=self.y1+self.paddlethick):
				if  self.x1 <= self.xb <=self.x1+self.paddlesize or self.x1<=(self.xb+self.diameter/2)<=self.x1+self.paddlesize: 	
					self.i+=1
					self.yn*=-1	
					self.sound.play()
			if self.yb+self.diameter<0:
				pong.gameover(event)
				self.run = False
			if self.yb> self.thisHeight:
				pong.gameover(event)
				self.run = False	
			self.xb+=self.vel * self.xn
			self.yb+=self.vel * self.yn	
			if event.keysym == "Left" and self.x1>0:
			   	self.x1-=self.vel+15
			   	self.x2-=self.vel +15 	
			elif event.keysym == "Right" and self.x1+self.paddlesize<self.thisWidth:
		  	   self.x1+=self.vel+15
		  	   self.x2+=self.vel+15		
			event.keysym = None	
		if event.keysym == "Return":	
			self.run = True
			if 	self.best < self.i:
				self.best = self.i	
			pong.input()  		   
	def input(self):
		self.i = 0
		self.xb = self.thisWidth/2
		self.yb = self.thisHeight/2 
		self.x1 = self.thisWidth/2 - self.paddlesize/2
		self.x2 = self.thisWidth/2 - self.paddlesize/2
		self.root.bind("<Key>", pong.move)

	def run(self):
			self.root.mainloop()	

def callable(pong):		
	pong.draw()
	pong.input()
	pong.run() 
pong = Pong(width=400,height=400)
callable(pong)


