print("===================================")
print("-------- Simple Calculator --------")
print("===================================")
print("")
num1 = float(input("Enter First Number : "))
oper = input("Enter The Operation (+ , - , / , * , %): ")
num2 = float(input("Enter Second Number : "))
if oper == "+":
    print(f"The Sum of {num1} + {num2} is", num1 + num2)
elif oper == "-":
    print(f"The Difference of {num1} - {num2} is", num1 - num2)
elif oper == "/":
    print(f"The Division of {num1} / {num2} is", num1 / num2)
elif oper == "*":
    print(f"The Multiple of {num1} * {num2} is", num1 * num2)
elif oper == "%":
    print(f"The Modulas of {num1} % {num2} is", num1 % num2)
