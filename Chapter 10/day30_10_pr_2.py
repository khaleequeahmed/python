class Calculator:
    def __init__(self, num):
        self.Number = num

    def square(self):
        print(f"The Value of the {self.Number} Square is {self.Number **2}")
            

    def squareRoot(self):
        print(f"The Value of the {self.Number} SquareRoot is {self.Number **0.5}")

    def cube(self):
        print(f"The Value of the {self.Number} Cube is {self.Number **3}")
            
a = Calculator(9)
a.square()
a.squareRoot()
a.cube()
