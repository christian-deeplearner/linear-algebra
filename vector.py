class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __repr__(self):
      return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self, v):
      new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
      return Vector(new_coordinates)

    def __sub__(self, v):
      new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
      return Vector(new_coordinates)

    def __mul__(self, scalar):
      new_coordinates = [scalar * x for x in self.coordinates]
      return Vector(new_coordinates)
