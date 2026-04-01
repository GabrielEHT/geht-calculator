class calculatorEngine:
    """Class that makes math operation and returns a rounded result
    with two decimals"""
    def __init__(self, equation: list):
        for index in range(len(equation)):
            try:
                equation[index] = int(equation[index])
            except ValueError:
                try:
                    equation[index] = float(equation[index])
                except ValueError:
                    pass
        self.solvethis = equation

    def __checkIndex(self, operand):
        try:
            return self.solvethis.index(operand)
        except ValueError:
            return 1000

    def solveEquation(self) -> int:
        while len(self.solvethis) > 1:
            if "*" in self.solvethis or "/" in self.solvethis:
                mul = self.__checkIndex("*")
                div = self.__checkIndex("/")

                if mul < div:
                    self.solveOperation(
                        self.solvethis[mul - 1: mul + 2], mul, "*"
                    )
                elif div < mul:
                    self.solveOperation(
                        self.solvethis[div - 1: div + 2], div, "/"
                    )
            elif "+" in self.solvethis or "-" in self.solvethis:
                add = self.__checkIndex("+")
                rem = self.__checkIndex("-")

                if add < rem:
                    self.solveOperation(
                        self.solvethis[add - 1: add + 2], add, "+"
                    )
                elif rem < add:
                    self.solveOperation(
                        self.solvethis[rem - 1: rem + 2], rem, "-"
                    )
        if self.solvethis[0] < 0.01 and self.solvethis[0] > -1:
            raise ValueError
        else:
            return round(self.solvethis[0], 2)

    def solveOperation(self, operation, op_index, op_type):
        if op_type == "*":
            operation.remove("*")
            result = operation[0] * operation[1]
        elif op_type == "/":
            operation.remove("/")
            result = operation[0] / operation[1]
        elif op_type == "+":
            operation.remove("+")
            result = operation[0] + operation[1]
        elif op_type == "-":
            operation.remove("-")
            result = operation[0] - operation[1]
        self.solvethis.insert(op_index - 1, result)
        del self.solvethis[op_index: op_index + 3]
