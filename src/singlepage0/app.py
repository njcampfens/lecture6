from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

texts = ['This is the first text of the list',
         'This is the second text of the list',
         'This is the third text of the list of texts']

@app.route('/first')
def first():
    return texts[0]

@app.route('/second')
def second():
    return texts[1]

@app.route('/third')
def third():
    return texts[2]
