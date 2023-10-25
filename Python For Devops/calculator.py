num1 = int(input("Enter num 1 : "))
num2 = int(input("Enter num 2 : "))

print("Please select the operation : + - * /")

print("Your choice =")
choice = input()

if choice == "+":
    print("Addition =", num1 + num2)
elif choice == "-":
    print("Subtraction =", num1 - num2)
elif choice == "*":
    print("Multiplication =", num1 * num2)
elif choice == "/":
    print("Division =", int(num1 / num2))
else: 
    print("Invalid Choice")