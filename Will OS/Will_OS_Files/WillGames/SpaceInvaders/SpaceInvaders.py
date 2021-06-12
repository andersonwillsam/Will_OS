# Space Invaders
import turtle
import os
import math
import random

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

# Draw Border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.goto(-300, -300)
border_pen.pensize(3)
border_pen.pendown()
for i in range(4):
    border_pen.forward(600)
    border_pen.left(90)
border_pen.hideturtle()

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# Create the turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)

playerspeed = 15

number_of_enemies = 5
enemies = []

for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.goto(x, y)

enemyspeed = 2

# Create the players bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"


# Move player left and right

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # Move the bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.goto(x,y)
        bullet.showturtle()
    
def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False
    
# Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main Game Loop
while True:

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        # Move the enemy back and down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.goto(0,-400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.goto(x, y)
            score += 10
            scorestring = "Score: %s"%score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
            score_pen.hideturtle()


        if isCollision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break        

    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"

    


turtle.done()
