#/restful.py

from flask import Flask, jsonify, request #import objects from the Flask model
app = Flask(__name__) #define app using Flask

@app.route('/', methods=['GET'])
def test():
    return jsonify({'Who Farted' : 'It was King Fisher!'})

@app.route('/lang', methods=['GET'])
def test2():
    return jsonify({'Who -' : 'It was the butler!'})

@app.route('/lang/joker', methods=['GET'])
def test3():
    return jsonify({'HOW' : 'Can I do it!'})
    
if __name__ == '__main__':
    app.run(debug=True, port=8080) #run app on port 8080 in debug mode