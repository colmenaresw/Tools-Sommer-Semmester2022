# Wilfredo Colmenares
# Computer Simulation in Science
# Sommer Semester 2022
# 2130541
# exercise 1, implementation of collatz conjecture

def collatz(n):
    """ function to compute and save into a list the collatz numbers"""
    l = []  # initialized list
    while n != 1:
        if n % 2 == 0:  # if the number is even
            n /= 2
        else:
            n = (n * 3) + 1
        l.append(n)
    return l

if __name__ == "__main__":
    print(collatz(2223))  # print answer
