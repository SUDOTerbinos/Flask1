from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print('how are you')
    x=input()
    if x == 'i am fine':
        print('it is good')
    else:
        print('ohh sorry')
    