"""
Wilfredo Colmenares
Computer Simulation in Science
Sommer Semester 2022
2130541
exercise 8, curve discussion
"""


from sympy import *
from sympy.plotting import plot

x = symbols('x')

# defining the function
f_x = 2*x + 8 + (66/(x-8))


# plotting
# p1 = plot(f_x, (x,0,4), show=False)
# p1.save("test.png")


# computing all zeros
zeros = solve(f_x, x)  # we calculate the zeros of the function

i_zeros = Interval(zeros[0], zeros[1])  # we create an interval with the zeros of the function
i = Interval(0, 5)

deriv = diff(f_x, x)  # we calculate its derivative
max = maximum(f_x, x, i)  # we calculate the maxima inside the interval [0, 5], otherwise it is infinity
integral_def = integrate(f_x, (x, zeros[0], zeros[1]))

print(type(zeros))
print(max)
print(integral_def.evalf())

print("done")