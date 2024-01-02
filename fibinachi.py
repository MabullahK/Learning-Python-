def Fibonacci(i):
  if i <= 1:
    return i
  else:
    return (Fibonacci(i-1) + Fibonacci(i-2))

i = int(input("Enter a number: "))
for j in range(i):
  print(Fibonacci(j))
