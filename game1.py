import turtle 
import random
window=turtle.Screen()
window.title("Космічні перегони")
window.bgcolor("black")
window.setup(width=600,height=600)
player=turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.goto(0,-250)

def move_left():
    x = player.xcor()
    x = x - 20
    if x > -280:
        player.setx(x)

def move_right(): 
    x = player.xcor()
    x = x+20
    if x<280:
        player.setx (x)

window.listen()
window.onkeypress(move_left,"Left")
window.onkeypress(move_right,"Right")
meteor = turtle.Turtle()
meteor.shape("circle")
meteor.color("red")
meteor.penup()
meteor_x = random.randint(-250, 250)
meteor.goto(meteor_x, 250)
meteor_speed = 2

game_runs = True
while game_runs:
    y = meteor.ycor()
    meteor.sety(y - meteor_speed)

    if meteor.ycor() < -280:
        y < -280
        meteor_x = random.randint(-250,250)
        meteor.goto(meteor_x,250)
        meteor_speed = meteor_speed + 1

    if player.distance(meteor) < 20:
        print("Game over")
        game_over = turtle.Turtle()
        game_over.color("white")
        game_over.penup()
        game_over.hideturtle()
        game_over.write("GAME OVER",align = "center",font = ("Arial", 30, "bold"))
        game_runs = False
        break