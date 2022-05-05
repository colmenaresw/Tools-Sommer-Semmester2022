"""
Wilfredo Colmenares
Computer Simulation in Science
Sommer Semester 2022
2130541
exercise 5, implementation of Glass class 
"""


class Glass:
    """
        class implementation of a glass with volumen and content
    """
    def __init__(self, volumen = 250, content = 0) -> None:
        self.volumen = volumen
        self.content = content

    def fillIn(self, amount):
        """
            method for filling the glass with some amount of liquid
        """
        try:
            if amount + self.content > self.volumen:  # we check that we don't fill above the capacity
                raise Exception("amount surpass the volumen of the glass")
            else:
                self.content += amount
                print("glass filled!")
        except Exception as e:
            print("caught:", e)


    def drink(self, amount):
        """
            method for drinking the content of the glass, reducing its current content
        """
        try:
            if amount > self.content:  # we check that we don't drink above the current content
                raise Exception("amount surpass the content of the glass")
            else:
                self.content -= amount
                print("glass drunk!")
        except Exception as e:
            print("caught:", e)


    def __str__(self) -> str:
        """
            we print the properties of the glass
        """
        s = f"the glass has a volumen of: {self.volumen} and its current content is: {self.content}"
        return s


#################### MAIN SCRIPT ######################

if __name__ == "__main__":
    # some test cases
    glass01 = Glass()  # no arguments
    glass02 = Glass(300)  # one arguments
    glass03 = Glass(300, 300)  # the two arguments

    # we test our methods
    glass01.fillIn(100)
    glass03.drink(20)

    # we test our exceptions
    glass01.fillIn(260)
    glass02.drink(20)

    # we test our string method
    print("for glass 01: ", glass01)
    print("for glass 02: ", glass02)
    print("for glass 03: ", glass03)