
from flask import Flask, jsonify, request, Blueprint
from flask_pymongo import PyMongo
from flask_cors import CORS, cross_origin
import re
import datetime

app = Flask(__name__)
cors = CORS(app, supports_credentials=True)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/regexApp'

mongo = PyMongo(app)


@app.route('/api/', methods=['GET'])
def home_page():
    data = mongo.db.data

    result = []

    for q in data.find():
        result.append({'input1': q['input1'], 'input2': q['input2'],
                       'output': q['output'], 'createdAt': q['createdAt']})

    return jsonify({'result': result})


@app.route('/api/output', methods=['POST'])
def post_output():
    data = mongo.db.data

    # Get input from request body
    input1 = request.json['input1']
    input2 = request.json['input2']

    # Remove special characters
    input1 = re.sub('\W+', '', input1)
    input2 = re.sub('\W+', '', input2)

    numPattern = re.compile(r'\d')
    strPattern = re.compile('[A-z]{2,}')
    alphPattern = re.compile('[A-z]?')

    if(numPattern.match(input1) and numPattern.match(input2)):
        output = int(input1) + int(input2)
        output = str(output)

    elif(strPattern.match(input1) and strPattern.match(input2)):
        output = input1 + input2

    elif(alphPattern.match(input1) and alphPattern.match(input2)):
        output = ""
        in1 = ord(input1.lower())
        in2 = ord(input2.lower())

        if(in2 > in1):
            for i in range(in1, in2+1):
                output += chr(i)
        else:
            for i in range(in2, in1+1):
                output += chr(i)

    else:
        output = 'None'

    result = data.insert_one({'input1': input1, 'input2': input2,
                              'output': output, 'createdAt': datetime.datetime.now()})

    return jsonify({'result': output})


if __name__ == '__main__':
    app.run(debug='True', port=5010)
