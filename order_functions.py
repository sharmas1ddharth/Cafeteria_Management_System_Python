import pymysql 
from prettytable import PrettyTable 
import datetime

# function to add order details to database
def add_order_details_to_database(name, date, total_paid): 
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    sql = f"""INSERT INTO ORDERS(NAME, DATE, TOTAL_PAID)
                VALUES ('{name}', '{date}', {total_paid})
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

# function to get details from database
def get_user_details_from_database(name): 
    
    db = pymysql.connect("localhost", "root", "uttu8449", "DISHES_PRICES")
    
    cursor = db.cursor()
    
    sql = f"SELECT DATE, TOTAL_PAID, ID FROM ORDERS WHERE NAME = '{name}'"
    
    cursor.execute(sql)
    
    result = cursor.fetchall()
    for row in result:
        
        date = row[0]
        total_price = row[1]
        order_id = row[2]
    table = PrettyTable()
    
    table.field_names = ["Order ID", "Date", "Total"]
    
    table.add_row([order_id, date, total_price])
    
    print(table)
    