## recursive function ##

def factorial(i):
  if i == 1:
    return i
  else:
    return i * factorial(i-1)

i = int(input("Enter a number: "))
print(factorial(i))
