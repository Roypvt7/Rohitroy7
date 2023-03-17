n = int(input("Enter the number of terms in the series: "))

sum = 0

for i in range(1, n+1):
  sum += 1 / i

print("The sum of the harmonic series is {}".format(sum))
