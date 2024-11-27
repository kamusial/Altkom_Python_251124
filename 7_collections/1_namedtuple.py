from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 22)
print(p.x, p.y)
print(p[0], p[1])

