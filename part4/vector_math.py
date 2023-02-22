import data
import math


def scale_vector(v, scalar):
    return data.vector((v.x * scalar), (v.y * scalar), (v.z * scalar))


def dot_vector(v1, v2):
    return (v1.x * v2.x) + (v1.y * v2.y) + (v1.z * v2.z)


def length_vector(v):
    return math.sqrt((v.x ** 2) + (v.y ** 2) + (v.z ** 2))


def normalize_vector(v):
    length = length_vector(v)
    return data.vector((v.x / length), (v.y / length), (v.z / length))


def difference_point(p1, p2):
    return data.vector((p1.x - p2.x), (p1.y - p2.y), (p1.z - p2.z))


def difference_vector(v1, v2):
    return data.vector((v1.x - v2.x), (v1.y - v2.y), (v1.z - v2.z))


def translate_point(p, v):
    return data.point((p.x + v.x), (p.y + v.y), (p.z + v.z))


def vector_from_to(from_point, to_point):
    return data.vector((to_point.x - from_point.x), (to_point.y - from_point.y), (to_point.z - from_point.z))
