d = int(input("time"))
while d!=0:
  print(d)
  d=d-1  
  a = int(input("what is your first number"))
  b = int(input("what is your second number"))
  c = input("what is your operator")
  if c == "+":
    print("Your answer is",a+b)
  elif c == "-":
    print("Your answer is",a-b)
  elif c == "*":
    print("Your answer is",a*b)
  elif c == "/":
    print("Your answer is",a/b)
  else:
    print("not an operator")