firstnumber = input("Enter Your First Number:" )
secondnumber = input("Enter Your Second Number:" )
operation = input("Enter Your Operation:" )

# print("Your Answer is:", int(firstnumber)+operation+int(secondnumber), "For", operation, "Operation")

Sum = firstnumber+secondnumber
Subtraction = firstnumber-secondnumber
Multiplication = firstnumber*secondnumber
Division = firstnumber/secondnumber


if operation == "+":
    print("Your Answer is:", int(Sum), "For")

if operation == "-":
    print("Your Answer is:",int(Subtraction))

if operation == "*":
    print("Your Answer is:", int(Multiplication))

if operation == "/":
    print("Your Answer is:", int(Division))
