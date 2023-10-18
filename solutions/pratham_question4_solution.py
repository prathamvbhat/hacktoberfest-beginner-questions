'''
Write a program to calculate the sum of natural numbers up to a given number.
'''

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))

sum = 0

for i in range(num1, num2+1):
    sum += i

print("Sum of natural numbers from {} to {} is {}".format(num1, num2, sum))