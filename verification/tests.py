"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""
from random import randint, choice
from itertools import chain
from fractions import Fraction
from my_solution import similar_triangles


class Triangle:
    def __init__(self, coords):
        self.coords = coords

    def random_scaling(self):
        x1, y1, x2, y2, x3, y3 = chain(*self.coords)
        scaling_candidates = []
        for s in range(1, 20):
            new_x2 = x1 + (x2 - x1) * s
            new_x3 = x1 + (x3 - x1) * s
            new_y2 = y1 + (y2 - y1) * s
            new_y3 = y1 + (y3 - y1) * s
            if (max(x1, new_x2, new_x3) - min(x1, new_x2, new_x3) <= 20
                    and max(y1, new_y2, new_y3) - min(y1, new_y2, new_y3) <= 20):
                scaling_candidates.append({(x1, y1), (new_x2, new_y2), (new_x3, new_y3)})
            else:
                break
        self.coords = choice(scaling_candidates)

    def random_rotation(self):
        rot = randint(0, 3)

        def rotate(coord):
            rot_coord = complex(*coord) * (1j ** rot)
            return int(rot_coord.real), int(rot_coord.imag)

        self.coords = list(map(rotate, self.coords))

    def random_reflection(self):
        sign = choice([-1, 1])
        self.coords = list(map(lambda co: (co[0] * sign, co[1]), self.coords))

    def random_translation(self):
        xs = [co[0] for co in self.coords]
        ys = [co[1] for co in self.coords]
        dx = randint(-10 - min(xs), 10 - max(xs))
        dy = randint(-10 - min(ys), 10 - max(ys))
        self.coords = list(map(lambda x, y: (x + dx, y + dy), xs, ys))


def make_random_triangle():
    coords_set = set()
    while True:
        while len(coords_set) < 3:
            x = randint(-5, 5)
            y = randint(-5, 5)
            coords_set.add((x, y))
        coords = list(coords_set)
        if len(set(map(lambda a, b: (c := a[0] - b[0]) and Fraction(a[1] - b[1], c),
                       coords, coords[1:]))) != 1:
            return Triangle(coords)
        coords_set.clear()


def make_two_triangles():
    if choice([1, 1, 1, 0]):
        # similar triangles
        triangle_1 = make_random_triangle()
        triangle_2 = Triangle(triangle_1.coords)
        triangle_2.random_scaling()
        triangle_2.random_reflection()
        triangle_2.random_rotation()
    else:
        # at random
        triangle_1 = make_random_triangle()
        triangle_2 = make_random_triangle()

    triangle_2.random_translation()

    return triangle_1.coords, triangle_2.coords


def make_random_tests(num):
    random_tests = []
    for _ in range(num):
        coords_1, coords_2 = make_two_triangles()
        random_tests.append({'input': [coords_1, coords_2],
                             'answer': similar_triangles(coords_1, coords_2)})
    return random_tests


TESTS = {
    "Basics": [
        {
            "input": [[[0, 0], [1, 2], [2, 0]], [[3, 0], [4, 2], [5, 0]]],
            "answer": True,
            "explanation": 'basic'
        },
        {
            "input": [[[0, 0], [1, 2], [2, 0]], [[3, 0], [4, 3], [5, 0]]],
            "answer": False,
            "explanation": 'basic (different)'
        },
        {
            "input": [[[0, 0], [1, 2], [2, 0]], [[2, 0], [4, 4], [6, 0]]],
            "answer": True,
            "explanation": 'scaling'
        },
        {
            "input": [[[0, 0], [0, 3], [2, 0]], [[3, 0], [5, 3], [5, 0]]],
            "answer": True,
            "explanation": 'reflection'
        },
        {
            "input": [[[1, 0], [1, 2], [2, 0]], [[3, 0], [5, 4], [5, 0]]],
            "answer": True,
            "explanation": 'scaling and reflection'
        },
        {
            "input": [[[1, 0], [1, 3], [2, 0]], [[3, 0], [5, 5], [5, 0]]],
            "answer": False,
            "explanation": 'scaling and reflection (different)'
        },
        {
            "input": [[[0, 2], [1, 4], [5, 2]], [[0, 1], [1, 3], [5, 1]]],
            "answer": True,
            "explanation": 'overlap'
        },
        {
            "input": [[[1, 3], [4, 2], [2, 1]], [[2, -2], [0, -3], [-1, -1]]],
            "answer": True,
            "explanation": 'negative coordinates'
        },
        {
            "input": [[[1, 3], [2, 5], [3, 3]], [[3, 0], [3, 2], [5, 1]]],
            "answer": True,
            "explanation": 'rotate 90 degrees'
        },
        {
            "input": [[[1, 3], [2, 5], [3, 3]], [[1, 1], [3, 1], [2, -1]]],
            "answer": True,
            "explanation": 'rotate 180 degrees'
        },
        {
            "input": [[[1, 3], [2, 5], [3, 3]], [[1, 2], [-1, 0], [1, 0]]],
            "answer": False,
            "explanation": 'rotate different'
        },
        {
            "input": [[[10, 10], [5, 10], [-10, -10]], [[10, 10], [7, 6], [-10, -10]]],
            "answer": False,
            "explanation": 'only ratio of 2 sides'
        },
    ],
    "Randoms": make_random_tests(10),
}
