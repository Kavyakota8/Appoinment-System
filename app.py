from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        purpose = request.form['purpose']
        appointments.append({
            "name": name,
            "email": email,
            "date": date,
            "time": time,
            "purpose": purpose
        })
        return redirect(url_for('success'))
    return render_template('book.html')

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/appointments')
def view_appointments():
    return render_template('appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
