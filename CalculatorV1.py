print("Calculator")
print("The operators are: add, raise to the power of, subtract, multiply and divide. You have to type these in the exact way as shown here otherwise the calculator will not work")
num1 = float(input("Please type in the first number of the equation: "))
num2 = float(input("Please type in the second number of the equation: "))
oper = input("Please type in what operator you would like to use in the equation: ")

if oper == "add":
  print(f"The answer is: {num1 + num2}")  
  
elif oper == "raise to the power of":
  print(f"The answer is: {num1 ** num2}")

elif oper == "subtract":
  print(f"The answer is: {num1 - num2}")

elif oper == "mulitply":
  print(f"The answer is: {num1 * num2}") 

elif oper == "divide":
  if num2 == 0:
    print("You cannot divide by 0")
  else:
    print(f"The answer is: {num1 / num2}")

  
  
