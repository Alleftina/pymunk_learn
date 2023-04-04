import pygame
import pymunk.pygame_util
import random

pymunk.pygame_util.positive_y_is_up = False


resolution = WIDTH, HEIGHT = 900, 700
FPS = 60


pygame.init()
surface = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)


space = pymunk.Space()
space.gravity = 0, 50


segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.4
segment_shape.friction = 1.0


def create_square(space, position):
    square_side = random.randint(1, 70)
    square_mass, square_size =random.random(), (square_side, square_side)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)

    square_body.position = position
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = random.random()
    square_shape.friction = random.random()
    square_shape.color = [random.randrange(255) for i in range(4)]
    space.add(square_body, square_shape)

while True:
    surface.fill(pygame.Color('black'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            create_square(space, i.pos)
            print(i.pos)

    space.step(1/FPS)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick()