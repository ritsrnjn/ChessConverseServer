from flask import Flask
from botplayer import botplayer_api

app = Flask(__name__)
app.register_blueprint(botplayer_api)


@app.route('/')
def index():
    return 'Testing if being auto updated!'


app.run(host='0.0.0.0', port=81)
