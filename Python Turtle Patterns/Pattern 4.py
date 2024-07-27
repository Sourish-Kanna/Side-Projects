import turtle

wn = turtle.Screen()
wn.bgcolor("light green")


num_str = '5'
if num_str.isdigit():
 squares = int(num_str)
else:
   squares=0

angle = 180 - 180*(squares-2)/squares

turtle.up

x = 0
y = 0
turtle.setpos(x, y)
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
numshapes = 8
for x in range(numshapes):
 turtle.color(colors[x%6])
 x += 5
 y += 5
 turtle.forward(x)
 turtle.left(y)
 for i in range(squares):
  turtle.begin_fill()
  turtle.down()
  turtle.forward(40)
  turtle.left(angle)
  turtle.forward(40)
  turtle.up()
  turtle.end_fill()
        
turtle.done()
