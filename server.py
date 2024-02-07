from flask import Flask, jsonify, request
from flask_cors import CORS

from mcts import MCTS
from node import Node
from state import State

# Initialize Flask app
app = Flask(__name__)
# Enable Cross-Origin Resource Sharing (CORS) for allowing requests from other origins
CORS(app) 

@app.route('/process', methods=['POST'])
def process():
    """
    Endpoint to process the game state and return the next move.

    Returns:
        jsonify: JSON response containing the next move.
    """
    try:
        # Extract game state data from the request
        data = request.json
        init_board = State(
            init_board=data['state'],
            currentPlayer=data['currentPlayer'],
            goats_killed=data['goats_killed'],
            goats_placed=data['goats_placed']
        )

        # Initialize Monte Carlo Tree Search (MCTS) with search limit of 1000 iterations
        mcts = MCTS(search_limit=1000)
        # Perform MCTS search to determine the next move
        node = mcts.search(Node(init_board))

        # Extract information about the next move
        result = {
            "player": node.last_action.player,
            "pos": node.last_action.pos,
            "next_pos": node.last_action.next_pos,
            "jumped_pos": node.last_action.jumped_pos
        }
        # Return JSON response containing the next move
        return jsonify(result)

    except Exception as e:
        # Handle any exceptions and return error response
        print(str(e))
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    # Run the Flask app
    app.run()
