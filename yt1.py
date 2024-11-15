import turtle
from turtle import*
import tkinter
from tkinter import*
import colorsys

t=turtle.Turtle()
wn=turtle.Screen()

wn.bgcolor("white")
wn.setup(height=1000,width=2090,startx=0,starty=0)

t.speed(0)
t.shape("circle")

global size
size=1
t.pensize(size)
t.shapesize(3)
def line():
	speed(0)
	up()
	ht()
	goto(-650,500)
	down()
	goto(-650,-500)
line()
def draw(x,y):
	if x<=-650:
		x=-650
	t.ondrag(None) 
	t.setheading(t.towards(x,y))
	t.goto(x,y)
	t.ondrag(draw)
	
	
def goto(x,y):
	if x<=-650:
		x=-650
	t.up()
	t.goto(x,y)
	t.down()
	
#........................
def red():
	t.color('red')
def orange():
	t.color('orange')
def yellow():
	t.color('yellow')
def green():
	t.color('green')
def blue():
	t.color('blue')
def indigo():
	t.color('indigo')
def violet():
	t.color('violet')
def black():
	t.color('black')
def white():
	t.color('white')
def cyan():
	t.color('cyan')
def green2():
	t.color('green2')
def brown():
	t.color('brown')
def gray():
	t.color('gray')			
def gold2():
	t.color('gold2')
def peachpuff():
	t.color('peach puff')
def slategray():
	t.color('slate gray')
	
			
def lawngreen():
	t.color('lawn green')
def khaki():
	t.color('khaki')
def deeppink():
	t.color('deep pink')
def NavajoWhite2():
	t.color('NavajoWhite2')
def orangered():
	t.color('orange red')
def firebrick1():
	t.color('firebrick1')
def OliveDrab1():
	t.color('OliveDrab1')
def SteelBlue1():
	t.color('SteelBlue1')
def palegreen():
	t.color('pale green')
def ivory2():
	t.color('ivory2')
def rosybrown():
	t.color('rosy brown')
def SkyBlue1():
	t.color('SkyBlue1')
def purple3():
	t.color('purple3')			
def gray59():
	t.color('gray59')
def lightyellow():
	t.color('light yellow')
def cadetblue():
	t.color('cadet blue')
				
					
								
canvas=wn.getcanvas()
button=Button(canvas.master,text='',bg='red',command=red).place(x=0,y=0,height=50,width=50) 
button=Button(canvas.master,text='',bg='orange',command=orange).place(x=50,y=0,height=50,width=50)
button=Button(canvas.master,text='',bg='yellow',command=yellow).place(x=100,y=0,height=50,width=50)
button=Button(canvas.master,text='',bg='green',command=green).place(x=150,y=0,height=50,width=50)
button=Button(canvas.master,text='',bg='blue',command=blue).place(x=200,y=0,height=50,width=50)
button=Button(canvas.master,text='',bg='indigo',command=indigo).place(x=250,y=0,height=50,width=50)
button=Button(canvas.master,text='',bg='violet',command=violet).place(x=300,y=0,height=50,width=50)
button=Button(canvas.master,text='',bg='black',command=black).place(x=0,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='white',command=white).place(x=50,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='cyan',command=cyan).place(x=100,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='green2',command=green2).place(x=150,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='brown',command=brown).place(x=200,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='gray',command=gray).place(x=250,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='gold2',command=gold2).place(x=300,y=50,height=50,width=50)
button=Button(canvas.master,text='',bg='slate gray',command=slategray).place(x=350,y=0,height=50,width=47)
button=Button(canvas.master,text='',bg='peach puff',command=peachpuff).place(x=350,y=50,height=50,width=47)

button=Button(canvas.master,text='',bg='lawn green',command=lawngreen).place(x=0,y=100,height=50,width=50) 
button=Button(canvas.master,text='',bg='khaki',command=khaki).place(x=50,y=100,height=50,width=50)
button=Button(canvas.master,text='',bg='deep pink',command=deeppink).place(x=100,y=100,height=50,width=50)
button=Button(canvas.master,text='',bg='NavajoWhite2',command=NavajoWhite2).place(x=150,y=100,height=50,width=50)
button=Button(canvas.master,text='',bg='orange red',command=orangered).place(x=200,y=100,height=50,width=50)
button=Button(canvas.master,text='',bg='firebrick1',command=firebrick1).place(x=250,y=100,height=50,width=50)
button=Button(canvas.master,text='',bg='OliveDrab1',command=OliveDrab1).place(x=300,y=100,height=50,width=50)
button=Button(canvas.master,text='',bg='SteelBlue1',command=SteelBlue1).place(x=0,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='pale green',command=palegreen).place(x=50,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='ivory2',command=ivory2).place(x=100,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='rosy brown',command=rosybrown).place(x=150,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='SkyBlue1',command=SkyBlue1).place(x=200,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='purple3',command=purple3).place(x=250,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='gray59',command=gray59).place(x=300,y=150,height=50,width=50)
button=Button(canvas.master,text='',bg='light yellow',command=lightyellow).place(x=350,y=150,height=50,width=47)
button=Button(canvas.master,text='',bg='cadet blue',command=cadetblue).place(x=350,y=150,height=50,width=47)

def reset():
	t.clear()
button=Button(canvas.master,text='reset',bg='cadet blue',command=reset).place(x=230,y=350,height=50,width=150)


def penplus():
	global size
	size+=1
	t.pensize(size)
	
def penminus():
	global size
	size-=1
	if size<0:
		size=0
	t.pensize(size)
	
button=Button(canvas.master,text='-',command=penminus).place(x=248,y=260,height=40,width=40)
button=Button(canvas.master,text='+',command=penplus).place(x=318,y=260,height=40,width=40)
pen=Label(canvas.master,text='Pensize:- ',bg='white',font=('freesansbold',7,'underline')).place(x=10,y=250)


def undo():
	t.undo()
und=Label(canvas.master,text='Undo:- ',bg='white',font=('freesansbold',7)).place(x=10,y=300)
button=Button(canvas.master,text='<<',command=undo).place(x=140,y=310,height=40,width=60)

global sx
sx=50
def square():
	global sx
	for i in range(4):
		t.fd(sx)
		t.rt(90)
def circle():
	global sx
	t.circle(sx)
def star():
	global sx
	for i in range(5):
		t.fd(sx)
		t.rt(144)
def leftarrow():
	global sx
	t.rt(104)
	t.fd(sx)
	lt(36)
	t.fd(sx)
	t.lt(68)
	t.up()
	t.fd(10)
	t.down()
	t.rt(68)
	t.bk(sx)
	t.rt(36)
	t.bk(sx)
def rightarrow():
	global sx
	t.rt(180)
	t.rt(104)
	t.fd(sx)
	lt(36)
	t.fd(sx)
	t.lt(68)
	t.up()
	t.fd(10)
	t.down()
	t.rt(68)
	t.bk(sx)
	t.rt(36)
	t.bk(sx)
def nstar():
	global sx
	for i in range(6):
		t.fd(sx)
		t.up()
		t.bk(sx)
		t.down()
		t.rt(60)
def line():
	global sx
	t.rt(90)
	t.fd(sx)
def stair():
	global sx
	for i in range(4):
		t.circle(sx,90)
		t.rt(90)
		t.fd(sx)
		t.up()
		bk(sx)
		t.down()
		t.lt(90)

sha=Label(canvas.master,text='Shape:- ',bg='white',font=('freesansbold',7)).place(x=10,y=400)
button=Button(canvas.master,text='□',command=square).place(x=10,y=450,height=60,width=60)
button=Button(canvas.master,text='○',command=circle).place(x=70,y=450,height=60,width=60)
button=Button(canvas.master,text='☆',command=star).place(x=130,y=450,height=60,width=60)
button=Button(canvas.master,text='《',command=leftarrow).place(x=190,y=450,height=60,width=60)
button=Button(canvas.master,text='》',command=rightarrow).place(x=10,y=510,height=60,width=60)
button=Button(canvas.master,text='*',command=nstar).place(x=70,y=510,height=60,width=60)
button=Button(canvas.master,text='|',command=line).place(x=130,y=510,height=60,width=60)
button=Button(canvas.master,text='¤',command=stair).place(x=190,y=510,height=60,width=60)

def shapeplus():
	global sx
	sx+=1
def shapeminus():
	global sx
	sx-=1
shapelb=Label(canvas.master,text='Shapesize:- ',bg='white',font=('freesansbold',7)).place(x=10,y=590)
button=Button(canvas.master,text='-',command=shapeminus).place(x=240,y=600,height=40,width=40)
button=Button(canvas.master,text='+',command=shapeplus).place(x=300,y=600,height=40,width=40)

global turn
turn=0
def left():
	global turn
	t.lt(turn)
def right():
	global turn
	t.rt(turn)
def turnplus():
	global turn
	turn+=5
def turnminus():
	global turn
	turn-=5
	if turn<=0:
		turn=0
	
turt=Label(canvas.master,text='Turtle direction:- ',bg='white',font=('freesansbold',7)).place(x=10,y=650)
button=Button(canvas.master,text='<<',command=left).place(x=100,y=700,height=40,width=100)
button=Button(canvas.master,text='>>',command=right).place(x=200,y=700,height=40,width=100)

button=Button(canvas.master,text='-',command=turnminus).place(x=100,y=760,height=40,width=100)
button=Button(canvas.master,text='+',command=turnplus).place(x=200,y=760,height=40,width=100)

#design
turt=Label(canvas.master,text='Design:- ',bg='white',font=('freesansbold',7)).place(x=10,y=800)

global a
global b
global c
global d
a=50
b=89
c=360
d=90
def aplus():
	global a
	a+=5
	pass
def aminus():
	global a
	a-=5
	pass
def bplus():
	global b
	b+=1
	pass
def bminus():
	global b
	b-=1
	pass
def cplus():
	global c
	c+=5
	pass
def cminus():
	global c
	c-=5
	pass
def dplus():
	global d
	d+=1
	pass
def dminus():
	global d
	d-=1
	pass

button=Button(canvas.master,text='+',command=aplus).place(x=160,y=810,height=40,width=40)
button=Button(canvas.master,text='-',command=aminus).place(x=200,y=810,height=40,width=40)
button=Button(canvas.master,text='+',command=bplus).place(x=160,y=850,height=40,width=40)
button=Button(canvas.master,text='-',command=bminus).place(x=200,y=850,height=40,width=40)
button=Button(canvas.master,text='+',command=cplus).place(x=240,y=810,height=40,width=40)
button=Button(canvas.master,text='-',command=cminus).place(x=280,y=810,height=40,width=40)
button=Button(canvas.master,text='+',command=dplus).place(x=240,y=850,height=40,width=40)
button=Button(canvas.master,text='-',command=dminus).place(x=280,y=850,height=40,width=40)


#main design

def d1():
	global a
	global b
	h=0.001
	for i in range(100):
		t.color(colorsys.hsv_to_rgb(h,1,1))
		h+=0.005
		for j in range(4):
			t.fd(a)
			t.rt(b)
		a+=1
		h+=0.005
		

def d2():
	global a
	global b
	global d
	h=0.001
	for i in range(100):
		t.color(colorsys.hsv_to_rgb(h,1,1))
		h+=0.005		
		for j in range(4):
		    t.circle(a,c)
		    t.rt(d)
		    
	
		    
def d3():
	wn.tracer(50)
	h=0
	def draw(ang,n):
	    t.circle(5+n,69)
	    t.left(ang)
	    t.circle(5+2*n,60)
	
	for i in range(100):
	    h+=0.005
	    t.color(colorsys.hsv_to_rgb(h,1,1))
	    t.up()
	    draw(90,i)
	    draw(180,i)
	    t.down()
	    draw(1/2,i-i)
	    draw(180,i/2)
	    draw(120,i-i)

def d4():
	h=0
	t.pensize(5)
	wn.tracer(100)
	for i in range(408):
		c=colorsys.hsv_to_rgb(h,1,1)
		h+=0.005
		t.goto(0,0)
		t.color(c)
		t.fd(400-i)
		t.lt(20)
		t.circle(10)
		t.rt(10)
def d5():
    global a
    t.pensize(5)
    wn.tracer(50)
    h=0

    for i in range(408):
	    c=colorsys.hsv_to_rgb(h,1,1)
	    h+=0.005
	    t.color(c)
	    t.fd(400-i)
	    t.rt(20)
	    t.circle(10)
	    t.left(40)
	    t.circle(-10)
	    t.rt(40)
	    t.bk(400-i)
	    t.rt(5)
    
def d6():
    t.pensize(5)
    wn.tracer(50)
    h=0
    for i in range(408):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.005
        t.color(c)
        t.fd((350+a)-i)
        t.rt(20)
        t.circle(10)
        t.left(130)
        t.circle(-10)
        t.rt(40)
        t.bk(400-i)
        t.rt(5)
	
def d7():
    t.pensize(7)
    wn.tracer(50)
    h=0
    a=60
    b=179
    for i in range(180):
        c=colorsys.hsv_to_rgb(h,1,1)
        h+=0.005
        t.color(c)
        t.circle(b)
        t.rt(a)
        b-=1
	
def d8():
    t.pensize(7)
    wn.tracer(50)
    h=0
    for i in range(500):
        c=colorsys.hsv_to_rgb(h,1,1)
        t.color(c)
        t.fd(100-i)
        t.rt(i**2)
        t.bk(100-i)
        h+=0.005
	
def d9():
    t.pensize(7)
    wn.tracer(50)
    h=0
    a=15
    for i in range(550):
        c=colorsys.hsv_to_rgb(h,1,1)
        t.color(c)
        h+=0.005
        t.circle(10)
        t.fd(20)
        t.rt(a)
        a+=1
	
def d10():
    t.pensize(7)
    wn.tracer(50)
    h=0
    a=15
    for i in range(250):
        c=colorsys.hsv_to_rgb(h,1,1)
        t.color(c)
        h+=0.005
        t.fd(20)
        t.rt(30)
        t.fd(a)
        t.lt(89)
        a+=1

def d11():
    t.pensize(7)
    wn.tracer(50)
    h=0
    a=15
    for i in range(10):
        a=10
        for j in range(20):
            c=colorsys.hsv_to_rgb(h,1,1)
            t.color(c)
            h+=0.005
            t.fd(20)
            t.lt(20)
            t.circle(10)
            t.fd(a)
            a+=1
	
def d12():
    t.pensize(7)
    wn.tracer(50)
    h=0
    a=20
    for i in range(25):
        for j in range(20):
            c=colorsys.hsv_to_rgb(h,1,1)
            t.color(c)
            h+=0.005
            t.fd(a)
            t.rt(120)
            t.fd(3)
            a+=1
	
def d13():
    t.pensize(7)
    wn.tracer(50)
    h=0
    a=100
    for i in range(6):
        for j in range(20):
            c=colorsys.hsv_to_rgb(h,1,1)
            t.color(c)
            h+=0.005
            t.circle(a)
            t.rt(20)
            a-=1
	
def d14():
	pass
def d15():
	pass
def d16():
	pass

#design line1
button=Button(canvas.master,text='1',command=d1).place(x=10,y=900,height=40,width=40)
button=Button(canvas.master,text='2',command=d2).place(x=50,y=900,height=40,width=40)
button=Button(canvas.master,text='3',command=d3).place(x=90,y=900,height=40,width=40)
button=Button(canvas.master,text='4',command=d4).place(x=130,y=900,height=40,width=40)
button=Button(canvas.master,text='5',command=d5).place(x=170,y=900,height=40,width=40)
button=Button(canvas.master,text='6',command=d6).place(x=210,y=900,height=40,width=40)
button=Button(canvas.master,text='7',command=d7).place(x=250,y=900,height=40,width=40)
button=Button(canvas.master,text='8',command=d8).place(x=290,y=900,height=40,width=40)

#design line2
button=Button(canvas.master,text='1',command=d9).place(x=10,y=940,height=40,width=40)
button=Button(canvas.master,text='2',command=d10).place(x=50,y=940,height=40,width=40)
button=Button(canvas.master,text='3',command=d11).place(x=90,y=940,height=40,width=40)
button=Button(canvas.master,text='4',command=d12).place(x=130,y=940,height=40,width=40)
button=Button(canvas.master,text='5',command=d13).place(x=170,y=940,height=40,width=40)
button=Button(canvas.master,text='6',command=d14).place(x=210,y=940,height=40,width=40)
button=Button(canvas.master,text='7',command=d15).place(x=250,y=940,height=40,width=40)
button=Button(canvas.master,text='8',command=d16).place(x=290,y=940,height=40,width=40)



t.ondrag(draw)
wn.onclick(goto)
wn.mainloop()
		
	
	
	
	
	
	
	
	

































		