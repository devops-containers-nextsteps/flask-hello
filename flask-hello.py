from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Manas is the best in the world. Lets rock!'

@app.route('/test')
def test():
    return 'Testing hidden functionality ;)'

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
