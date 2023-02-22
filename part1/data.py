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
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return utility.epsilon_equal(self.center, other.pt) and utility.epsilon_equal(self.radius,
                                                                                      other.radius)


class color:
    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def __eq__(self, other):
        return utility.epsilon_equal(self.R, other.R) and utility.epsilon_equal(self.G,
                                                                                other.G) and utility.epsilon_equal(
            self.B, other.B)
