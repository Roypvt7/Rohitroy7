n = int(input("Enter a number: "))

result = 1

for i in range(1, n+1):

  result *= i

print("The factorial of {} is {}".format(n, result))
