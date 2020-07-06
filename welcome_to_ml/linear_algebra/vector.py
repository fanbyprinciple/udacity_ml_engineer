class Vector(object):
    def __init__(self, coordinates):
        try:
            if(not coordinates):
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)             

        except ValueError:
            raise ValueError('The coordinates must be non empty !')

        except TypeError:
            raise TypeError('The coordinates must be an iterable.')
    
    def __str__(self):
        # handle for when the object is called
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self,v):
        # used to check for equivalence
        return self.coordinates == v.coordinates
    
    def add(self, v):
        try:
            new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(new_coordinates)
        except Exception as e:
            print(e)

    def magnitude(self):
        try:
            sum = 0
            for i in self.coordinates:
        
                sum += i * i
            return sum ** 0.5
        
        except Exception as e:
            print(e)

    def normalise(self):
        try:
            sum = 0
            for i in self.coordinates:
                sum += i * i
            magnitude = sum ** 0.5
            new_coordinates = [i/magnitude for i in self.coordinates]
            return new_coordinates
        
        except Exception as e:
            print(e)

    def sub(self, v):
        try:
            new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(new_coordinates)
        except Exception as e:
            print(e)
    
    def times_scalar(self, c):
        try:            
            new_coordinates = [c*x for x in self.coordinates]
            return Vector(new_coordinates)
        except Exception as e:
            print(e)