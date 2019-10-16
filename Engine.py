from Object import Object


class Engine:

    def __init__(self, system):
        self.__G = 6.67408e-11
        self.__system = system

    def get_objects(self):
        return self.__system

    def process_system(self, frame_time):
        for obj in self.__system:
            self.process_object(obj, frame_time)

        for obj in self.__system:
            obj.commit_location()

    def process_object(self, obj, frame_time):
        acc_x = 0
        acc_y = 0

        for obj2 in self.__system:
            if obj.get_id() != obj2.get_id():
                a_x, a_y = self.calculate_acceleration(obj, obj2)
                acc_x += a_x
                acc_y += a_y

        obj.update_location(frame_time)
        obj.update_velocity(frame_time, acc_x, acc_y)

    def calculate_acceleration(self, obj1, obj2):
        x1, y1 = obj1.get_location()
        x2, y2 = obj2.get_location()
        x = x1 - x2
        y = y1 - y2

        r = (x ** 2 + y ** 2) ** 0.5
        a = self.__G * obj2.get_mass() / r ** 2
        a_x = - a * x / r
        a_y = - a * y / r

        return a_x, a_y
