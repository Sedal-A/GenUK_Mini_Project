#... PART 1 ...
#... STRINGS ...

first_name = "Sedal"
last_name = "Altun"

print(first_name)
print(last_name)

print(f"Hello, my name is {first_name} {last_name}.")

#... INTEGERS ...

x = 5
y = 10
product = x + y

print(product)
print(f"The product of {x} and {y} is {product}")
print(type(product))

#... LISTS ...

people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

third_person = people[2]
print(third_person)

third_last_person = people[-3]
print(third_last_person)

specific_names = people[2:-1]
print(specific_names)
specific_names_2 = people[2:6]
print(specific_names_2)
#... SAME CODE BELOW ...
x_people = people[0]
y_people = people[-1]
product_people = x_people == y_people
print(product_people)
#... THEY ALL DO THE SAME THING ...
product_people_2 = people[0] == people[-1]
print(product_people_2)
#... BUT ITS JUST CLEANER ...
print(people[0] == people[-1])

#... INPUT ...

name = input("Enter your name: ")
print("Welcome back", name)

x_input = input("Enter a number: ")
y_input = input("Enter a second number: ")
input_product = x_input + y_input
print(input_product)
#... x = 5, y = 6. This gives us 56 ...
print(type(input_product))
#... we get 56 since it SEE it as a STR ...
number = input("Enter a number:")
number = int(number)
#... here we are changing the type to INT from STR ...
print(number)
print(type(number))
#... so to get 2 INPUTS and + them we need to convert to INT/FLOAT from STR ...
x_input = int(input("Enter a number: "))
y_input = int(input("Enter a second number: "))
#... here we changed the VAR type from STR to INT ...
input_product = x_input + y_input
#... we couldnt change it here since the + will already have taken place ...
print(input_product)
print(type(input_product))
#... This ALSO WORKS, but the example above is cleaner ...
x_input = input("Enter a number: ")
y_input = input("Enter a second number: ")
input_product = int(x_input) + int(y_input)
print(input_product)
print(type(input_product))

x_input_2 = int(input("Enter a number: "))
y_input_2 = int(input("Enter a second number: "))
print(x_input_2 == y_input_2)



#... PART 2 ...

equal_or_nah = int(input("Enter a number: "))

if equal_or_nah % 4 == 0:
    print(equal_or_nah, "Is a Multiple of 4 so therefor its also an Even number")
elif equal_or_nah % 2 == 0:   
    print(equal_or_nah, "Is a Even number")
else:
    print(equal_or_nah, "ISN'T a Even number")
#...
fizz_or_buzz = int(input("Enter a number: "))

if fizz_or_buzz % 15 == 0:
    print(fizz_or_buzz, "Since its a Multiple of 3 and 5 we get Fizz and Buzz")
elif fizz_or_buzz % 3 == 0:
    print("Fizz")
elif fizz_or_buzz % 5 == 0:
    print("Buzz")
else:
    print(fizz_or_buzz, "ISN'T a Multiple of 3 or 5")



#...
degree = input("Enter eitehr C for Celsius or F for Fahrenheit: ")
temp_num = int(input("Enter your temperature: "))

if degree == "c" or degree == "C":
    converted_num =((temp_num * 1.8) + 32)
    print(f"{temp_num}C converts to {converted_num}F")
elif degree == "f" or degree == "F":
    converted_num =((temp_num - 32) / 1.8)
    print(f"{temp_num}F converts to {converted_num}C")
else:
    print("Incorrect temperature Input")
#... The one above and below are the same code the only difference is we ask for the
#... INPUTs before we start the calculations, whereas below we ask for the DEGREE then 
#... get an INPUT in each IF statement, Above is 1 line less PLUS it looks a bit cleaner
#... since if we HAVE to enter the INPUT in each IF statement the code will become longer.
c_or_f = input("Enter C - convert Celsius to Fahrenheit or Enter F - convert Fahrenheit to Celsius: ")

if c_or_f == "C" or c_or_f == "c":
    temp = float(input("Enter your Temperature: "))
    c_to_f = (temp * 1.8) + 32
    print(f"Your {temp}C is {c_to_f}F")
elif c_or_f == "F" or c_or_f == "f":
    temp = float(input("Enter your Temperature: "))
    f_to_c = (temp - 32) / 1.8
    print(f"Your {temp}F is {f_to_c}C")
else:
    print("Incorrect Input")



#... PART 3 ...

# LOGICAL OPERATORS ​
# AND - if BOTH are TRUE
# OR - if ONE is TRUE 
# NOT - if NEITHER is TRUE

#   a = False
#   b = False
#   x = not(a)
#   y = not(b)
#   print(a or b) ==> False 
#   print(x or y) ==> True
#   print(a or x) ==> True
#   print(x or b) ==> True

#   a = False
#   b = False
#   x = not(a)
#   y = not(b)
#   print(a and b) ==> False
#   print(a and x) ==> Fasle
#   print(y and b) ==> Fasle
#   print(x and y) ==> True

#... IF we use IF instead of ELIF and ELSE, EXMAPLE BELOW
#... Here we put the highest value at the front of the IF statement
#... putting it at the front allows our INPUT (if they hit all criteria)
#... to jsut run to top IF, now if we did it so the highest criteria was 
#... at the bottom our result would print each statement. 
age = int(input("Enter your age: "))
salary = int(input("Enter your salary: £"))

if age >= 30 and salary >= 50000:
    print("We can offer you a loan of up to £100,000")
elif age >= 30 and salary >= 35000:
    print("We can offer you a loan of up to £75,000")
elif age >= 21 and salary >= 21000:
    print("We can offer you a loan of up to £50,000")
else:
    print("Sorry we cant offer you a loan")

# age = int(input("Enter your age: "))
# salary = int(input("Enter your salary: £"))

# if age >= 21 and salary >= 21000:
#     print("We can offer you a loan of up to £50,000")
# if age >= 30 and salary >= 35000:
#     print("We can offer you a loan of up to £75,000")
# if age >= 30 and salary >= 50000:
#     print("We can offer you a loan of up to £100,000")
# else:
#     print("Sorry we cant offer you a loan")
# 
# ==> 
# 
# Enter your age: 35
# Enter your salary: £65000
# We can offer you a loan of up to £50,000
# We can offer you a loan of up to £75,000
# We can offer you a loan of up to £100,000






