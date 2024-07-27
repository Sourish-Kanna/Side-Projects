import turtle

loadWindow = turtle.Screen()
turtle.speed(0)
turtle.bgcolor('black')
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
for i in range(25):
    turtle.pencolor(colors[i%6])
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
        
turtle.done()
