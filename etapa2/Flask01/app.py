from flask import Flask 

app = Flask(__name__)

@app.route('/')
def HelloWord():
    return 'Hello Word!'

@app.route('/nome')
def Nome():
    return 'Clara Lima'

if __name__ == '__main__':
    app.run(debug = True)