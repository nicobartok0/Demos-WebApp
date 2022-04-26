from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

@app.route('/')
def Index():    
    return 'index'

if __name__ == '__main__':
    app.run(port=3000, debug=True)