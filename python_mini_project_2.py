#load Products_List.TXT
#load Couriers_List.TXT






#TAKE ME HOME SCREEN 
#LET ME EXIT A PROGRAM

products_list = ["Choco", "Milk", "Oreo"]
couriers_list = ["Hermes", "Royal", "DPP"]


operation = input('''
Pick an action to use:
1 To View the Product List
2 To View the Couriers List
3 Create a Product List and Add it to the List
4 Create a Courier List and Add it to the List
5 To Update or Delete a Product or Courier
''')

if operation == "1":
    print(
        #Product_list
        )

if operation == "2":
    print(
        #Courier_list
        )

elif operation == "3":
    #PRODUCT_LIST       .append(input("Enter a new product: "))
    # I think its "w+" is what i want but look over it in the weekend
    print(
        #PRODUCT_LIST
        )

elif operation == "4":
    #COURIER_LIST       .append(input("Enter a new product: "))
    # I think its "w+" is what i want but look over it in the weekend
    print(
        #COURIER_LIST
        )

elif operation == "5":
    
    pick update or delete:
    if update:
        if porduct

        elif COURIER_LIST

        else: 
            "Wrong input"
            "reenter input"


    elif delete:
        if product:


        elif courier_list


    else:
        "wrong input"
        "reenter input"




                
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