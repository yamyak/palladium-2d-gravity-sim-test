from Engine import Engine
from Display import Display
from Object import Object

from time import perf_counter
from time import sleep


if __name__ == "__main__":

    system = []
    sun = Object(0, 1.9885e30, 0, 0, 0, 0)
    earth = Object(1, 5.9722e24, 0, 1.49163657e11, 29.78e3, 0)
    system.append(sun)
    system.append(earth)

    sim_time = 0.001
    frame_time = 60 * 60

    display = Display()
    engine = Engine(system)

    frame = 0
    while True:
        start = perf_counter()
        engine.process_system(frame_time)
        elapsed = perf_counter() - start

        if frame % 2160 == 0:
            print(str(frame) + " : " + str(earth.get_velocity()[0]) + ", " + str(earth.get_velocity()[1]))

        if elapsed < sim_time:
            sleep(sim_time - elapsed)

        display.update(engine.get_objects())
        frame += 1
