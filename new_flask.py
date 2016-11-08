from flask import Flask

app = Flask(__name__)
#app.config.from_object('config')

#@app.route("/")
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello Earth One'

if __name__ == '__main__':
    app.run(debug=True)