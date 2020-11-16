from flask import Flask, render_template
from db_connector import connect_to_database, execute_query

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/book_ticket.html')
def book_tickets():
    return render_template('book_ticket.html')

@app.route('/customers.html')
def customers():
    db_connection = connect_to_database()
    query = "SELECT customerID, firstName, lastName, currentPod, destination FROM Customers;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('customers.html', rows=result)

@app.route('/engineer_pods.html')
def engineer_pods():
    db_connection = connect_to_database()
    query = "SELECT engineerID, podID FROM Engineer_Pods;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('engineer_pods.html', rows=result)

@app.route('/engineers.html')
def engineers():
    db_connection = connect_to_database()
    query = "SELECT engineerID, firstName, lastName, available FROM Service_Engineers;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('engineers.html', rows=result)

@app.route('/locations.html')
def locations():
    db_connection = connect_to_database()
    query = "SELECT locationID, description FROM Locations;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('locations.html', rows=result)

@app.route('/pods.html')
def pods():
    db_connection = connect_to_database()
    query = "SELECT podID, operableStatus, seatCapacity, availableSeat, inTransition, currentLocation FROM Transport_Pods;"
    result = execute_query(db_connection, query).fetchall()
    print(result)
    return render_template('pods.html', rows=result)

@app.route('/review.html')
def review():
    return render_template('review.html')

@app.route('/ticket_response.html')
def ticket_response():
    return render_template('ticket_response.html')    

if __name__ == "__main__":
    app.run(debug=True)
