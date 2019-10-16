from Engine import Engine
from Display import Display
from Object import Object

from time import perf_counter
from time import sleep


if __name__ == "__main__":

    system = []
    sun = Object(0, 1.9885e30, 0, 0, 0, 0)
    earth = Object(1, 5.97237e24, 0, 1.49163657e11, 29.78e3, 0)
    system.append(sun)
    system.append(earth)

    sim_time = 0.1
    frame_time = 60 * 60 * 24

    display = Display()
    engine = Engine(system)

    while True:
        start = perf_counter()
        engine.process_system(frame_time)
        elapsed = perf_counter() - start
        print(elapsed)

        if elapsed < sim_time:
            sleep(sim_time - elapsed)

        display.update(engine.get_objects())
