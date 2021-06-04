import flask
from flask import request, jsonify
import controller

app = flask.Flask(__name__)
conf_path = "confs/conf.json"
controller.SetupBoard(conf_path)


@app.route('/', methods=['POST'])
def home():
    try:
        request_data = request.get_json(force=True)
        task = controller.Request_handler(request_data)
        result = jsonify(task.asCard())  # Returns the created card
        return result, 201
    except Exception:
        return "400 - Bad parameters\n", 400


app.run(host="localhost", port=3000, debug=True)
