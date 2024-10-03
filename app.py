from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dummy data storage (replace with database later)
bookings = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book_auto():
    if request.method == 'POST':
        name = request.form['name']
        pickup = request.form['pickup']
        dropoff = request.form['dropoff']
        ride_time = request.form['ride_time']
        # Store the booking data
        booking = {
            'name': name,
            'pickup': pickup,
            'dropoff': dropoff,
            'ride_time': ride_time,
            'status': 'Pending'
        }
        bookings.append(booking)
        return redirect(url_for('booking_confirmed'))
    return render_template('book.html')

@app.route('/confirmed')
def booking_confirmed():
    return render_template('confirmed.html')

# Display all bookings (for testing)
@app.route('/bookings')
def view_bookings():
    return render_template('bookings.html', bookings=bookings)

if __name__ == '__main__':
    app.run(debug=True)
