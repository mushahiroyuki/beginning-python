#ファイル名 Chapter15/1504flask2.py
from flask import Flask
app = Flask(__name__)

@app.route('/powers')
def powers(n=10):
    return ', '.join(str(2**i) for i in range(n))
