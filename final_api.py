from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cx_Oracle


app = Flask(__name__, template_folder='template')
CORS(app)

username = 'mdemarc2'
Password = 'Fa02404090'
intstant_client_dir="path_to_instant_client"

# init oracle client
cx_Oracle.init_oracle_client(lib_dir=r"C:\\Users\\mdem1\\instantclient_21_15")
# make dsn
dsn = cx_Oracle.makedsn("csdb.csc.Villanova.edu", 1521, sid="orcl")
# connect to db user, pswd, connection, should do this in a try block
try:
    connection = cx_Oracle.connect(username, Password, dsn, encoding="UTF-8")
    print('connected to database')
except cx_Oracle.DatabaseError as e:
    print('Error: ', e)

# serve HTML page
@app.route('/')
def index():
    return render_template('customer_page.html')

@app.route('/search/customer', methods=['GET'])
def search_customer():
    name = request.args.get('name', '')
    cursor = connection.cursor()

    query = "SELECT c.userid, c.name, c.email, c.phone, p.method FROM CUSTOMER c, PAYMENT p WHERE c.Name LIKE :name AND c.userid = p.userid"
    cursor.execute(query, {'name': f'%{name}%'})
    results = cursor.fetchall()

    # Close cursor
    cursor.close()
    print('connection closed')
    return jsonify(results)


@app.route('/search/product', methods=['GET'])
def search_product():
    product_type = request.args.get('type', '')
    cursor = connection.cursor()

    query = 'SELECT DISTINCT c.Name, p.* FROM CART ca, PRODUCT p, CUSTOMER c WHERE ("Type" LIKE :type OR Brand LIKE :brand) AND ca.userid = c.userid AND p.productid = ca.productid'
    cursor.execute(query, {'type': f'%{product_type}%', 'brand': f'%{product_type}%'})
    results = cursor.fetchall()

    # Close cursor
    cursor.close()
    print('connection closed')
    return jsonify(results)

@app.route('/search/purchases', methods=['GET'])
def search_purchases():
    name = request.args.get('name', '')
    email = request.args.get('email', '')
    cursor = connection.cursor()

    # SQL query to join CUSTOMER and PAYMENT tables
    query = """
        SELECT c.UserID, c.Name, c.Email, p.PurchaseID, p.ProductName, p.Amount, p.Date
        FROM CUSTOMER c
        JOIN PAYMENT p ON c.UserID = p.UserID
        WHERE c.Name LIKE :name OR c.Email LIKE :email
    """
    cursor.execute(query, {'name': f'%{name}%', 'email': f'%{email}%'})
    results = cursor.fetchall()

    # Format results as a list of dictionaries for easy JSON conversion
    purchases = [
        {
            'UserID': row[0],
            'Name': row[1],
            'Email': row[2],
            'PurchaseID': row[3],
            'ProductName': row[4],
            'Amount': row[5],
            'Date': row[6]
        }
        for row in results
    ]

    # Close cursor
    cursor.close()
    return jsonify(purchases)

@app.route('/insert/customer', methods=['POST'])
def insert_customer():
    try:
        data = request.json
        name = data['name']
        email = data['email']
        phone = data['phone']

        cursor = connection.cursor()

        # Get the next UserID (manual handling)
        cursor.execute("SELECT NVL(MAX(UserID), 0) + 1 FROM CUSTOMER")
        next_user_id = cursor.fetchone()[0]

        # Insert new customer
        query = """
            INSERT INTO CUSTOMER (UserID, Name, Email, Phone)
            VALUES (:userid, :name, :email, :phone)
        """
        cursor.execute(query, {
            'userid': next_user_id,
            'name': name,
            'email': email,
            'phone': phone
        })

        connection.commit()
        
        cursor.close()
        return jsonify({'message': 'Customer inserted successfully!'}), 201

    except cx_Oracle.DatabaseError as e:
        print("Error: ", e)
        return jsonify({'error': 'Failed to insert customer'}), 500


if __name__ == '__main__':
    app.run(debug=True)


