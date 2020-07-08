from vector import Vector

a = Vector((-7.579, -7.88))
b = Vector(( 22.737,23.64))
print("parallel_to: {}".format(a.is_parallel_to(b)))
print("orthogonal_to: {}".format(b.is_orthogonal_to(a)))


c = Vector((-2.029, 9.97, 4.172))
d = Vector((-9.231, -6.639, -7.245))
print("parallel_to: {}".format(c.is_parallel_to(d)))
print("orthogonal_to: {}".format(d.is_orthogonal_to(c)))

e = Vector((2.118, 4.827))
f = Vector(( 0, 0))
print("parallel_to: {}".format( e.is_parallel_to(f)))
print("orthogonal_to: {}".format(f.is_orthogonal_to(e)))


g = Vector((-2.328, -7.284, -1.214))
h = Vector((-1.821, 1.072, -2.94))
print("parallel_to: {}".format( g.is_parallel_to(h)))
print("orthogonal_to: {}".format(g.is_orthogonal_to(h)))

