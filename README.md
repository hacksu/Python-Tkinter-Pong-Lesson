# Python-Tkinter-Pong-Lesson
## Intro
For this lesson, all you need to download is Python 3. Any version will do, but the latest verison of Python is recommended. You can download Python from [here](python.org).
## Creating the code
Create a new Python file. You can name it whatever you wish, but we recommend something like Pong.py.

We'll need to start by importing the libraries we will need in-order to create our game. We will start by adding the two lines
```
from tkinter import *
import random
```
The random library is used to place our ball randomly so that each bout is slightly different. We import * from tkinter, as this allows us to use all of tkinter's functions and variables without putting "tkinter." in front of it.

We will start by creating a class to hold our game
```
class Window:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("800x600")
        
        self.window.mainloop()
        
Window()
```
If you run this code, you should see a small window containing nothing pop up. The first line of the class defines our window, the second line sizes the window to be 800px x 600px, and the last loop starts the window's "mainloop", which handles things such as input, redrawing, etc.

We can't currently  do anything with this window, so let's add a canvas to it. Inside the init function, below the geometry line, add
```
self.canvas = Canvas(self.window,width=800,height=800)
self.canvas.config(background="black")
self.canvas.pack()
```
This bit of code creates a canvas which allows us to draw shapes and images. We tell the canvas to match the size of the window, make its background pitch black, and then insert it into the window.

We are now going to create the information that we will need to draw the paddles and the ball
```
self.humPaddle = [50,300]
self.comPaddle = [750,300]

self.comDirection = "down"

self.ball = [400,300]
```
These values will hold the coords of where the paddles and ball are on the screen.

This is all well and good, but a game isn't anything if you can't see it, so lets create the function that will draw our game.

In the class, create the following function
```
def MainLoop(self):
    self.canvas.delete("paddle","ball")
    self.canvas.create_rectangle(self.humPaddle[0]-10,self.humPaddle[1]-50,
                                 self.humPaddle[0]+10,self.humPaddle[1]+50,
                                 fill="white",tag = "paddle")
    self.canvas.create_rectangle(self.comPaddle[0]-10,self.comPaddle[1]-50,
                                     self.comPaddle[0]+10,self.comPaddle[1]+50,
                                     fill="white",tag = "paddle")

    self.canvas.create_oval(self.ball[0]-5,self.ball[1]-5,
                            self.ball[0]+5,self.ball[1]+5,
                            fill = "white",tag = "ball")
                            
    self.window.after(10,self.MainLoop)
```
Here, we first start by deleting the paddles and ball from the canvas if they exist. This prevents our ball and paddles from leaving a streak across the screen as they move. We then draw the paddles and ball using their coordinates. The last line tells the window to re-run the function after 10 milliseconds, which is why it is called the main loop.
Our ball can't move yet, so let's fix that. Up in the init function, add `self.ballVel = [random.choice([-4,-3,-2,-1]),random.randint(-7,7)]` This will give our ball a random direction and speed to move in. Now, in the MainLoop function, add
```
self.ball[0] += self.ballVel[0]
self.ball[1] += self.ballVel[1]
```
This will change the coordinates of the ball using the velocity. Now if we run the code, the ball will bounce around the screen, but it will just fly off and not stay on our window. We can fix this by adding some more code to our MainLoop
```
if(self.ball[1] < 0+5): # Ceiling
    self.ballVel[1] = abs(self.ballVel[1])
elif(self.ball[1] > 600-5): # Floor
    self.ballVel[1] = -abs(self.ballVel[1])

if(self.ball[0] < 0 or self.ball[0] > 800): #Paddles missed
    self.ball = [400,300]
    self.ballVel = [random.choice([-4,-3,-2,-1]),random.randint(-7,7)]
```
If the ball hits the ceiling or the floor, the ball will reverse direction, and if it goes behind a paddle, it will reset to the center with a new velocity.

Now we need to make the paddles move. To make the computer's paddle move, we simply need to add
```
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
```
Now the computer's paddle will bounce around the screen. The player's paddle is a bit more complicated though.
In the init function, we need to add the following 2 lines
```
self.window.bind("<Up>",self.up)
self.window.bind("<Down>",self.down)
```
The bind function will bind some kinnd of event to the provided function. You can bind things like mouse scroll, mouse click, button press, etc. In this case, we bind a function to the Up and Down Arrow Keys. The two functions look like this
```
def up(self,event):
    self.humPaddle[1] -= 10
    if(self.humPaddle[1] < 50):
        self.humPaddle[1] = 50

def down(self,event):
    self.humPaddle[1] += 10
    if(self.humPaddle[1] > 550):
        self.humPaddle[1] = 550
```
Now, whenever you press the up or down arrow keys, your paddle will move. The last step is to make the ball bounce off of the paddles. Go back down to your MainLoop function and add this last bit
```
if(self.ball[0] > self.humPaddle[0]-10 and self.ball[0] < self.humPaddle[0] + 10 and
    self.ball[1] > self.humPaddle[1]-50 and self.ball[1] < self.humPaddle[1] + 50):
    self.ball[0] = self.humPaddle[0]+15
    self.ballVel[0] = abs(self.ballVel[0])+1
    
if(self.ball[0] > self.comPaddle[0]-10 and self.ball[0] < self.comPaddle[0] + 10 and
    self.ball[1] > self.comPaddle[1]-50 and self.ball[1] < self.comPaddle[1] + 50):
    self.ball[0] = self.comPaddle[0]-15
    self.ballVel[0] = -abs(self.ballVel[0])-1
```
Whenever the ball goes inside the paddle, the ball is shifted back out, it's velocity is reversed and its speed is raised.

Pong should now be working, but its missing a bunch of features, like a score count. Can you add more features to this?
