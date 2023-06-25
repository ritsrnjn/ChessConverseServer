from flask import Flask
from botplayer import botplayer_api

app = Flask(__name__)
app.register_blueprint(botplayer_api)


@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
