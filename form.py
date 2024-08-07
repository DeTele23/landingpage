from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # Handle both GET and POST
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Do something with the data (e.g., send an email)
        return render_template('contact_success.html')  # Or another response
    else:  # GET request
        return render_template('contact.html')  # Render the form

if __name__ == '__main__':
    app.run(debug=True)
