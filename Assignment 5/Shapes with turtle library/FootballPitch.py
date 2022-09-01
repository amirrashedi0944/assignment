import turtle
leonardo = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("Green")
leonardo.speed(2)
for i in range(1, 5):
    if i % 2 != 0:
        leonardo.forward(300)
        leonardo.left(90)
    else:
        leonardo.forward(180)
        leonardo.left(90)
print(leonardo.pos())
leonardo.penup()
leonardo.goto(150, 0)
leonardo.left(90)
leonardo.pos()
leonardo.pendown()
leonardo.forward(180)
leonardo.penup()
leonardo.goto(180, 90)
leonardo.pendown()
leonardo.circle(30, 360, 50)
leonardo.penup()
corners = [[10, 0], [300, 10], [290, 180], [0, 170]]
for x, y in corners:
    leonardo.goto(x, y)
    leonardo.pendown()
    leonardo.circle(10, 90)
    leonardo.penup()
leonardo.goto(151, 90)
leonardo.pendown()
leonardo.circle(1)
leonardo.penup()
penaltyArea = [[0, 45], [0, 55], [300, 135], [300, 125]]
counter = 1
for x, y in penaltyArea:
    leonardo.goto(x, y)
    leonardo.pendown()
    leonardo.right(90)
    if counter % 2 == 0:
        leonardo.forward(18)
        leonardo.left(90)
        leonardo.forward(70)
        leonardo.left(90)
        leonardo.forward(18)
        leonardo.left(90)
    else:
        leonardo.forward(45)
        leonardo.left(90)
        leonardo.forward(90)
        leonardo.left(90)
        leonardo.forward(45)
        leonardo.right(90)
    leonardo.penup()
    counter += 1
leonardo.goto(45, 70)
leonardo.pendown()
leonardo.right(90)
leonardo.circle(20, 180)
leonardo.penup()
leonardo.goto(255, 110)
leonardo.pendown()
leonardo.circle(20, 180)
leonardo.penup()
goals = [[0, 80], [300, 100]]
for x, y in goals:
    leonardo.goto(x, y)
    leonardo.pendown()
    leonardo.right(180)
    leonardo.forward(5.5)
    leonardo.right(90)
    leonardo.forward(20)
    leonardo.right(90)
    leonardo.forward(5.5)
    leonardo.right(180)
    leonardo.penup()
window.mainloop()
