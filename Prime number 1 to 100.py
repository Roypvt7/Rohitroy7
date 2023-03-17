start = 1
end = 100

for number in range(start, end + 1):
  is_prime = True

  for divisor in range(2, number):
    if number % divisor == 0:
      is_prime = False
      break

  if is_prime:
    print(number)
