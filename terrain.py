import numpy as np
import matplotlib.pyplot as plt

def get_basic_terrain(sample=1000,std = 3):
    x = np.arange(0, sample, 1)
    terrain = x 
    return terrain.reshape(1,sample)

def get_sine_terrain(size=100,sample=1000,f=2):
    Fs = size
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    
    return y.reshape(1,sample)

def get_basic_terrain_descending(sample=1000):
    x = np.arange(sample,0, -1)
    terrain = x 

    return terrain.reshape(1,sample)


def get_parabola(sample = 1000,a=2,b=4):
    
    x= np.arange(-sample/2,sample/2)
    y = a*x*x + b*x

    terrain =  y
    
    return terrain.reshape(1,sample)

def get_random_terrain(sample = 1000):
    a = 0
    for i in range(100):
        a = a + np.random.randint(-3,3,1)*get_sine_terrain(sample/10,sample = sample,f = np.random.normal(1,2)/10)

    terrain = a/100
    return terrain.reshape(1,sample)

def get_noise(sample = 1000,std=3):
    noise = np.random.normal(scale=std, size=[1, sample])
    return noise



from tkinter import *
import numpy as np

class PaintBox( Frame ):
    def __init__( self ):
        Frame.__init__( self )
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "A simple paint program" )
        self.master.geometry( "1000x600" )

        self.message = Label( self, text = "Drag the mouse to draw" )
        self.message.pack( side = BOTTOM )
        self.points = []
      
      # create Canvas component
        self.myCanvas = Canvas( self )
        self.myCanvas.pack( expand = YES, fill = BOTH )

      # bind mouse dragging event to Canvas
        self.myCanvas.bind( "<B1-Motion>", self.paint )

    def paint( self, event ):
        x1, y1 = ( event.x - 4 ), ( event.y - 4 )
        x2, y2 = ( event.x + 4 ), ( event.y + 4 )
        self.myCanvas.create_oval(x1, y1, x2, y2, fill = "red" )
        x = (x1+x2)/2
        y = (y1+y2)/2
        self.points.append([x,y])
        
   
    def main():
        PaintBox().mainloop()
        
        
def get_drawing():
    paint = PaintBox()

    paint.mainloop()

    points = np.array(paint.points)

    return 600 - points[:,1].reshape(1,points.shape[0])




    