import pygame
import pgzrun
from random import randint

TITLE = "bouncyball"
HEIGHT = 600
WIDTH = 800
GRAVITY = 1600

class Ball():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        R = randint(0,255)
        G = randint(0,255)
        B = randint(0,255)
        self.colour = (R,G,B)
        self.vx = 200
        self.vy = 0
    def display(self): 
         pos = (self.x, self.y)
         screen.draw.filled_circle(pos, self.radius, self.colour)

ball = Ball(16, 16, 16)

def draw():
    screen.clear()
    ball.display()

def update(dt): # delta time- very small time duration
        
    # Apply constant acceleration formulae    
    uy = ball.vy # uy = current vertical velocity of ball
    ball.vy += GRAVITY * dt #(v=u+at) ball's vertical velocity increases due to the acc. of gravity 
    ball.y += (uy + ball.vy) * 0.5 * dt #(s = ut + 1/2 at^2)  - calculate avg. velocity over the time interval dt
    # detect and handle bounce
    if ball.y > HEIGHT - ball.radius:  # we've bounced!
        ball.y = HEIGHT - ball.radius  # fix the position
        ball.vy = -ball.vy * 0.9  # inelastic collision
    # X component doesn't have acceleration
    ball.x += ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx

def on_key_down(key):
    """Pressing a key will kick the ball upwards."""
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()