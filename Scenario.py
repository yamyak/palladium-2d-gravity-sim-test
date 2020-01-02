from Engine import Engine
from Display import Display
from Object import Object

from time import perf_counter
from time import sleep


if __name__ == "__main__":
    # minimum real world time each frame must be
    sim_time = 0.0
    # simulation frame time in seconds (amount of time 1 frame is)
    frame_time = 60 * 60
    # pygame screen size in pixels
    screen_size = 1000
    # simulation space size loaded into screen size
    space_size = 60e11

    # initialize solar system objects
    # solar system objects initialized with data from: https://ssd.jpl.nasa.gov/horizons.cgi?
    system = []
    sun = Object(0, "Sun", 1.9885e30, 0, 0, 0, 0)
    mercury = Object(1, "Mercury", 3.302e23, -2.105262111032039e10, -6.640663808353403e10, 3.665298706393840e4,
                     -1.228983810111077e4)
    venus = Object(2, "Venus", 48.685e23, -1.075055502695123e11, -3.366520720591562e9, 8.891598046362434e2,
                   -3.515920774124290e4)
    earth = Object(3, "Earth", 5.97237e24, -2.521092863852298e10, 1.449279195712076e11, -2.983983333368269e4,
                   -5.207633918704476e3)
    moon = Object(4, "Moon", 7.349e22, -2.552857888050620e10, 1.446860363961675e11, -2.927904627038706e4,
                  -6.007566180814270e3)
    mars = Object(5, "Mars", 6.4171e23, 2.079950549908331e11, -3.143009561106971e9, 1.295003532851602e3,
                  2.629442067068712e4)
    ceres = Object(6, "Ceres", 9.3835e20, -3.556734767233869e11, 1.197945446667982e11, -6.242631825543756e3,
                   -1.831679381403535e4)
    jupiter = Object(7, "Jupiter", 1898.13e24, 5.989091595026654e11, 4.391225931434094e11, -7.901937631606453e3,
                     1.116317697592017e4)
    saturn = Object(8, "Saturn", 5.6834e26, 9.587063372677683e11, 9.825652108592927e11, -7.428885682764759e3,
                    6.738814239440629e3)
    uranus = Object(9, "Uranus", 86.813e24, 2.158774703477132e12, -2.054825231595053e12, 4.637648411798546e3,
                    4.627192877193521e3)
    neptune = Object(10, "Neptune", 102.413e24, 2.514853503350991e12, -3.738847517955682e12, 4.465802576076253e3,
                     3.075682494272277e3)
    pluto = Object(11, "Pluto", 1.307e22, -1.477558339934327e12, -4.182460438550376e12, 5.261925689692920e3,
                   -2.648919644838698e3)

    # load all objects into simulation engine
    system.append(sun)
    system.append(mercury)
    system.append(venus)
    system.append(earth)
    system.append(moon)
    system.append(mars)
    system.append(ceres)
    system.append(jupiter)
    system.append(saturn)
    system.append(uranus)
    system.append(neptune)
    system.append(pluto)

    # initialize the display and the simulation engine
    display = Display(screen_size, space_size)
    engine = Engine(system)

    # each iteration of loop runs through 1 simulation frame
    frame = 0
    while True:
        # initialize real world frame timer
        start = perf_counter()
        # process 1 frame of simulation given amount of simulation time frame should be
        engine.process_system(frame_time)
        # calculate how long frame took in real world time
        elapsed = perf_counter() - start

        # code to print out frame data
        # print(str(frame) + " : " + str(earth.get_velocity()[0]) + ", " + str(earth.get_velocity()[1]))
        # print(str(frame) + " : " + str(elapsed))

        # if real world frame time is less than minimum value, sleep until minimum time reached
        if elapsed < sim_time:
            sleep(sim_time - elapsed)

        # update the display with new positions
        display.update(engine.get_objects())

        frame += 1
