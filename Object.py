class Object:

    def __init__(self, obj_id, m, x, y, v_x, v_y):
        self.__id = obj_id
        self.__mass = m
        self.__loc = (x, y)
        self.__temp_loc = (x, y)
        self.__velocity = (v_x, v_y)

    def update_location(self, x, y):
        self.__temp_loc = x, y

    def update_velocity(self, v_x, v_y):
        self.__velocity = v_x, v_y

    def commit_location(self):
        self.__loc = self.__temp_loc

    def get_velocity(self):
        return self.__velocity

    def get_location(self):
        return self.__loc

    def get_mass(self):
        return self.__mass

    def get_id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, Object):
            return NotImplemented

        return self.__id == other.get_id()
