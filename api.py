#pip install flask
#pip install requests
from flask import Flask

app = Flask (__name__)

@app.route('/bem vindo', methods= ['GET'])
def sejaBemVindoGet():
    return 'Bem vindo a nossa primeira api'

@app.route('/bem vindo', methods= ['POST'])
def sejaBemVindoPost():
    return 'Bem vindo a nossa primeira api'

@app.route('/bem vindo', methods= ['PUT'])
def sejaBemVindoPut():
    return 'Bem vindo a nossa primeira api'

@app.route('/bem vindo', methods= ['DELETE'])
def sejaBemVindoDelete():
    return 'Bem vindo a nossa primeira api'



if __name__ =='__main__':
    app.run(host='0.0.0.0', port=105)
