from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process the data (send email, store in database, etc.)
        
        success = True
        return render_template('index.html', message_sent=True, success = success)  # Pass success flag
    else:
        return render_template('index.html', message_sent=False)  # No flag if not sent

if __name__ == '__main__':
    app.run(debug=True)
