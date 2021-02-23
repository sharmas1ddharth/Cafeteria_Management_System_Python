import pymysql 
from prettytable import PrettyTable 
import datetime
from menu_functions import add_menu_to_database, edit_menu_item_in_database, delete_menu_item_from_database
from order_functions import add_order_details_to_database, get_user_details_from_database


# function to get current date
def date_now(): 
    
    now = datetime.datetime.now()
    date_format = now.strftime("%d-%m-%Y")
    
    return date_format


# function to get current time
def time_now(): 
    
    now = datetime.datetime.now()
    time_format = now.strftime("%I:%M %p")
    
    return time_format


# function for admin account
def admin_account(): 
    
    print("Command List => Press '1' for add dish to menu,")
    
    print("\t\tPress '2' for edit price,") 
    
    print("\t\tPress '3' for delete item from menu")
    
    print("\t\tPress 'q' to exit")
    
    admin_input = input("Enter command : ")
    
    if admin_input == '1':
        dish = input("Enter new dish : ")
        price = int(input("Enter price for new dish : "))
        add_menu_to_database(dish, price)
    
    elif admin_input == '2':
        dish = input("Enter dish name for which you want to change price : ")
        price = int(input("Enter new price for dish : "))
        edit_menu_item_in_database(dish, price)
        
    elif admin_input == '3':
        dish = input("Enter dish name which you want to delete : ")
        delete_menu_item_from_database(dish)

    elif admin_input == 'q':
        select_input(command=)
        

# function to take user input
def select_input(my_input): 
    
    if my_input == '1':
        output = view_menu()
    
    elif my_input == '2':
        output = add_order()
    
    elif my_input == '3':
        name = input("Enter name of the person : ")
        print()
        output = get_user_details_from_database(name)
        
    else:
        
        output = "Error : Please Enter Correct Command"    
    return output


# function for adding order details
def add_order(): 
    
    name = input("Name of the person : ")
    
    date = date_now()
    
    time = time_now()
    
    total_price = get_total_price()
    
    bill = f"-----------------\nYour Bill {name}\n------------------\nTotal = {total_price}\nDate : {date}\nTime : {time}\n\n"
    
    date_time = f"{date}, {time}"
    
    add_order_details_to_database(name, date_time, total_price)
    
    print(bill)
    

# function to view menu
def view_menu():
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    table2 = PrettyTable()
    
    table2.field_names = ["Dish", "Price"]
    
    sql = "SELECT * FROM PRICE_LIST"
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        
        for row in results:
            dish = row[0]
            price = row[1]
            table2.add_row([dish, price])
        print(table2)   
                 
    except:
        print("Error Can't show menu")
        
    db.close()
    

# function to get price from database
def get_price_from_database(dish):
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    sql = f"SELECT PRICE FROM PRICE_LIST WHERE DISHES = '{dish}'"
    
    cursor.execute(sql)
    
    result = cursor.fetchall()
    
    for row in result:
        price = row[0]
        
    return price


# fuction to add total price
def get_total_price():
    
    price_list = []
    
    print()
    
    dish = input("What you want to eat ? : ")
    
    while dish != "":
        dish_price = get_price_from_database(dish)
        price_list.append(dish_price)
        print()
        dish = input("Anything else ? : ")
        print()
    total_price = sum(price_list)
    
    return total_price



if __name__ == "__main__":
    
    print("---------------------------------------------------------------------CAFETERIA MANAGEMENT SYSTEM---------------------------------------------------------------------")
    
    print()
    
    print("===============================================")
    
    print("Command List => Press '1' for menu,")
    
    print("\t\tPress '2' to add order,") 
    
    print("\t\tPress '3' to view order")
    
    print("\t\tPress 'q' to exit")
    
    print("===============================================")
    
    print()
    
    # take input from user
    command = input("Enter command : ")
    
    print()

    # loop to get command 
    while command != "q":
        
        if command == '0':
            admin_account()
            
        elif command == '1' or '2' or '3':
            select_input(command)
            
        else:
            print("Error : Please enter correct command") 
            
        print("------------------------------------------------------------------------------------------------------")
        
        print()
        
        command = input("Enter command : ")
        
        
    # exit message
    print("Thank you for using this project | This project is created by => Shashwat Dubey, Subrat Rathore")
