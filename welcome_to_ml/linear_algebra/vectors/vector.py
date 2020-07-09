from math import acos, degrees,pi, sqrt
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if(not coordinates):
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(sum(coordinates_squared)).sqrt()
 

    def normalized(self):
        # try:
        magnitude = self.magnitude()
        return self.times_scalar(Decimal('1.0')/magnitude)
        # except Exception as e:
        #     print(e)

    def sub(self, v):
        try:
            new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
            return Vector(new_coordinates)
        except Exception as e:
            print(e)
    
    def times_scalar(self, c):
        # try:            
        new_coordinates = [Decimal(c)*x for x in self.coordinates]
        return Vector(new_coordinates)
        # except Exception as e:
        #     print(e)

    def angle_with(self, v, in_degrees= False):
        # try:
        u1 = self.normalized()
        u2 = v.normalized()
        
        angle_in_radians = acos(u1.dot(u2))

        if in_degrees:
            degrees_per_radian = 180 / pi
            return angle_in_radians * degrees_per_radian
        else:
            return angle_in_radians

        # except Exception as e:
        #     print(e)

    def dot(self, v):
        # try:
        sum = 0
        for x,y in zip(self.coordinates,v.coordinates):
            sum += x *y
        return sum     
            
        # except Exception as e:
        #     print(e)
    
    def is_parallel_to(self, v):
        if (self.is_zero() or v.is_zero()):
            return True
        else:
            return (
                self.angle_with(v) == 0 
                or self.angle_with(v) == pi)

    def is_orthogonal_to(self, v, tolerance=1e-10):
        return abs(self.dot(v)) < tolerance
    
    def is_zero(self, tolerance=1e-10):
        return (self.magnitude() < tolerance)
    
    #component paralle to
    def project_to(self,v):
        v_unit_vector = v.normalized()
        return v_unit_vector.times_scalar(self.dot(v_unit_vector))
    
    def find_orthogonal_to(self, v):
        self_parallel = self.project_to(v)
        return self.sub(self_parallel) 
    
    def orthogonal_decompose(self,v):
        self_parallel = self.project_to(v)
        self_perp = self.find_orthogonal_to(v)
        return [self_parallel.coordinates, self_perp.coordinates]

    def cross(self,v):
        x1 = self.coordinates[0]
        y1 = self.coordinates[1]
        z1 = self.coordinates[2]
        x2 = v.coordinates[0]
        y2 = v.coordinates[1]
        z2 = v.coordinates[2]
        
        x = y1*z2 - y2 * z1
        y = - (x1* z2 - x2 * z1)
        z =  x1 * y2 -x2 *y1

        return Vector((x,y,z))

    def area_of_parallelogram(self, v):
        return self.cross(v).magnitude()
    
    def area_of_triangle(self, v):
        return Decimal(0.5) * self.cross(v).magnitude()
    
