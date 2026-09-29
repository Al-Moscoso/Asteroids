from circleshape import CircleShape 
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        

    def update(self, dt: float) -> None:
        # must override
        self.position += self.velocity * dt


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        else:
            log_event("asteroid_split")
  
            random_angle = random.uniform(20,50) # nosec
            #new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius  / 2)
            #new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2 )
            #new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)
            #new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            #new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius  / 2)
            #new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2 )
            new_asteroid1 = pygame.math.Vector2.rotate(self.velocity, random_angle)
            new_asteroid2 = pygame.math.Vector2.rotate(self.velocity, -random_angle)
            #print(new_asteroid1.velocity)
            #print(new_asteroid2.velocity)
            

            #new_radius1 = new_asteroid1.radius - ASTEROID_MIN_RADIUS
            #new_radius2 = new_asteroid2.radius - ASTEROID_MIN_RADIUS 
            new_radius1 = self.radius - ASTEROID_MIN_RADIUS
             

            #new_asteroid3 = Asteroid(new_asteroid1.position[0], new_asteroid1.position[1], new_radius1)
            #new_asteroid3.velocity = pygame.math.Vector2(new_asteroid1.velocity, random_angle) * 1.2

            #new_asteroid4 = Asteroid(new_asteroid2.position[0], new_asteroid2.position[1], new_radius2)
            #new_asteroid4.velocity = pygame.math.Vector2(new_asteroid2.velocity, random_angle) * 1.2

            new_asteroid3 = Asteroid(self.position[0], self.position[1], new_radius1)
            new_asteroid3.velocity = new_asteroid1 * 1.2

            new_asteroid4 = Asteroid(self.position[0], self.position[1], new_radius1)
            new_asteroid4.velocity = new_asteroid2 * 1.2








