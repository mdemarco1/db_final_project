from flask import Flask, request, jsonify
import cx_Oracle

# app = Flask(__name__)


# init oracle client
cx_Oracle.init_oracle_client(lib_dir=r"C:\\Users\\mdem1\\instantclient_21_15")
# make dsn
dsn = cx_Oracle.makedsn("csdb.csc.Villanova.edu", 1521, sid="orcl")
# connect to db user, pswd, connection

try: 
    connection = cx_Oracle.connect('mdemarc2', 'Fa02404090', dsn, encoding="UTF-8")
    print("connection successful!")
    cursor = connection.cursor()
    # practice queries!!!! #
    query = """ select addressno from address where city = :city_name"""
    querycust = """select userid from customer where name = :emal"""
    query2 = '''SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM DUAL'''
    query5 = """select addressid from address where city='Lavalette'"""
    query3 = """SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='ADDRESS'"""

    query_products = 'SELECT c.Name, p.* FROM CART ca, PRODUCT p, CUSTOMER c WHERE "Type" LIKE :type OR Brand LIKE :brand AND ca.userid = c.userid AND p.productid = c.productid'

    query = """select addressid from address where city = :1"""
    city = 'Lavalette'
    params = {'city_name': city}

    query_prod = """select productid from product where "Type" = :name"""
    # cursor.execute(query_prod, name='Shirt')

    query = "SELECT c.userid, c.name, c.email, c.phone, p.method FROM CUSTOMER c, PAYMENT p WHERE c.Name LIKE :name AND c.userid = p.userid"

    cursor.execute(query, name='John')
    # query = """
    #     SELECT c.UserID, c.Name, c.Email, p.PayID, p.Method
    #     FROM CUSTOMER c
    #     JOIN PAYMENT p ON c.UserID = p.UserID
    #     WHERE c.Name LIKE :name OR c.Email LIKE :email
    # """

    # cursor.execute(query, name='Matt DeMarco', email='')
    # cursor.execute(query_prod)
    
    # cursor.execute(query)

    # cursor.execute("""select table_name from user_tables""")
    # cursor.execute(query)

    # cursor.execute("""SELECT * FROM ADDRESS""")

    # cursor.execute("""select * from ADDRESS""")

    # Fetch and print results
    # print('curr schame', cursor.fetchone()[0])
    rows = cursor.fetchall()
    
    if rows:
        print("Address Numbers in Lavalette:")
        for row in rows:
            print(row[0])
    else:
        print("No addresses found in Lavalette.")
except cx_Oracle.DatabaseError as e:
    print('error connecting: ', e)
finally:
    if 'connection' in locals() and connection:
        connection.close()
        print('connection closed')

# @app.route('/search/customer', methods=['GET'])
# def search_customer():
#     name = request.args.get('name', '')
#     cursor = connection.cursor()

#     query = "SELECT * FROM CUSTOMER WHERE Name LIKE :name"
#     cursor.execute(query, {'name': f'%{name}%'})
#     results = cursor.fetchall()

#     # Close cursor
#     cursor.close()
#     return jsonify(results)


# @app.route('/search/product', methods=['GET'])
# def search_product():
#     product_type = request.args.get('type', '')
#     cursor = connection.cursor()

#     query = "SELECT * FROM PRODUCT WHERE Type LIKE :type"
#     cursor.execute(query, {'type': f'%{product_type}%'})
#     results = cursor.fetchall()

#     # Close cursor
#     cursor.close()
#     return jsonify(results)


# if __name__ == '__main__':
    # app.run(debug=True)



# TESTING THE CONNECTION
# try:   
#     connection = cx_Oracle.connect('mdemarc2', 'Fa02404090', dsn)
#     print("connection successful!")

#     cursor = connection.cursor()
#     # query = """ select addressno from address where city = :city_name"""
#     query = """ select * from ADDRESS"""
#     city = "Lavalette"
#     # cursor.execute(query, city_name=city)
#     # cursor.execute(query)

#     # cursor.execute("SELECT SYS_CONTEXT('USERENV', 'CURRENT_SCHEMA') FROM dual")
#     # cursor.execute("""select table_name from user_tables""")

#     cursor.execute('SELECT * FROM "ADDRESS"')

#     # cursor.execute("""select * from ADDRESS""")

#     # Fetch and print results
#     # print('curr schame', cursor.fetchone()[0])
#     rows = cursor.fetchall()
    
#     if rows:
#         print("Address Numbers in Lavalette:")
#         for row in rows:
#             print(row[0])
#     else:
#         print("No addresses found in Lavalette.")
# except cx_Oracle.DatabaseError as e:
#     print('error connecting: ', e)
# finally:
#     if 'connection' in locals() and connection:
#         connection.close()
#         print('connection closed')