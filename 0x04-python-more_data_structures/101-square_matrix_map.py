#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda horizontal: list(map(lambda vertical: vertical ** 2, horizontal)), matrix))
