from flask import Flask
import os windows

app = Flask(__name__)

@app.route("/different")
def hello():
    return "updated Flask sample application on azure hghapp service updated verrsion-4"



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6000))
    app.run(debug=True,host='0.0.0.0',port=port)
