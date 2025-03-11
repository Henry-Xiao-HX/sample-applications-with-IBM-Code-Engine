from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.debug = True

def askWatsonx(question):
   answer = "I don't know!" #replace this with call to watsonx
   return answer

@app.route('/')
def welcome():
   return 'Welcome to my Python Flask Server'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

@app.route('/watsonx', methods = ['GET', 'POST'])
def watsonx():
   if request.method == 'POST':
      input = request.json   #user input
      question = input['question']
      answer = askWatsonx(question)
      return answer
   else:
      return "Send me a POST request with a question for watsonx!"
   
if __name__ == '__main__':
    app.run(debug=True,port=8080,host='0.0.0.0')