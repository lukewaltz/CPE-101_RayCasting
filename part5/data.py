import utility


class point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)


class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x) and utility.epsilon_equal(self.y,
                                                                                other.y) and utility.epsilon_equal(
            self.z, other.z)


class ray:
    def __init__(self, pt, v):
        self.v = v
        self.pt = pt

    def __eq__(self, other):
        return utility.epsilon_equal(self.pt, other.pt) and utility.epsilon_equal(self.v, other.v)


class sphere:
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return utility.epsilon_equal(self.center, other.pt) and \
               utility.epsilon_equal(self.radius, other.radius) and \
               utility.epsilon_equal(self.color, other.color) and \
               utility.epsilon_equal(self.finish, other.finish)


class color:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def __eq__(self, other):
        return utility.epsilon_equal(self.R, other.R) and utility.epsilon_equal(self.G,
                                                                                other.G) and utility.epsilon_equal(
            self.B, other.B)

    def __str__(self):
        return f"{self.R} {self.G} {self.B}"


class finish:
    def __init__(self, ambient, diffuse, specular, roughness):
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.roughness = roughness

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient,
                                     other.ambient) and utility.epsilon_equal(self.diffuse,
                                                                              other.diffuse) and utility.epsilon_equal(
            self.specular, other.specular) and utility.epsilon_equal(self.roughness, other.roughness)


class light:
    def __init__(self, point, color):
        self.point = point
        self.color = color

    def __eq__(self, other):
        return utility.epsilon_equal(self.point, other.point) and utility.epsilon_equal(self.color, other.color)
