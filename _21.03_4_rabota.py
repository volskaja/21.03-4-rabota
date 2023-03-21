from tkinter import *
from turtle import window_width
from random import * 
colors=["black",
        "cyan",
        "magenta",
        "red",
        "blue",
        "yellow",
        "green",
        "pink"]
raam2=Tk()
raam2.title("Ringid")
tahvel2=Canvas(raam2, width=600, height=600, background="black")
x0=0
y0=0
x1=600
y1=600
p=5
for i in range(55):
    x0+=p
    y0+=p
    x1-=p
    y1-=p
    tahvel2.create_oval(x0,y0,x1,y1, fill=choice(colors))
tahvel2.grid()
raam2.mainloop()