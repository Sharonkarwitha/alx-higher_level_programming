#!/usr/bin/python3
a = 10
b = 5

import calculator_1

sum_result = calculator_1.add(a, b)
sub_result = calculator_1.subtract(a, b)
mul_result = calculator_1.multiply(a, b)
div_result = calculator_1.divide(a, b)

print("Sum: {}".format(sum_result))
print("Subtraction: {}".format(sub_result))
print("Multiplication: {}".format(mul_result))
print("Division: {}".format(div_result))
