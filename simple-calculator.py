#Colors and text forms
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

#Ask the user which operations will be used.
try:
    operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use? ")
except ValueError:
    print(BOLD + RED + "Sorry! Only strings are allowed"+ END )
    
if operation.lower() != 'addition' and operation.lower() != 'subtraction' and operation.lower() != 'multiplication' and operation.lower() != 'division':
    raise Exception(BOLD + RED +"Please only enter the qouted words among the choices."+ END)


#Ask the user to enter two (2) numbers.

if operation.lower() == 'addition':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = float(input1) + float(input2)
    result = "%.3f"%result
    print(BOLD + input1 ,"+",input2,"=", result + END)

elif operation.lower() == 'subtraction':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = float(input1) - float(input2)
    result = "%.3f"%result
    print(BOLD + input1 ,"-",input2,"=", result + END)
   

elif operation.lower() == 'multiplication':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = float(input1) * int(input2)
    result = "%.3f"%result
    print(BOLD + input1 ,"x",input2,"=", result + END)

if operation.lower() == 'division':
    input1 = input("Enter your first number: ")
    input2 = input("Enter your second number: ")
    result = float(input1) / float(input2)
    result = "%.3f"%result
    print(BOLD + input1 ,"/",input2,"=", result + END)

response = input("Would you like to repeat the process? Type'yes' to proceed, enter 'no' if not.")
response.lower()

#Ask the user if they want to repeat the process
while response.lower() == 'yes':
    operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use? ")
    operation.lower()

    if operation.lower() == 'addition':
        input1 = input("Enter your first number: ")
        input2 = input("Enter your second number: ")
        result = float(input1) + float(input2)
        result = "%.3f"%result
        print(BOLD + input1 ,"+",input2,"=", result + END)
        

    elif operation.lower() == 'subtraction':
        input1 = input("Enter your first number: ")
        input2 = input("Enter your second number: ")
        result = float(input1) - float(input2)
        result = "%.3f"%result
        print(BOLD + input1 ,"-",input2,"=", result + END)
        

    elif operation.lower() == 'multiplication':
        input1 = input("Enter your first number: ")
        input2 = input("Enter your second number: ")
        result = float(input1) * float(input2)
        result = "%.3f"%result
        print(BOLD + input1 ,"x",input2,"=", result + END)

    if operation.lower() == 'division':
        input1 = input("Enter your first number: ")
        input2 = input("Enter your second number: ")
        result = float(input1) / float(input2)
        result = "%.3f"%result
        print(BOLD + input1 ,"/",input2,"=", result + END)   
    
    response = input("Would you like to repeat the process? Type'yes' to proceed, enter 'no' if not.")
    response.lower()

    if response.lower() == 'no':
        print("End program")
        
if response.lower() == 'no':
    print("End program")



#ps. apply file exception functions.