from flask import Flask, render_template, request, jsonify 
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.j8jl3wt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '_main_':
    app.run('0.0.0.0',port=5000, debug=True)