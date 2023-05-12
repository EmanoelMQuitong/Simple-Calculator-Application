#Colors and text forms
BLUE = '\033[94m'
DARKCYAN = '\033[36m'
PURPLE = '\033[95m'
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

#Ask the user which operations will be used.
print('\n')
ch = '#'
BORDER = ch*200
print(BOLD+PURPLE+BORDER+END)
print('\n')

try:
    operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use? ")
except ValueError:
    print(BOLD + RED + "Sorry! Only strings are allowed"+ END )
    BORDER
    
if operation.lower() != 'addition' and operation.lower() != 'subtraction' and operation.lower() != 'multiplication' and operation.lower() != 'division':
    raise Exception(BOLD + RED +"Please only enter the qouted words among the choices."+ END)


print('\n')
#Ask the user to enter two (2) numbers.

if operation.lower() == 'addition':
    
    try:
        print(BOLD+BLUE+"Enter your first number:"+END)
        input1 = input(" ")
           
        print(BOLD+BLUE+"Enter your second number:"+END)
        input2 = input(" ")
        result = float(input1) + float(input2)
    
    except ValueError:
        print('\n')
        print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

    except TypeError:
        print('\n')
        print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

    result = "%.3f"%result
    result = input1 ,"+",input2,"=", result
    print('\n')
    print(result)

elif operation.lower() == 'subtraction':
    print(BOLD+BLUE+"Enter your first number:"+END)
    try:
        print(BOLD+BLUE+"Enter your first number:"+END)
        input1 = input(" ")
           
        print(BOLD+BLUE+"Enter your second number:"+END)
        input2 = input(" ")
        result = float(input1) - float(input2)
    
    except ValueError:
        print('\n')
        print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

    except TypeError:
        print('\n')
        print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )
    
    result = "%.3f"%result
    result = input1 ,"-",input2,"=", result
    print('\n')
    print(result)
   

elif operation.lower() == 'multiplication':
    try:
        print(BOLD+BLUE+"Enter your first number:"+END)
        input1 = input(" ")
           
        print(BOLD+BLUE+"Enter your second number:"+END)
        input2 = input(" ")
        result = float(input1) * float(input2)
    
    except ValueError:
        print('\n')
        print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

    except TypeError:
        print('\n')
        print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

    result = "%.3f"%result
    result = input1 ,"/",input2,"=", result
    print('\n')
    print(result)

if operation.lower() == 'division':
    try:
        print(BOLD+BLUE+"Enter your first number:"+END)
        input1 = input(" ")
           
        print(BOLD+BLUE+"Enter your second number:"+END)
        input2 = input(" ")
        result = float(input1) / float(input2)
    
    except ValueError:
        print('\n')
        print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

    except TypeError:
        print('\n')
        print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

    result = "%.3f"%result
    result = input1 ,"/",input2,"=", result
    print('\n')
    print(result)

print('\n')
print(BOLD+PURPLE+BORDER+END)
print('\n')

try:
    response = input("Would you like to repeat the process? Type'yes' to proceed, enter 'no' if not.")

except TypeError:
    print('\n')
    print(BOLD + RED + "Sorry! Only strings are allowed"+ END )





#Ask the user if they want to repeat the process
while response.lower() == 'yes':
    print('\n')
    try:
        operation = input("Which operation ('addition', 'subtraction', 'multiplication' or 'division') would you like to use? ")
    except ValueError:
        print(BOLD + RED + "Sorry! Only strings are allowed"+ END )
    
    if operation.lower() != 'addition' and operation.lower() != 'subtraction' and operation.lower() != 'multiplication' and operation.lower() != 'division':
        raise Exception(BOLD + RED +"Please only enter the qouted words among the choices."+ END)

    print('\n')


    if operation.lower() == 'addition':
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            input2 = input(" ")
            result = float(input1) + float(input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )

        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )

        result = "%.3f"%result
        result = input1 ,"+",input2,"=", result
        print('\n')
        print(result)
        

    elif operation.lower() == 'subtraction':
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            input2 = input(" ")
            result = float(input1) - float(input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )
        
        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )
    
        result = "%.3f"%result
        result = input1 ,"-",input2,"=", result
        print('\n')
        print(result)
        

    elif operation.lower() == 'multiplication':
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            input2 = input(" ")
            result = float(input1) * float(input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )
        
        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )
    
        result = "%.3f"%result
        result = input1 ,"x",input2,"=", result
        print('\n')
        print(result)

    if operation.lower() == 'division':
        try:
            print(BOLD+BLUE+"Enter your first number:"+END)
            input1 = input(" ")
           
            print(BOLD+BLUE+"Enter your second number:"+END)
            input2 = input(" ")
            result = float(input1) / float(input2)
    
        except ValueError:
            print('\n')
            print(BOLD + RED + "Sorry! Only integers and floats are allowed"+ END )
        
        except TypeError:
            print('\n')
            print(BOLD + RED + "Non-integer and non-float are cannot be used."+ END )
        

        result = "%.3f"%result
        result = input1 ,"/",input2,"=", result
        print('\n')
        print(result)   
    
    response = input("Would you like to repeat the process? Type'yes' to proceed, enter 'no' if not.")
    response.lower()

    print('\n')
    print(BOLD+PURPLE+BORDER+END)
    print('\n')
    

    if response.lower() == 'no':
        print("End of program")
        
if response.lower() == 'no':
    print("End of program")

if response.lower() != 'yes' and response.lower() != 'no':
    raise Exception(BOLD + RED +"Please only enter the qouted words among the choices."+ END)



#ps. apply file exception functions.