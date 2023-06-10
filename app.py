from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect('https://oss-frontend.onrender.com')

if __name__ == '__main__':
    app.run()
