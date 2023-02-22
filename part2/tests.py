import math
import unittest
import data
import vector_math
import collisions


class TestData(unittest.TestCase):
    def test_point_1(self):
        pt1 = data.point(1, 2, 3)
        self.assertEqual(pt1.x, 1)
        self.assertEqual(pt1.y, 2)
        self.assertEqual(pt1.z, 3)

    def test_point_2(self):
        pt2 = data.point(4, 8, 6)
        self.assertEqual(pt2.x, 4)
        self.assertEqual(pt2.y, 8)
        self.assertEqual(pt2.z, 6)

    def test_vector_1(self):
        v1 = data.vector(1, 2, 3)
        self.assertEqual(v1.x, 1)
        self.assertEqual(v1.y, 2)
        self.assertEqual(v1.z, 3)

    def test_vector_2(self):
        v2 = data.vector(5, 9, 7)
        self.assertEqual(v2.x, 5)
        self.assertEqual(v2.y, 9)
        self.assertEqual(v2.z, 7)

    def test_ray_1(self):
        pt1 = data.point(1, 2, 3)
        v1 = data.vector(1, 2, 3)
        r1 = data.ray(pt1, v1)
        self.assertEqual(r1.pt.x, 1)
        self.assertEqual(r1.pt.y, 2)
        self.assertEqual(r1.pt.z, 3)
        self.assertEqual(r1.v.x, 1)
        self.assertEqual(r1.v.y, 2)
        self.assertEqual(r1.v.z, 3)

    def test_ray_2(self):
        pt2 = data.point(3, 5, 7)
        v2 = data.vector(2, 4, 6)
        r2 = data.ray(pt2, v2)
        self.assertEqual(r2.pt.x, 3)
        self.assertEqual(r2.pt.y, 5)
        self.assertEqual(r2.pt.z, 7)
        self.assertEqual(r2.v.x, 2)
        self.assertEqual(r2.v.y, 4)
        self.assertEqual(r2.v.z, 6)

    def test_sphere_1(self):
        center1 = data.point(1, 2, 3)
        radius1 = 4.00
        color1 = data.color(255, 0, 0)
        sphere1 = data.sphere(center1, radius1, color1)
        self.assertEqual(sphere1.center.x, 1)
        self.assertEqual(sphere1.center.y, 2)
        self.assertEqual(sphere1.center.z, 3)
        self.assertAlmostEqual(sphere1.radius, 4, 2)

    def test_sphere_2(self):
        center2 = data.point(3, 9, 5)
        radius2 = 8.65
        color2 = data.color(0, 0, 255)
        sphere2 = data.sphere(center2, radius2, color2)
        self.assertEqual(sphere2.center.x, 3)
        self.assertEqual(sphere2.center.y, 9)
        self.assertEqual(sphere2.center.z, 5)
        self.assertAlmostEqual(sphere2.radius, 8.65, 2)

    def test_scale_vector_1(self):
        scalar = 2
        v = data.vector(1, 2, 3)
        sv = vector_math.scale_vector(v, scalar)
        self.assertEqual(v.x * scalar, 2)
        self.assertEqual(v.y * scalar, 4)
        self.assertEqual(v.z * scalar, 6)
        self.assertEqual(sv.x, 2)
        self.assertEqual(sv.y, 4)
        self.assertEqual(sv.z, 6)

    def test_scale_vector_2(self):
        scalar = 3
        v = data.vector(1, 2, 3)
        sv = vector_math.scale_vector(v, scalar)
        self.assertEqual(v.x * scalar, 3)
        self.assertEqual(v.y * scalar, 6)
        self.assertEqual(v.z * scalar, 9)
        self.assertEqual(sv.x, 3)
        self.assertEqual(sv.y, 6)
        self.assertEqual(sv.z, 9)

    def test_dot_vector_1(self):
        v1 = data.vector(1, 2, 2)
        v2 = data.vector(2, 1, 2)
        dotv = vector_math.dot_vector(v1, v2)
        self.assertEqual(v1.x * v2.x, 2)
        self.assertEqual(v1.y * v2.y, 2)
        self.assertEqual(v1.z * v2.z, 4)
        self.assertEqual(dotv.x, 2)
        self.assertEqual(dotv.y, 2)
        self.assertEqual(dotv.z, 4)

    def test_dot_vector_2(self):
        v1 = data.vector(2, 2, 4)
        v2 = data.vector(2, 2, 2)
        dotv = vector_math.dot_vector(v1, v2)
        self.assertEqual(v1.x * v2.x, 4)
        self.assertEqual(v1.y * v2.y, 4)
        self.assertEqual(v1.z * v2.z, 8)
        self.assertEqual(dotv.x, 4)
        self.assertEqual(dotv.y, 4)
        self.assertEqual(dotv.z, 8)

    def test_length_vector_1(self):
        v = data.vector(2, 2, math.sqrt(8))
        vLength = vector_math.length_vector(v)
        self.assertEqual(v.x ** 2 + v.y ** 2, 8)
        self.assertEqual(vLength, math.sqrt(8))

    def test_length_vector_2(self):
        v = data.vector(3, 3, math.sqrt(18))
        vLength = vector_math.length_vector(v)
        self.assertEqual(v.x ** 2 + v.y ** 2, 18)
        self.assertEqual(vLength, math.sqrt(18))

    def test_normalize_vector_1(self):
        v = data.vector(1, 2, 2)
        n = vector_math.normalize_vector(v)
        self.assertEqual(v.z / v.z, 1)
        self.assertEqual(n.x, 1)
        self.assertEqual(n.y, 2)
        self.assertEqual(n.z, 1)

    def test_normalize_vector_2(self):
        v = data.vector(2, 4, 6)
        n = vector_math.normalize_vector(v)
        self.assertEqual(v.z / v.z, 1)
        self.assertEqual(n.x, 2)
        self.assertEqual(n.y, 4)
        self.assertEqual(n.z, 1)

    def test_difference_point_1(self):
        p2 = data.point(1, 2, 3)
        p1 = data.point(4, 5, 6)
        dp = vector_math.difference_point(p1, p2)
        self.assertEqual(dp.x, 3)
        self.assertEqual(dp.y, 3)
        self.assertEqual(dp.z, 3)

    def test_difference_point_2(self):
        p2 = data.point(2, 2, 2)
        p1 = data.point(4, 5, 6)
        dp = vector_math.difference_point(p1, p2)
        self.assertEqual(dp.x, 2)
        self.assertEqual(dp.y, 3)
        self.assertEqual(dp.z, 4)

    def test_difference_vector_1(self):
        v2 = data.vector(1, 2, 3)
        v1 = data.vector(4, 5, 6)
        dv = vector_math.difference_vector(v1, v2)
        self.assertEqual(dv.x, 3)
        self.assertEqual(dv.y, 3)
        self.assertEqual(dv.z, 3)

    def test_difference_vector_2(self):
        v2 = data.vector(1, 1, 1)
        v1 = data.vector(4, 5, 6)
        dv = vector_math.difference_vector(v1, v2)
        self.assertEqual(dv.x, 3)
        self.assertEqual(dv.y, 4)
        self.assertEqual(dv.z, 5)

    def test_translate_point_1(self):
        p = data.point(1, 2, 3)
        v = data.vector(4, 5, 6)
        tp = vector_math.translate_point(p, v)
        self.assertEqual(tp.x, 5)
        self.assertEqual(tp.y, 7)
        self.assertEqual(tp.z, 9)

    def test_translate_point_2(self):
        p = data.point(0, 0, 0)
        v = data.vector(4, 5, 6)
        tp = vector_math.translate_point(p, v)
        self.assertEqual(tp.x, 4)
        self.assertEqual(tp.y, 5)
        self.assertEqual(tp.z, 6)

    def test_vector_from_to_1(self):
        from_point = data.point(1, 2, 3)
        to_point = data.point(4, 5, 6)
        vft = vector_math.vector_from_to(from_point, to_point)
        self.assertEqual(vft.x, 3)
        self.assertEqual(vft.y, 3)
        self.assertEqual(vft.z, 3)

    def test_vector_from_to_2(self):
        from_point = data.point(0, 0, 0)
        to_point = data.point(4, 5, 6)
        vft = vector_math.vector_from_to(from_point, to_point)
        self.assertEqual(vft.x, 4)
        self.assertEqual(vft.y, 5)
        self.assertEqual(vft.z, 6)

    def test_sphere_intersection_point_1(self):
        pt = data.point(0, 2, 0)
        v = data.vector(0, 0, 3)
        ray = data.ray(pt, v)
        center = data.point(0, 5, 0)
        radius = 2
        color = data.color(255, 0, 0)
        sphere = data.sphere(center, radius, color)
        intersection = data.point(0, 2, 0)

        self.assertEqual(collisions.sphere_intersection_point(ray, sphere).x, intersection.x)
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere).y, intersection.y)
        self.assertEqual(collisions.sphere_intersection_point(ray, sphere).z, intersection.z)

    def test_find_intersection_points_1(self):
        center1 = data.point(2, 2, 0)
        radius1 = 2
        color1 = data.color(255, 0, 0)
        sphere1 = data.sphere(center1, radius1, color1)
        center2 = data.point(3, 2, 0)
        radius2 = 2
        color2 = data.color(0, 0, 255)
        sphere2 = data.sphere(center2, radius2, color2)
        sphere_list = [sphere1, sphere2]

        pt = data.point(0, 0, 0)
        v = data.vector(8, 7, 0)
        ray = data.ray(pt, v)

        intersectionPt1 = data.point(3.2, 2.4, 0)
        intersectionPt2 = data.point(4.5, 3.0, 0)

        self.assertListEqual(collisions.sphere_intersection_point(radius1, sphere1).x, intersectionPt1.x)
        self.assertListEqual(collisions.sphere_intersection_point(radius1, sphere1).y, intersectionPt1.y)
        self.assertListEqual(collisions.sphere_intersection_point(radius1, sphere1).z, intersectionPt1.z)
        self.assertListEqual(collisions.sphere_intersection_point(radius2, sphere2).x, intersectionPt2.x)
        self.assertListEqual(collisions.sphere_intersection_point(radius2, sphere2).y, intersectionPt2.y)
        self.assertListEqual(collisions.sphere_intersection_point(radius2, sphere2).z, intersectionPt2.z)

    def test_sphere_normal_at_point_1(self):
        center = data.point(2, 5, 0)
        radius = 4
        color = data.color(255, 0, 0)
        sphere = data.sphere(center, radius, color)
        pt = data.point(0, 0, 0)
        vec_to_point_sphere = vector_math.vector_from_to(pt, sphere.center)
        self.assertEqual(vec_to_point_sphere.x, 2)
        self.assertEqual(vec_to_point_sphere.y, 5)
        self.assertEqual(vec_to_point_sphere.z, 0)


if __name__ == '__main__':
    unittest.main()
