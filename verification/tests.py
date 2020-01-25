"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


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
    ]
}
