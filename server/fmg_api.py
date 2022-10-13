from flask import Flask

app = Flask(__name__)

@app.route("/")
def fmg_home():
    return "find my grandpa"

app.run(host='0.0.0.0', port=80)
