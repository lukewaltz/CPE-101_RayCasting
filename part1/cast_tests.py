import unittest
import cast
import vector_math
import data
import collisions


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_cast_ray_1(self):
        pt = data.point(100, 100, 0)
        v = data.vector(100, 100, 100)
        ray = data.ray(pt, v)
        center1 = data.point(100, 150, 0)
        center2 = data.point(75, 225, 0)
        radius1 = 5
        radius2 = 10
        sphere1 = data.sphere(center1, radius1)
        sphere2 = data.sphere(center2, radius2)
        sphere_list = [sphere1, sphere2]
        self.assertEqual(cast.cast_ray(ray, sphere_list), 5)

    def test_cast_all_rays_1(self):
        cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.point(0, 0, -14),
                           [data.sphere(data.point(1, 1, 0), 2), data.sphere(data.point(0.5, 1.5, -3), 0.5)])


if __name__ == '__main__':
    unittest.main()
