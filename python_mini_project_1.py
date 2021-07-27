user_list = ["Choco", "Milk", "Oreo"]


operation = input('''
Pick an action to use:
1 To View the Product List
2 To Create a Product and Add it to the List
3 To View All Products
4 To Update or Delete a Product
''')

if operation == "1":
    print(user_list)

elif operation == "2":
    user_list.append(input("Enter a new product: "))
    print(user_list)

elif operation == "3":
    print(user_list)

elif operation == "4":
    update_delete = input('''
    Pick an action
    1 To Update
    2 To Delete
    ''')
    if update_delete == "1":
        print(user_list)
        list_num = input("Enter List number you want to Update (Remember list Items start at 0): ")
        user_list[int(list_num)] = input("Input your UPDATED Product: ")
        print(user_list)
        
    elif update_delete == "2":
        print(user_list)
        list_num = int(input("Enter List number you want to Remove (Remember list Items start at 0): "))
        user_list.pop(list_num) 
        #... This code below will give us the ITEM that we POPPED/REMOVED # THIS DOESNT WORK 
        #... user_list = user_list.pop(list_num)       # BIG BRIAN CONFUSED
        print(user_list)
    
    else:
        print("Wrong Input")

else:
    print("Wrong Input")

# #... ADD A UI AND A GO BACK TO HOMEBACK OPTION.
# #... FIX THE 4.2 ELIF STATEMENTS to also show whats been REMOVED from the LIST
