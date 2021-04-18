from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def home():
    with open("pg1.html") as f:
        html = f.read()
    return html

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return redirect('/')
    
if __name__ =='__main__':
    app.run(host="0.0.0.0")