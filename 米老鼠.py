import turtle
import time

t =turtle.Pen()
t.pensize(10)
#用于调试
#t.speed(0)

time.sleep(10)
#利用画圆函数circle来绘制米老鼠
def _circle(x,y,color,size):
    t.setheading(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(size)
    t.end_fill()


_circle(0,-200,"black",200)
_circle(200,100,"black",100)
_circle(-200,100,"black",100)
