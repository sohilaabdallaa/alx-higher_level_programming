#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided


matrix = [
    [1.5, 1.5, 1.5],
    [1.5, 1.5, 1.5]
]
print(matrix_divided(matrix, 3))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 0.5))


matrix = [
    [0, 0, 0],
    [0, 0, 0]
]
print(matrix_divided(matrix, 3))


