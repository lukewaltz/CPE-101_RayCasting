import data
import vector_math
import collisions


def cast_ray(ray, sphere_list):
    if not collisions.find_intersection_points(sphere_list, ray):
        return False
    else:
        return True


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
            if cast_ray(eye_ray, sphere_list):
                print("0 0 0")
            else:
                print("255 255 255")


cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.point(0, 0, -14),
              [data.sphere(data.point(1, 1, 0), 2), data.sphere(data.point(0.5, 1.5, -3), 0.5)])
