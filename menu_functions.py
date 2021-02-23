import pymysql
import datetime
from prettytable import PrettyTable 


# function to add new dish to menu
def add_menu_to_database(dish, price): 
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    sql = f"""INSERT INTO PRICE_LIST(DISHES, PRICE)
                VALUES ('{dish}', {price})
            """
    try:
        cursor.execute(sql)
        db.commit()
        message = "done"
        
    except:
        db.rollback()
        message = "error"
        
    db.close()
    
    return message


# function to edit menu item
def edit_menu_item_in_database(dish, price):
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    sql = f"""UPDATE PRICE_LIST SET PRICE = {price} WHERE DISHES = '{dish}';
            """
    try:
        cursor.execute(sql)
        db.commit()
        message = "done"
        
    except:
        db.rollback()
        message = "error"
        
    db.close()
    
    return message


# function to delete menu item
def delete_menu_item_from_database(dish):
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    sql = f"""DELETE FROM PRICE_LIST WHERE DISHES = '{dish}';
            """
    try:
        cursor.execute(sql)
        db.commit()
        message = "done"
        
    except:
        
        db.rollback()
        message = "error"
        
    db.close()
    
    return message