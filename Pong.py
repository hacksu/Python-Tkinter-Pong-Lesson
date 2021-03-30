from tkinter import *

import random

class Window:

    def __init__(self):

        self.window = Tk();
        self.window.geometry("800x600")

        self.canvas = Canvas(self.window,width=800,height=600)
        self.canvas.config(background="black")
        #self.canvas.pack(fill = BOTH, expand=True)
        self.canvas.pack()

        self.humPaddle = [50,300]
        self.comPaddle = [750,300]

        self.comDirection = "down"

        self.ball = [400,300]
        self.ballVel = [random.choice([-4,-3,-2,-1]),random.randint(0,0)]

        self.window.update()

        self.window.bind("<Up>",self.up)
        self.window.bind("<Down>",self.down)

        self.MainLoop()
        self.window.mainloop()

    def up(self,event):
        self.humPaddle[1] -= 10
        if(self.humPaddle[1] < 50):
            self.humPaddle[1] = 50

    def down(self,event):
        self.humPaddle[1] += 10
        if(self.humPaddle[1] > 550):
            self.humPaddle[1] = 550

    def MainLoop(self):

        self.canvas.delete("paddle","ball")

        self.canvas.create_rectangle(self.humPaddle[0]-10,self.humPaddle[1]-50,
                                     self.humPaddle[0]+10,self.humPaddle[1]+50,
                                     fill="white",tag = "paddle")
        self.canvas.create_rectangle(self.comPaddle[0]-10,self.comPaddle[1]-50,
                                     self.comPaddle[0]+10,self.comPaddle[1]+50,
                                     fill="white",tag = "paddle")

        self.canvas.create_oval(self.ball[0]-5,self.ball[1]-5,self.ball[0]+5,
                                self.ball[1]+5,
                                fill = "white",tag = "ball")


        self.ball[0] += self.ballVel[0]
        self.ball[1] += self.ballVel[1]

        if(self.comDirection == "up"):
            self.comPaddle[1] += 5
            if(self.comPaddle[1] > 550):
                self.comDirection = "down"
                self.comPaddle[1] = 550
        else:
            self.comPaddle[1] -= 5
            if(self.comPaddle[1] < 50):
                self.comDirection = "up"
                self.comPaddle[1] = 50

        
        if(self.ball[1] < 0+5): # Ceiling
            self.ballVel[1] = abs(self.ballVel[1])
        elif(self.ball[1] > 600-5): # Floor
            self.ballVel[1] = -abs(self.ballVel[1])

        if(self.ball[0] < 0 or self.ball[0] > 800): #Paddles missed
            self.ball = [400,300]
            self.ballVel = [random.choice([-4,-3,-2,-1]),random.randint(-7,7)]
        

        # Human Paddle
        if(self.ball[0] > self.humPaddle[0]-10 and self.ball[0] < self.humPaddle[0] + 10 and
           self.ball[1] > self.humPaddle[1]-50 and self.ball[1] < self.humPaddle[1] + 50):
            self.ball[0] = self.humPaddle[0]+15
            self.ballVel[0] = abs(self.ballVel[0])+1

        if(self.ball[0] > self.comPaddle[0]-10 and self.ball[0] < self.comPaddle[0] + 10 and
           self.ball[1] > self.comPaddle[1]-50 and self.ball[1] < self.comPaddle[1] + 50):
            self.ball[0] = self.comPaddle[0]-15
            self.ballVel[0] = -abs(self.ballVel[0])-1
        
        
        self.window.after(10,self.MainLoop)

Window()
        
