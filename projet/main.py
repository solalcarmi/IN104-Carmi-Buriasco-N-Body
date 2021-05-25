#!/usr/bin/env python3

from simulator import Simulator, World, Body
from simulator.utils.vector import Vector2
from simulator.solvers import RK4
from simulator.physics.engine import DummyEngine
from simulator.graphics import Screen

import pygame as pg

if __name__ == "__main__":
    b1 = Body(Vector2(0, 4),
              velocity=Vector2(0.1, 0),
              mass=100,
              draw_radius=5)
    b2 = Body(Vector2(0, 100),
              velocity=Vector2(0.05, 0),
              mass=50,
              draw_radius=5, color=(0, 255, 0))
    b3 = Body(Vector2(0.05, 50),
              velocity=Vector2(0, 0.1),
              mass=50,
              draw_radius=5, color=(255, 0, 0))


    world = World()
    world.add(b1)
    world.add(b2)
    world.add(b3)

    simulator = Simulator(world, DummyEngine, RK4)

    screen_size = Vector2(800, 600)
    screen = Screen(screen_size,
                    bg_color=(0, 0, 0),
                    caption="Simulator")
    screen.camera.scale = 1

    # this coefficient controls the speed
    # of the simulation
    time_scale = 10

    simulator.solver.max_step_size = time_scale / 100

    print("Start program")
    while not screen.should_quit:
        dt = screen.tick(60)

        # simulate physics
        delta_time = time_scale * dt / 1000
        simulator.step(delta_time)
        #simulator.check_for_collisions()

        # read events
        screen.get_events()

        # handle events
        #   scroll wheel
        if screen.get_wheel_up():
            screen.camera.scale *= 1.1
        elif screen.get_wheel_down():
            screen.camera.scale *= 0.9

        # draw current state
        screen.draw(world)

        # draw additional stuff
        screen.draw_corner_text("Time: %f" % simulator.t)

        # show new state
        screen.update()

    screen.close()
    print("Done")
