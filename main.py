from flask import Flask

if __name__ == "__main__":
    app = Flask(__name__)
    print("teste")
    app.run(debug=True)
