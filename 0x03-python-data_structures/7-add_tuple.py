#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    results = [0, 0]
    for i in range(2):
        if (len(tuple_a) > i):
            results[i] += tuple_a[i]
        if (len(tuple_b) > i):
            results[i] += tuple_b[i]

    done = (results[0], results[1])
    return (done)
