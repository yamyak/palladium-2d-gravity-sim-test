from Object import Object


class Engine:

    # initialize simulation engine gravity and objects
    def __init__(self, system):
        self.__G = 6.67408e-11
        self.__system = system

    def get_objects(self):
        return self.__system

    # process 1 frame of simulation
    def process_system(self, frame_time):
        # iterate through all objects in system
        for obj in self.__system:
            # calculate new position and velocity of object after simulation frame time has passed
            # does not update location since all object locations depend on all other object locations
            self.calculate_runge_kutta_integrator(obj, frame_time)

        # iterate through all objects in system
        # update locations with values calculated in previous loop
        for obj in self.__system:
            obj.commit_location()

    # applied the runge kutta integrator algorithm to find new location and velocity of object
    # algorithm can be found here: https://sites.temple.edu/math5061/files/2016/12/final_project.pdf
    def calculate_runge_kutta_integrator(self, obj, frame_time):
        x, y = obj.get_location()

        k1x, k1y = obj.get_velocity()

        k1vx, k1vy = self.calculate_total_acceleration(obj.get_id(), x, y)

        k2x = k1x + frame_time * k1vx / 2
        k2y = k1y + frame_time * k1vy / 2

        tx = x + frame_time * k1x / 2
        ty = y + frame_time * k1y / 2
        k2vx, k2vy = self.calculate_total_acceleration(obj.get_id(), tx, ty)

        k3x = k1x + frame_time * k2vx / 2
        k3y = k1y + frame_time * k2vy / 2

        tx = x + frame_time * k2x / 2
        ty = y + frame_time * k2y / 2
        k3vx, k3vy = self.calculate_total_acceleration(obj.get_id(), tx, ty)

        k4x = k1x + frame_time * k3vx
        k4y = k1y + frame_time * k3vy

        tx = x + frame_time * k3x
        ty = y + frame_time * k3y
        k4vx, k4vy = self.calculate_total_acceleration(obj.get_id(), tx, ty)

        x2 = x + (k1x + 2 * k2x + 2 * k3x + k4x) * frame_time / 6
        y2 = y + (k1y + 2 * k2y + 2 * k3y + k4y) * frame_time / 6
        obj.update_location(x2, y2)

        v2_x = k1x + (k1vx + 2 * k2vx + 2 * k3vx + k4vx) * frame_time / 6
        v2_y = k1y + (k1vy + 2 * k2vy + 2 * k3vy + k4vy) * frame_time / 6
        obj.update_velocity(v2_x, v2_y)

    # calculate gravity force of all other objects in system on current object
    def calculate_total_acceleration(self, obj_id, x, y):
        acc_x = 0
        acc_y = 0

        # iterate through all objects in system
        for obj in self.__system:
            # check that not comparing against oneself
            if obj_id != obj.get_id():
                # calculate the acceleration caused by gravitational interaction between 2 objects
                a_x, a_y = self.calculate_acceleration(x, y, obj)
                # add acceleration to total value
                acc_x += a_x
                acc_y += a_y

        return acc_x, acc_y

    # calculate acceleration between 2 objects caused by gravitational force
    def calculate_acceleration(self, x1, y1, obj):
        # calculate distance between 2 objects
        x2, y2 = obj.get_location()
        x = x1 - x2
        y = y1 - y2
        r = (x ** 2 + y ** 2) ** 0.5

        # calculate acceleration between 2 objects
        # equations used: F = m1 * a = G * m1 * m2 / r^2  =>  a = G * m2 / r^2
        a = self.__G * obj.get_mass() / r ** 2
        # split acceleration into x and y components
        a_x = - a * x / r
        a_y = - a * y / r

        return a_x, a_y
