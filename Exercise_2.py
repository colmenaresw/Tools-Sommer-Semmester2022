# Wilfredo Colmenares
# Computer Simulation in Science
# Sommer Semester 2022
# 2130541
# exercise 2, implementation of circunference of an Ellipse
import math

def length(x1, y1, x2, y2):
    """ function to compute the distance between two points"""
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return distance

def ellipse(a, b, t):
    """
        a, b are the half axes
        t is the parameter that goes from 0 to 2pi
        (a*sin(t), b*sin(t))
    """
    point = (a*math.cos(t), b*math.sin(t))
    return point



def circumference(a, b , n):
    points = []  # a list to save the points
    total_l = 0  # the total lenght of the circumference

    for p in range(n):  # calculate and save every point
        point = ellipse(a, b, (p/n)*2*math.pi)
        points.append(point)

    for q in range(n):
        if q < n - 1:
            total_l += length(points[q][0], points[q][1], points[q + 1][0], points[q + 1][1])
        else:
            total_l += length(points[q][0], points[q][1], points[0][0], points[0][1])

    return total_l

if __name__ == "__main__":

    # we take the input from the user
    a = int(input("please insert axis b:\n"))
    b = int(input("please insert axis a:\n"))
    epsilon = float(input("please insert precision e:\n"))
    n = 4

    # we iterate until we get the desired result
    while True:
        c_n = circumference(a,b, n)
        c_n_2 = circumference(a,b, n*2)
        accu = abs((c_n - c_n_2)/ c_n)
        print(f"current value of the circumference perimeter: {c_n} accuracy: {accu*100}%")
        if abs(accu) < epsilon:
            break
        n *= 2