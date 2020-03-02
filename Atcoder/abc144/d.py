"""
import math


a, b, x = list(map(float, input().split()))

theta = 0
if x >= a * a * b / 2:
    theta = math.atan((2.0 * (a * a * b - x)) / (a ** 3)) / (2 * math.pi) * 360
else:
    theta = math.atan((a * b * b) / 2.0 * x) / (2 * math.pi) * 360

print(theta)
"""

from math import atan, pi

a, b, x = map(int, input().split())

if x >= a * a * b / 2:
    print(atan((a*a*b-x)/(a*a*a/2))/(2 * pi)*360)
else:
    print(90 - atan(x/(a*b*b/2))/(2 * pi)*360)
