from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

connection_string = ""
with open("mongoDB_connectionString") as f:
    connection_string = f.read()
db_client = MongoClient(connection_string)
db = db_client['test1']
collection = db['test1_collect']

# ROUTES

@app.route('/', methods=['GET'])
def home() :
    return "Welcome to the home page"

@app.route('/users', methods=['GET'])
def getall_users() :
    users = []
    for u in collection.find() :
        u['_id'] = str(u['_id'])
        users.append(u)
    return jsonify(users)


if __name__ == "__main__" : 
    app.run()