from flask import Flask, render
app = Flask(__name__)

@app.route('/')
def hello():
    return render('index.html')
