#... PART 1 ...
#... LOOPS ...

for x in range(11):
    print(x)
#...
i = 0
while i <= 10:
    print(i) 
    i += 1
#...
nums = [0, 2, 8, 20, 43, 82, 195, 204, 367]

for num in nums:
    print(num)
#...
for x in range(11):
    print(x)
else:
    print("Done!")
#...
#... Here we are looking for any items that appear in both lists
list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for word1 in list1:         # so we use a FOR loop to get each item out of the first list
    for word2 in list2:     # we then NEST another FOR loop to get each item for the second list
        if word1==word2:    # now we check if the WORD is there
            print(word1)    # using IF to then print if they are equal
            break           # THIS MAKES IT MORE EFFIECENT, so it DOESNT need to checck the rest of the list
#... 

# import random
# x = random.randint(1, 100)
# while x % 5 != 0:
#     print(x)
#     x = random.randint(1, 100)
#     if (x % 3 == 0):
#         print("Skipping")
#         continue
#
import random
while True:
    x = random.randint(1,100)
    if x % 3 == 0:
        print("Skipping Multiples of 3")
        continue
    if x % 5 == 0:
        print("Stop/Break when encountering Multipes of 5")
        break
    elif x > 0:
        print(x)
#...

#... DICTIONARIES ...
#...
car = {'brand': 'Ford','model': 'Mustang','year' : 1964,'isNew': False}
#... this lets us see the Value linked to the key
print(car["brand"])
#... here we are adding a new Key and VALUE into the Dicionary
car["colour"] = "Blue"
print(car["colour"])
#... here we UPDATE a VALUE 
car["model"] = "Shelby Mustang"
print(car["model"])
#... here we are DELETING a KEY
del car["model"]
print(car)
#... here we are trying to get the KEY and VALUES in the dictionary
for key, value in car.items():
    print(f"Key:{key}, Value: {value}")

#... FUNCTIONS

def add_numbers(a, b):
    print(a+b)

add_numbers(1,5)
#...
def add_numbers(*nums):
    total = 0
    for num in nums:
        total += num 
    print(total)
add_numbers(1,5,5)     # This is how we call a FUNC (1,5,5) is jsut an example
#... This on doesnt work properly since the PRINT STATEMENT IS INDENTED
#... so instead of getting 10 we get, 1,6,11.
def add_numbers(*nums):
    total = 0
    for num in nums:
        total += num 
        print(total)
add_numbers(1,5,5)     # This is how we call a FUNC (1,5,5) is jsut an example
#...
#...
#... Here we are using an KEY WORD ARG, this lets us put NAMED ARGUMENTS inside
#... KWARGS effectively create DICTIONARIES of KEY-VALUES arguments 
#... 
def name_age(**data):
    for key, value in data.items():
        print(f"{key} is {value}")
        
name_age(first_name = "Sedal", sec_name = "Altun", age = "26")


#...
operation = input('''
Pick an action to use:
+ for addition
- for subtraction
* for multiplication
/ for division
@ for circle\'s circumference
0 for circle\'s area
''')


if operation == '+':
    num_1 = int(input('Enter your first number: '))
    num_2 = int(input('Enter your second number: '))
    total = num_1 + num_2
    print(f" {num_1} + {num_2} = {total}")
  
elif operation == '-':
    num_1 = int(input('Enter your first number: '))
    num_2 = int(input('Enter your second number: '))
    total = num_1 - num_2
    print(f" {num_1} - {num_2} = {total}")

elif operation == '*':
    num_1 = int(input('Enter your first number: '))
    num_2 = int(input('Enter your second number: '))
    total = num_1 * num_2
    print(f" {num_1} + {num_2} = {total}")
    
elif operation == '/':
    num_1 = int(input('Enter your first number: '))
    num_2 = int(input('Enter your second number: '))
    total = num_1 / num_2
    print(f" {num_1} / {num_2} = {total}")

elif operation == "@":
    num_1 = int(input('Enter the Circle\'s radius: '))
    total = num_1 * 3.14 * 2
    print(f" IF The radius is {num_1}, The Circumference will be {total}")
    
elif operation == "0":
    num_1 = int(input('Enter the Circle\'s radius: '))
    total = (num_1 ** 2) * 3.14
    print(f" IF The radius is {num_1}, The Area will be {total}")

else:
    print('You have not typed a valid operator, please run the program again.')

