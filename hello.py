from flask import Flask
app = Flask(__name__)

def sum(a, b):
    return a + b
@app.route('/')

def hello():
    return {"message": sum(2,3)}
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
