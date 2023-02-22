import data
import vector_math
import collisions
import math


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def cast_ray(ray, sphere_list, eye_point):
    lst = collisions.find_intersection_points(sphere_list, ray)
    color = data.color(255, 255, 255)
    if lst != []:
        d = math.inf
        for t in lst:
            if distance(eye_point, t[0].center) < d:
                d = distance(eye_point, t[0].center)
                color = t[0].color
    return color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    print("P3")
    print(width, height)
    print("255")
    x_step = (max_x - min_x) / width
    y_step = (max_y - min_y) / height
    for j in range(height):
        for i in range(width):
            x = min_x + i * x_step
            y = max_y - j * y_step
            pt = data.point(x, y, 0)
            eye_ray = data.ray(eye_point, vector_math.vector_from_to(eye_point, pt))
            color = cast_ray(eye_ray, sphere_list, eye_point)
            print(color)


cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.point(0, 0, -14),
              [data.sphere(data.point(1, 1, 0), 2, data.color(0, 0, 255)),
               data.sphere(data.point(0.5, 1.5, -3), 0.5, data.color(255, 0, 0))])



