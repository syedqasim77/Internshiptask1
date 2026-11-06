num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Additton: ", num1+num2)
print("Subtraction:", num1-num2)
print("Multiplication:", num1*num2)
print("Division", num1/num2)

if num2 != 0:
    print("Division:", num1/num2)
    print("Modulus:", num1%num2)
    
else:
    print("Division is not possible by 0")
    print("Modulus is not possible by 0")