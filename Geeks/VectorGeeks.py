import numpy as np

# Horizontal Vector:

lstH = [10, 20, 30, 40, 50]

vctrH = np.array(lstH)

vctrH = np.array(lstH)

print("Vector created from a list:")
print(vctrH)

# Vertical Vector:

lstV = [[2],
        [4],
        [6],
        [10]]

vctrV = np.array(lstV)

vctrV = np.array(lstV)

print("Vector created from a list:")
print(vctrV)

# Addition, Subtraction, Multiplication, Division, Dot Operation on a Python Vector:

lst1 = [10, 20, 330, 40, 50]
lst2 = [1, 2, 3, 4, 5]


vctr1 = np.array(lst1)

vctr2 = np.array(lst2)


print("Vector created from a list 1:")
print(vctr1)
print("Vector created from a list 2:")
print(vctr2)

vctr_add = vctr1+vctr2
print("Addition of two vectors: ", vctr_add)

vctr_sub = vctr1-vctr2
print("Subtraction of two vectors: ", vctr_sub)

vctr_mul = vctr1*vctr2
print("Multiplication of two vectors: ", vctr_mul)

vctr_div = vctr1/vctr2
print("Division of two vectors: ", vctr_div)

vctr_dot = vctr1.dot(vctr2)
print("Dot product of two vectors: ", vctr_dot)
