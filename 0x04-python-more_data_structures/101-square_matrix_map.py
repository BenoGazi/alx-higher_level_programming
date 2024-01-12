#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda h: list(map(lambda v: v ** 2, h)), matrix))
