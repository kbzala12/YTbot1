from flask import Flask
app = Flask('')
@app.route('/')
def home():
    return "Alive"

if __name__ == '__main__':
    app.run()