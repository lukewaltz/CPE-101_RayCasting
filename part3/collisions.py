import math
import data
import vector_math


def sphere_intersection_point(ray, sphere):
    vector_between_point_sphere = vector_math.difference_point(ray.pt, sphere.center)

    a = vector_math.dot_vector(ray.v, ray.v)
    b = vector_math.dot_vector(vector_math.scale_vector(vector_between_point_sphere, 2), ray.v)
    c = vector_math.dot_vector(vector_between_point_sphere, vector_between_point_sphere) - (sphere.radius ** 2)

    determinant = (b ** 2) - (4 * a * c)

    if determinant < 0:
        return None
    elif determinant == 0:
        root = (-b) / (2 * a)
        if root >= 0:
            point = vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.v, root))
            return point
        else:
            return None
    if determinant > 0:
        root1 = ((-b) + math.sqrt(determinant)) / (2 * a)
        root2 = ((-b) - math.sqrt(determinant)) / (2 * a)

        if root1 >= 0 and root2 >= 0:
            if root1 > root2:
                return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.v, root2))
            else:
                return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.v, root1))
        elif root1 > 0 or root2 > 0:
            if root1 > 0:
                return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.v, root1))
            else:
                return vector_math.translate_point(ray.pt, vector_math.scale_vector(ray.v, root2))


def find_intersection_points(sphere_list, ray):
    r = []
    for sphere in sphere_list:
        point = sphere_intersection_point(ray, sphere)
        if point is not None:
            r.append((sphere, point))
    return r


def sphere_normal_at_point(sphere, pt):
    vec_to_point_sphere = vector_math.vector_from_to(sphere.center, pt)
    return vector_math.normalize_vector(vec_to_point_sphere)

