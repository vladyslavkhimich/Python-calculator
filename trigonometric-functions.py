import math


def radFromDegs(degs):
    return degs / 180 * math.pi


def factorial(number):
    if number == 1:
        return number
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


def sine(degs):
    rads = radFromDegs(degs)
    return round(rads - (pow(rads, 3) / factorial(3)) + (pow(rads, 5) / factorial(5)), 7)


def cosine(degs):
    rads = radFromDegs(degs)
    return round(1 - (pow(rads, 2) / factorial(2)) + (pow(rads, 4) / factorial(4)), 7)


def tangent(degs):
    return round(sine(degs) / cosine(degs), 7)


def cotangent(degs):
    return round(cosine(degs) / sine(degs), 7)
