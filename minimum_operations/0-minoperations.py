#!/usr/bin/python3
"""a project with the function "minoperations" """


def minOperations(n):

    operations = 0
    addition = 1
    c = 0

    while addition < n:
        if n % addition == 0:
            c = addition
            addition *= 2
            operations += 1
        else:
            addition += c
        operations += 1

    return operations
