# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

# Solution
class Calculator:
    def calculate(self, a, b, operation):
        if operation == 'Addition':
            return a + b
        elif operation == 'Subtraction':
            return a - b
        elif operation == 'Multiplication':
            return a * b
        elif operation == 'Division':
            return a / b if b != 0 else "Cannot divide by zero!"
        else:
            return "Invalid operation"

# Example usage:
calc = Calculator()
print(calc.calculate(5, 3, 'Addition'))      # Output: 8
print(calc.calculate(5, 0, 'Division'))      # Output: Cannot divide by zero!