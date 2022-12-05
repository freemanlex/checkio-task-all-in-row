"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [[1, 2, 3]],
            "answer": [1, 2, 3]
        },
        {
            "input": [[1, [2, 2, 2], 4]],
            "answer": [1, 2, 2, 2, 4]
        },
        {
            "input": [[[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]],
            "answer": [2, 4, 5, 6, 6, 6, 6, 6, 7]
        },
        {
            "input": [[-1, [1, [-2], 1], -1]],
            "answer": [-1, 1, -2, 1, -1],
        },
    ],
    "Edge": [
        {
            "input": [[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]],
            "answer": [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
        },
        {
            "input": [[]],
            "answer": []
        },
        {
            "input": [[[[[[[[[[2 ** 32 - 1]]]]]]]]]],
            "answer": [2 ** 32 - 1]
        },
        {
            "input": [[[[[[[[[[2 ** 32 - 1]]]]]]]], -2**32 + 1]],
            "answer": [2 ** 32 - 1, -2 ** 32 + 1]
        },
        {
            "input": [[[[[[[[[[]]]]]]]]]],
            "answer": []
        },
        {
            "input": [[-1, [1, [-2, [3], [[5], [10, -11], [1, 100, [-1000, [5000]]], [20, -10, [[[]]]]]]]]],
            "answer": [-1, 1, -2, 3, 5, 10, -11, 1, 100, -1000, 5000, 20, -10],
        },
    ],
    "Extra": [
        {
            "input": [[1, [2, [3]]]],
            "answer": [1, 2, 3]
        },
        {
            "input": [[100, 200, 300, [400, 500]]],
            "answer": [100, 200, 300, 400, 500]
        },
        {
            "input": [[2, [2, [2, [2]]]]],
            "answer": [2, 2, 2, 2]
        },
        {
            "input": [[[[[3], 3], 3], 3]],
            "answer": [3, 3, 3, 3]
        },
        {
            "input": [[[7], [6], [7]]],
            "answer": [7, 6, 7]
        },
        {
            "input": [[11, 21, 31]],
            "answer": [11, 21, 31]
        },
        {
            "input": [[13, [23, 23, 23], 43]],
            "answer": [13, 23, 23, 23, 43]
        },
        {
            "input": [[[[22]], [44, [55, 66, [66], 66, 66, 66], 77]]],
            "answer": [22, 44, 55, 66, 66, 66, 66, 66, 77]
        },
        {
            "input": [[10, [20, [30]]]],
            "answer": [10, 20, 30]
        },
        {
            "input": [[1001, 2001, 3001, [4001, 5001]]],
            "answer": [1001, 2001, 3001, 4001, 5001]
        },
        {
            "input": [[20, [20, [20, [20]]]]],
            "answer": [20, 20, 20, 20]
        },
        {
            "input": [[[[[53], -43], 33], 23]],
            "answer": [53, -43, 33, 23]
        },
        {
            "input": [[[7007], [6006], [7007]]],
            "answer": [7007, 6006, 7007]
        },
    ]
}
