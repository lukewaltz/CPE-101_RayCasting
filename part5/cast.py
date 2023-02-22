import data
import vector_math
import collisions
import math
import sys


def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2)


def color_mult(c1, c2):
    return data.color((c1.R * c2.R), (c1.G * c2.G), (c1.B * c2.B))


def color_float(c1, f1):
    return data.color((c1.R * f1), (c1.G * f1), (c1.B * f1))


def color_add(c1, c2):
    return data.color((c1.R + c2.R), (c1.G + c2.G), (c1.B + c2.B))


def index_of_min(distance_list):
    length = len(distance_list)
    if length == 0:
        return None

    minimum = 0
    for i in range(length):
        if distance_list[i] < distance_list[minimum]:
            minimum = i
    return minimum


def nearest_index(intersections_only, eye_point):
    length = len(intersections_only)
    if length == 0:
        return None

    distance_list = [distance(p, eye_point) for p in intersections_only]
    return index_of_min(distance_list)


def cast_ray(ray, sphere_list, ambient_color, light, eye_point):
    intersection_list = collisions.find_intersection_points(sphere_list, ray)
    intersections_only = [t[1] for t in intersection_list]
    near_index = nearest_index(intersections_only, ray.pt)
    if near_index is None:
        return data.color(1, 1, 1)

    color = color_mult(color_float(sphere_list[near_index].color, sphere_list[near_index].finish.ambient),
                       ambient_color)
    #color = color_float(color, 0)

    #intersection = intersections_only[near_index]
    sphere = intersection_list[near_index][0]
    point = intersection_list[near_index][1]
    normal = collisions.sphere_normal_at_point(sphere, point)
    pe = vector_math.translate_point(point, vector_math.scale_vector(normal, 0.01))

    light_dir = vector_math.normalize_vector(vector_math.vector_from_to(pe, light.point))

    ray_to_light = data.ray(pe, light_dir)
    reflection_blocks = collisions.find_intersection_points(sphere_list, ray_to_light)
    if not reflection_blocks:
        # nothing blocking the light
        diffuse_factor = vector_math.dot_vector(normal, light_dir)

        if diffuse_factor < 0:
            diffuse_contribution = data.color(0, 0, 0)
        else:
            c1 = color_float(light.color, diffuse_factor)
            c2 = sphere.color
            c3 = color_mult(c1, c2)
            c4 = sphere.finish.diffuse
            diffuse_contribution = color_float(c3, c4)

        color = color_add(color, diffuse_contribution)

    else:
        # light might be blocked
        block_points = [t[1] for t in reflection_blocks]
        nearest_block = block_points[nearest_index(block_points, pe)]
        if (distance(pe, nearest_block)) > (distance(pe, light.point)):
            # nearest block is father than light point
            # diffuse contribution to color
            diffuse_factor = vector_math.dot_vector(normal, light_dir)
            if diffuse_factor < 0:
                diffuse_contribution = data.color(0, 0, 0)
            else:
                c1 = color_float(diffuse_factor, light.color)
                c2 = color_float(sphere.color, sphere.finish.diffuse)
                diffuse_contribution = color_mult(c1, c2)
            color = color_add(color, diffuse_contribution)

    # specular stuff
    normal_light = vector_math.dot_vector(normal, light_dir)
    b = (normal_light * 2)
    c = vector_math.scale_vector(normal, b)
    reflection_vector = vector_math.difference_vector(light_dir, c)
    v_dir = vector_math.normalize_vector(vector_math.vector_from_to(eye_point, pe))
    specular_intensity = vector_math.dot_vector(reflection_vector, v_dir)
    if specular_intensity < 0:
        specular_contribution = data.color(0, 0, 0)
    else:
        c1 = color_float(light.color, sphere.finish.specular)
        c2 = specular_intensity ** (1 / sphere.finish.roughness)
        specular_contribution = color_float(c1, c2)
    color = color_add(color, specular_contribution)

    return color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, ambient_color, light):
    print("P3")
    print(width, height)
    print("255")
    x_step = (max_x - min_x) / width
    y_step = (max_y - min_y) / height
    for j in range(height):
        for i in range(width):
            x = min_x + i * x_step
            y = max_y - j * y_step
            direction_point = data.point(x, y, 0)
            eye_ray = data.ray(eye_point, vector_math.vector_from_to(eye_point, direction_point))
            color = cast_ray(eye_ray, sphere_list, ambient_color, light, eye_point)
            red = min(int(color.R * 255), 255)
            green = min(int(color.G * 255), 255)
            blue = min(int(color.B * 255), 255)
            print(red, green, blue)


cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.point(0, 0, -14),
              [data.sphere(data.point(1, 1, 0), 2, data.color(0.0, 0.0, 1.0),
                           data.finish(0.2, 0.4, 0.5, 0.05)),
               data.sphere(data.point(0.5, 1.5, -3), 0.5, data.color(1.0, 0.0, 0.0),
                           data.finish(0.4, 0.4, 0.5, 0.05))],
              data.color(1.0, 1.0, 1.0), data.light(data.point(-100.0, 100.0, -100.0), data.color(1.5, 1.5, 1.5)))
