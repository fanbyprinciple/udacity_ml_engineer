from vector import Vector

a = Vector((8.462, 7.893, -8.187))
b = Vector((6.984, -5.975, 4.778))
print("cross vector: ", a.cross(b).coordinates)
# print("orthogonal_to: {}".format(b.is_orthogonal_to(a)))


c = Vector((-8.987, -9.838, 5.031))
d = Vector((-4.268, -1.861, -8.866))
print("Area of parallelogram: ", c.area_of_parallelogram(d))
# print("orthogonal_to: {}".format(d.is_orthogonal_to(c)))

e = Vector((1.5,9.547,3.681))
f = Vector(( -6.007, 0.124, 5.772 ))
print("Area of triangle: ",e.area_of_triangle(f) )
# print("orthogonal_to: {}".format(f.is_orthogonal_to(e)))


# g = Vector((-2.328, -7.284, -1.214))
# h = Vector((-1.821, 1.072, -2.94))
# print("parallel_to: {}".format( g.is_parallel_to(h)))
# print("orthogonal_to: {}".format(g.is_orthogonal_to(h)))
