from vector import Vector

a = Vector((7.887, 4.138))
b = Vector(( -8.802, 6.776))
print(a.dot(b))


c = Vector((-5.955, -4.904, -1.874))
d = Vector((-4.496, -8.755, 7.103))
print(c.dot(d))

e = Vector((3.183, -7.627))
f = Vector(( -2.668, 5.319))
print(e.angle_with(f))


g = Vector((7.35, 0.221, 5.188))
h = Vector((2.751, 8.259, 3.985))
print(g.angle_with(h, in_degrees=True))

# e = Vector((1.671, -1.012, -0.318))
# scalar = 7.41
# print(e.times_scalar(scalar))

