try:
  a=int(input("Enter the first number:"))
  b=int(input("Enter the second number:"))
  print("What operation? (+ - * /)")

  o=input("Enter Operation:")
  match o:
    case "+":
      print(f"Result: {a+b}")
    case "-":
      print(f"Result: {a-b}")
    case "*":
      print(f"Result: {a*b}")
    case "/":
      print(f"Result: {a/b}")
  

except Exception as e:
  print("Enter a valid value")
