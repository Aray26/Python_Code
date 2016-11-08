import os
import flask
from flask import Flask

app =Flask(__name__) #builtin environment variable refers scope

#decorator 
@app.route('/')
def helloWorld():
    return "<h1>Hello World"
    
if __name__ == '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT','8080')),debug=True)
    
#http://127.0.0.1:8080/

unicode('test unicode')
    