class Road:
    _specific_asphalt_consumption = 25
    _roadway_thickness = 5

    def __init__(self, length, width):
        self._length = length;
        self._with = width

    def asphalt_consumption(self):
        return self._length * self._with * Road._specific_asphalt_consumption * Road._roadway_thickness


road = Road(5000, 20)
Road.roadway_thickness=30
road.attr=6
print(road.asphalt_consumption())
