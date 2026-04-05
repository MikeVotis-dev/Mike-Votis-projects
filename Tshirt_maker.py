import math
import turtle


class Tshirt:
    def __init__(self):
        print("Welcome to the T-shirt generator!\n")

        self.shirt_color = input("What color do you want your T-shirt to be? ")
        self.logo_color = input("What color do you want the text to be? ")
        self.text = input("What name do you want to write? ")

        self.screen = turtle.Screen()
        self.screen.setup(640, 720)
        self.screen.bgcolor("white")
        self.screen.title("T-shirt Generator")

        self.t = turtle.Turtle()
        self.t.hideturtle()
        self.t.speed(10)
        self.t.pensize(2.5)
        self.t.color("black")

    def pu(self, x, y):
        self.t.penup()
        self.t.goto(x, y)

    def dashed_line(self, x1, y1, x2, y2, dash=6, gap=4):
        length = math.hypot(x2 - x1, y2 - y1)
        if length == 0:
            return

        dx = (x2 - x1) / length
        dy = (y2 - y1) / length
        pos = 0.0
        draw_part = True

        self.pu(x1, y1)
        while pos < length:
            step = min(dash if draw_part else gap, length - pos)
            if draw_part:
                self.t.pendown()
            else:
                self.t.penup()

            self.t.goto(x1 + dx * (pos + step), y1 + dy * (pos + step))
            pos += step
            draw_part = not draw_part

        self.t.penup()

    def draw_daisy(self, cx, cy):
        self.t.pensize(1)
        self.t.pencolor("black")

        for deg in range(0, 360, 45):
            rad = math.radians(deg)
            px = cx + 9 * math.cos(rad)
            py = cy + 9 * math.sin(rad)
            self.pu(px, py - 5)
            self.t.pendown()
            self.t.fillcolor("white")
            self.t.begin_fill()
            self.t.circle(5)
            self.t.end_fill()

        self.pu(cx, cy - 6)
        self.t.pendown()
        self.t.fillcolor("yellow")
        self.t.begin_fill()
        self.t.circle(6)
        self.t.end_fill()
        self.t.penup()

    def draw_shirt(self):
        bw = 140
        by = -195
        sty = 135
        sby = 52
        sox = 250
        crx = 72
        cry = 36

        self.t.pencolor("black")
        self.t.fillcolor(self.shirt_color)
        self.t.begin_fill()

        self.pu(-bw, by)
        self.t.pendown()

        self.t.goto(bw, by)
        self.t.goto(bw, sby)

        self.t.setheading(0)
        self.t.forward(sox - bw)
        self.t.setheading(90)
        self.t.forward(sty - sby)
        self.t.setheading(180)
        self.t.forward(sox - bw)

        self.t.goto(crx, sty)

        for i in range(181):
            a = math.radians(i)
            self.t.goto(crx * math.cos(-a), sty + cry * math.sin(-a))

        self.t.goto(-bw, sty)

        self.t.setheading(180)
        self.t.forward(sox - bw)
        self.t.setheading(270)
        self.t.forward(sty - sby)
        self.t.setheading(0)
        self.t.forward(sox - bw)

        self.t.goto(-bw, by)
        self.t.end_fill()
        self.t.penup()

        self.t.pensize(1.3)
        for i in range(181):
            a = math.radians(i)
            x = (crx - 6) * math.cos(-a)
            y = (sty - 7) + (cry - 9) * math.sin(-a)
            if i == 0:
                self.pu(x, y)
            if (i // 6) % 2 == 0:
                self.t.pendown()
            else:
                self.t.penup()
            self.t.goto(x, y)
        self.t.penup()

        self.dashed_line(-sox + 9, sby + 4, -sox + 9, sty - 4)
        self.dashed_line(sox - 9, sby + 4, sox - 9, sty - 4)

        self.t.pensize(2)
        self.pu(-bw, by + 22)
        self.t.pendown()
        self.t.goto(bw, by + 22)
        self.t.penup()

        self.t.pensize(1.3)
        self.dashed_line(-bw + 5, by + 36, bw - 5, by + 36)

        self.t.pensize(1.5)
        lx = sox - 26
        ly = (sby + sty) / 2 - 10
        self.pu(lx, ly)
        self.t.pendown()
        for _ in range(2):
            self.t.forward(16)
            self.t.left(90)
            self.t.forward(20)
            self.t.left(90)
        self.t.penup()

        self.draw_daisy(-bw + 65, by + 52)

    def draw_text(self):
        self.t.pencolor(self.logo_color)
        self.pu(0, 20)
        self.t.write(self.text, align="center", font=("Arial", 22, "bold"))

    def run(self):
        self.draw_shirt()
        self.draw_text()
        turtle.done()


my_shirt = Tshirt()
my_shirt.run()
