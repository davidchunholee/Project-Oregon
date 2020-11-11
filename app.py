from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index')

@app.route('/index')
def index():
    return render_template('index')

@app.route('/book_ticket')
def book_tickets():
    return render_template('book_ticket')

@app.route('/customers')
def customers():
    return render_template('customers')

@app.route('/engineer_pods')
def engineer_pods():
    return render_template('engineer_pods')

@app.route('/engineers')
def engineers():
    return render_template('engineers')

@app.route('/locations')
def locations():
    return render_template('locations')    

@app.route('/pods')
def pods():
    return render_template('pods')

@app.route('/review')
def review():
    return render_template('review')

@app.route('/ticket_response')
def ticket_response():
    return render_template('ticket_response')    

if __name__ == "__main__":
    app.run(debug=True)
