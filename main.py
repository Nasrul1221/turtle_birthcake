import turtle

w = turtle.Screen()
w.bgcolor('black')
t = turtle.Turtle()
t.hideturtle()

width_cake = 49
length_cake = 410

width_bt = 7
length_bt = 410

def sq():
    t.setposition(-220, -135)
    width = 5
    length = 450
    t.color('white')
    t.fillcolor('white')
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.left(90)
        t.forward(width)
        t.left(90)
    t.end_fill()

def part0_cake():
    t.penup()
    t.goto(-200, -129)
    t.pendown()

    t.color('goldenrod')
    t.fillcolor('goldenrod')
    t.begin_fill()
    t.setheading(90)

    for i in range(2):
        t.forward(width_cake)
        t.right(90)
        t.forward(length_cake)
        t.right(90)
    t.end_fill()

def betw0():
    t.penup()
    t.goto(-200, -80)
    t.pendown()

    t.color('peachpuff')
    t.fillcolor('peachpuff')
    t.begin_fill()

    for i in range(2):
        t.forward(width_bt)
        t.right(90)
        t.forward(length_bt)
        t.right(90)
    t.end_fill()

def part1_cake():
    t.penup()
    t.goto(-200, -72)
    t.pendown()

    t.color('goldenrod')
    t.fillcolor('goldenrod')
    t.begin_fill()

    for i in range(2):
        t.forward(width_cake)
        t.right(90)
        t.forward(length_cake)
        t.right(90)
    t.end_fill()

def betw1():
    t.penup()
    t.goto(-200, -23)
    t.pendown()

    t.color('peachpuff')
    t.fillcolor('peachpuff')
    t.begin_fill()

    for i in range(2):
        t.forward(width_bt)
        t.right(90)
        t.forward(length_bt)
        t.right(90)
    t.end_fill()

def part2_cake():
    t.penup()
    t.goto(-200, -15)
    t.pendown()

    t.color('goldenrod')
    t.fillcolor('goldenrod')
    t.begin_fill()

    for i in range(2):
        t.forward(width_cake)
        t.right(90)
        t.forward(length_cake)
        t.right(90)
    t.end_fill()

def drip(x, y, drip_length):
    t.speed(50)
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color('firebrick')
    t.fillcolor('firebrick')
    t.begin_fill()

    t.setheading(-90)
    t.circle(drip_length, 180)

    t.end_fill()

def candles(x, y, candle_color):
    t.speed(15)
    t.setheading(90)
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.color(candle_color)
    t.fillcolor(candle_color)
    t.begin_fill()

    height = 50
    width = 7
    for i in range(2):
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

    #fire for candles
    t.penup()
    t.goto(x + 3, y + height + 3)
    t.pendown()

    t.color('orange')
    t.fillcolor('orange')
    t.begin_fill()

    t.setheading(35)
    t.circle(10, 120)
    t.setheading(-140,)
    t.circle(10, 120)
    t.end_fill()

    #center of a candle
    t.penup()
    t.goto(x + 2, y + height + 6)
    t.pendown()

    t.color('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(3)
    t.end_fill()

def write_text():
    t.setheading(90)
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.color('pink')
    t.write('Happy Birthday', align='center', font=("Georgia", 50, 'bold'))

sq()
part0_cake()
betw0()
part1_cake()
betw1()
part2_cake()
drip(-200, 34, 15)
drip(-171, 34, 20)
drip(-137, 34, 13)
drip(-115, 34, 20)
drip(-85, 34, 15)
drip(-60, 34, 13)
drip(-40, 34, 22)
drip(-2, 34, 14)
drip(20, 34, 15)
drip(43, 34, 20)
drip(80, 34, 11)
drip(100, 34, 18)
drip(129, 34, 16)
drip(157, 34, 18)
drip(190, 34, 10)
candles(-180, 35, 'dodgerblue')
candles(-120, 35, 'mediumseagreen')
candles(-60, 35, 'turquoise')
candles(0, 35, 'hotpink')
candles(60, 35, 'gold')
candles(120, 35, 'mediumorchid')
candles(180, 35, 'limegreen')
write_text()

turtle.done()
