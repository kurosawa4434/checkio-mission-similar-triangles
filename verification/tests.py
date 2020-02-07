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


def make_random_tests(num):
    random_tests = []
    for _ in range(num):
        coords_1, coords_2 = make_two_triangles()
        random_tests.append({'input': [coords_1, coords_2],
                             'answer': similar_triangles(coords_1, coords_2)})
    return random_tests


def make_two_triangles():
    def make_ronadom_triangle():
        coords_set = set()
        while True:
            while len(coords_set) < 3:
                x = randint(-5, 5)
                y = randint(-5, 5)
                coords_set.add((x, y))
            coords = list(coords_set)
            if len(set(map(lambda a, b: (c := a[0] - b[0]) and Fraction(a[1] - b[1], c), coords, coords[1:]))) != 1:
                return coords
            coords_set.clear()

    def scaling(coords):
        x, y, x1, y1, x2, y2 = chain(*coords)
        scaling_candidates = []
        for s in range(1, 20):
            new_x1 = x + (x1 - x) * s
            new_x2 = x + (x2 - x) * s
            new_y1 = y + (y1 - y) * s
            new_y2 = y + (y2 - y) * s
            if (max(x, new_x1, new_x2) - min(x, new_x1, new_x2) <= 20
                    and max(y, new_y1, new_y2) - min(y, new_y1, new_y2) <= 20):
                scaling_candidates.append({(x, y), (new_x1, new_y1), (new_x2, new_y2)})
            else:
                break
        scale = randint(0, len(scaling_candidates) - 1)
        return scaling_candidates[scale]

    def rotation(coords):
        rot = randint(0, 3)

        def rotate(coord):
            rot_coord = complex(*coord) * (1j ** rot)
            return int(rot_coord.real), int(rot_coord.imag)

        return list(map(rotate, coords))

    def reflection(coords):
        sign = choice([-1, 1])
        return list(map(lambda co: (co[0] * sign, co[1]), coords))

    def translation(coords):
        xs = [co[0] for co in coords]
        ys = [co[1] for co in coords]
        dx = randint(-10 - min(xs), 10 - max(xs))
        dy = randint(-10 - min(ys), 10 - max(ys))
        return list(map(lambda x, y: (x + dx, y + dy), xs, ys))

    # main
    if choice([1, 1, 1, 0]):
        # similar triangles
        triangle_1 = make_ronadom_triangle()
        triangle_2 = scaling(triangle_1)
        triangle_2 = reflection(triangle_2)
        triangle_2 = rotation(triangle_2)
    else:
        # at random
        triangle_1 = make_ronadom_triangle()
        triangle_2 = make_ronadom_triangle()

    return triangle_1, translation(triangle_2)


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
    ],
    "Randoms": make_random_tests(10),
}
