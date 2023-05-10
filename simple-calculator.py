#Ask the user which operations will be used.
operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use? ")
operation.lower()

#Ask the user to enter two (2) numbers.
if operation == 'addition':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = int(input1) + int(input2)
    print(result)

elif operation == 'subtraction':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = int(input1) - int(input2)
    print(result)

elif operation == 'multiplication':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = int(input1) * int(input2)
    print(result)

if operation == 'division':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = int(input1) // int(input2)
    print(result)
#Display Result

#Ask the user if they want to repeat the process

#If 'yes', return from step 1
#If 'no', Display "Thank you!!!", then close the program.

#ps. apply file exception functions.