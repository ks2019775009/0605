import turtle as t # 2019775009 김수민

draw_action = 1

oldx = 0
oldy = 0

def new_clear():
    global draw_action
    global oldx
    global oldy
    t.clear()
    t.pensize(1)
    t.pendown()
    draw_action = 1
    oldx = 0
    oldy = 0
def draw(x,y):
    global oldx
    global oldy

    if draw_action == 1:
        t.goto(x,y)
        oldx = x
        oldy = y
    elif draw_action == 2:
        t.goto(x,oldy)
        t.goto((x+oldx)//2, y)
        t.goto(oldx, oldy)
    elif draw_action ==3:
        t.goto(x, oldy)
        t.goto(x, y)
        t.goto(oldx, y)
        t.goto(oldx, oldy)
    elif draw_action == 4:
        t.circle(-((x-oldx)//2))
def drag(x, y):
    if draw_action == 1:
        draw(x,y)
def move(x, y):
    global oldx
    global oldy
    penstatus = t.isdown()
    t.penup()
    t.goto(x, y)
    if penstatus == True:
        t.pendown()
    oldx = x
    oldy = y

def Key_l():
    global draw_action
    draw_action = 1
def Key_t():
    global draw_action
    draw_action = 2
def Key_r():
    global draw_action
    draw_action = 3
def Key_c():
    global draw_action
    draw_action = 4
def Key_n():
    new_clear()
def Key_u():
    t.penup()
def Key_d():
    t.pendown()
def Key_1():
    t.pensize(1)
def Key_2():
    t.pensize(3)
def Key_5():
    t.pensize(5)

t.setup(600,600)
s = t.Screen()
t.shapesize(2)
t.speed(0)
t.left(90)
new_clear()
t.ondrag(drag)
s.onkey(Key_l, "l")
s.onkey(Key_t, "t")
s.onkey(Key_r, "r")
s.onkey(Key_c, "c")
s.onkey(Key_n, "n")
s.onkey(Key_u, "u")
s.onkey(Key_d, "d")
s.onkey(Key_1, "1")
s.onkey(Key_2, "2")
s.onkey(Key_5, "5")
s.onscreenclick(draw, 1)
s.onscreenclick(move, 3)
s.listen()

