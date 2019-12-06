# Data-Train-Status-Update---Susan
Data Science WEEK 1 

Linear Regression:  It is majorly used to identify the strength of the relationship between independent variables on dependent variables
Analogies include: 
To determine the strength of predictors,
To forecast an effect and trend forecasting.
Income and spending, 
Age and income 
Sales and marketing
Weather Forecast
Price forecast of a commodity

Logistic Regression predicts whether something is true or false. Its used for classification



Data Science WEEK 2

An expression is a combination of values, variables, operators, and calls to functions that need to be evaluated.

Syntax Errors are also known as parsing errors. This occurs when the parser is unable to understand a line of code. This could be due to typos, incorrect indentation or incorrect arguments.

PEP8 (Python Enhancement Proposal)  is a python style guide. It is a set of rules for how to format Python code to maximize its readability.

Linters: is a program that supports linting(i.e verifying code quality). To ensure the source code is legible, readable, less polluted and easier to maintain.

“**********”
Variable is a reserved memory location to store values. They are containers for storing data values.

Primitive built-in types are data types built into Python. This includes Integer, Float, Booleans, and Strings.

Triple Quotes are used for Multi-Line String in Python.

It returns the letter “o”.

 It returns the letter “t”.
 
 It returns the letters “ohn Smit”.
 
 print(len(name)).
 
 An escape sequence is used to escape characters e.g \n, \t, \\, \a, \f, \r, \t etc..
 4+1
print("John Smith"[1:-1]). It capitalizes the first letter of each word.




Data Science WEEK 3

They are both division operators, however “/” division gives a floating result while the “//” gives the integer part of the floating result.

1000. It means 10 raised to the power of 3.

3.

We can round using the round() function. E.g round(15.3456) or round(15.3456,2).

1.0.  It prints out 1 with a decimal 1.0.

It evaluates to true when age =>18 or age>65, when age <18 or age <65 and when both 18<=age<65.

Parameter is a variable in the declaration of a function. Argument is the actual value of this variable that gets passed to function.Parameters are placeholders for arguments e.g def sum(number) return number + number. sum(3) is the argument while 3 is the parameter.

None.

Keyword arguments are also known as **kwargs is used to pass a keyworded variable-length argument list. A keyword argument is where you provide a name to the variable as you pass it to the function. It can be thought of as a dictionary that maps a key to its values.

Parameters in functions are made optional by making it a default value
 
For unpacking the list types in a container


DATA SCIENCE WEEK 3

1. Write a function that returns the maximum of two numbers
CODE:
def max_num(a,b):
     if a > b:
          print("a is greater than b")
     else:
        print("b is greater than a")
max_num(2,3)

2. Write a function for checking the speed of drivers. This function should have one parameter: speed. 
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended”
*CODE:*
def driver_speed(speed):
    
    if speed < 70:
        print("Ok!")
   
    else:
        demerit = (speed-70)/5
        if demerit > 12:
            print("License suspended")
        else:
            print("Points: ",round(demerit))
           
driver_speed(80)

3. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. For example, if the limit is 3, it should print:0 EVEN,1 ODD,2 EVEN,3 ODD
*CODE:*
def showNumbers(limit):
  for limit in range (0,limit+1):
    if limit % 2 == 0:
      print (limit,"is an even number")
    else:
      print(limit, "is an odd number")
showNumbers(13)

#4 Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.

*CODE:*
def sum_mult(limit):
  [limit for limit in range(0,limit+1) if limit % 3 == 0 or limit % 5 == 0]
  print(sum([limit for limit in range(0,limit+1) if limit % 3 == 0 or limit % 5 == 0]))

sum_mult(20)
