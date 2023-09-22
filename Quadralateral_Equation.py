# Write python function to print X and Y roots of A,B and C
# Reference : Q
#Calculate the discriminant D = b^2 - 4ac.
# Compute the two solutions for x and y using the quadratic formula:
# x = (-b + √D) / (2a)
# y = (-b - √D) / (2a)
# Print the values of x and y. 

def find_roots(entries):
    arr = list(map(int, input('Enter number').split(',')))
    print(arr)