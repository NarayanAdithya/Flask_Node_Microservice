from flask import Flask,jsonify
import requests
import json

app=Flask(__name__)
app.secret_key='687T*&(YIGDUG97987'

Data=json.load(open('flaskapp/app.json','r'))

@app.route('/')
def home():
    return jsonify({"Made By":"Adithya Narayan","Roll Number":"19BBS0068","Type":"Flask Microservice"})

@app.route('/brands')
def get_brands():
    return jsonify(Data)

@app.route('/subtraction/<int:a>/<int:b>')
def subtraction(a,b):
    return jsonify({'Answer':abs(a-b)})


@app.route('/products/<brand>')
def get_list_items(brand):
    items=requests.get('http://127.0.0.1:5001/products/{}'.format(brand))
    items=json.loads(items.text)
    return jsonify({"Products":items})


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
    