from typing import List, Tuple
from fractions import Fraction

Coords = List[Tuple[int, int]]


def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    def make_edges(coords):
        return [(x1 - x2) ** 2 + (y1 - y2) ** 2 for (x1, y1), (x2, y2) in zip(coords, coords[1:] + coords[:1])]

    edges_1 = make_edges(coords_1)
    edges_2 = make_edges(coords_2)

    return any(len(set(map(Fraction, sorted(edges_1, reverse=j), edges_2[i:] + edges_2[:i]))) == 1
               for j in range(2) for i in range(3))


if __name__ == '__main__':
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'basic (different)'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
