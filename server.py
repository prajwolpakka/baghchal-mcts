from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS from flask_cors

from mcts import MCTS
from node import Node
from state import State

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for your app

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.json
        init_board = State(
            init_board=data['state'],
            currentPlayer=data['currentPlayer'],
            goats_killed=data['goats_killed'],
            goats_placed=data['goats_placed']
        )
        # print("Initial Board State:", init_board)
        mcts = MCTS(search_limit=1000)
        node = mcts.search(Node(init_board))

        # print("Action:", action)
        # print("Final State:", final_state)

        result = {
            "player": node.last_action.player,
            "pos": node.last_action.pos,
            "next_pos": node.last_action.next_pos,
            "jumped_pos": node.last_action.jumped_pos
        }
        return jsonify(result)

    except Exception as e:
        print(str(e))
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run()







