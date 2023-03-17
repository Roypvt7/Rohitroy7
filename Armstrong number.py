def num_digits(num):
  return len(str(num))

for i in range(100, 500):
  num = i
  digits = num_digits(num)
  sum = 0


  while (num > 0):
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

  if (sum == i):
    print(i)

