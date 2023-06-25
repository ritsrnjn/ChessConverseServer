from flask import Blueprint, request, jsonify

botplayer_api = Blueprint('botplayer_api', __name__)


@botplayer_api.route('/move', methods=['POST'])
def move():
  data = request.get_json()
  source_square = data['sourceSquare']
  target_square = data['targetSquare']
  fen = data['fen']

  # Reverse the strings
  reversed_source_square = source_square[::-1]
  reversed_target_square = target_square[::-1]
  reversed_fen = fen[::-1]

  response = {
    'sourceSquare': reversed_source_square,
    'targetSquare': reversed_target_square,
    'fen': reversed_fen
  }

  return jsonify(response)
