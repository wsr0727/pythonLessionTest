__author__ = 'Administrator'
#turtle.goto(坐标x,坐标y)，让海龟走到坐标的地方
#turtle.bk()当前反方向前行
#turtle.seth(度数)改变海龟行进方向
#turtle.left(度数）、turtle.right(度数）
import turtle #引入绘图库，海龟库
turtle.setup(650, 350, 200, 200)#启动窗口，设置窗体大小及位置，（宽度，高度，左上角顶点离电脑窗口左顶点坐标1，坐标2）
turtle.penup()#海龟飞起，行走轨迹不再画布上显示
turtle.fd(-250)#向前走
turtle.pendown()#海龟落下，行走规矩在画布上重新显示
turtle.pensize(25)#海龟宽度，也可以用turtle.width(width)
turtle.pencolor("purple")#RGB颜色
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)#让海龟向左侧的一个点为圆心曲线运行
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40*2/3)
turtle.done()
