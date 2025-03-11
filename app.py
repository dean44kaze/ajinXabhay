from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import random
import solver  # Import the local solver.py file

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow frontend requests

# Fixed center colors (based on correct cube net positioning)
fixed_centers = {
    "up": "white",
    "down": "yellow",
    "left": "orange",
    "right": "red",
    "front": "green",
    "back": "blue"
}

# Function to generate a scrambled cube state
def scramble_cube():
    cube = {face: [None] * 9 for face in fixed_centers.keys()}  # Initialize faces

    # Set fixed center colors
    for face, center_color in fixed_centers.items():
        cube[face][4] = center_color  # Center tile (index 4)

    # Create a list of available tiles (each color appears 8 times)
    available_tiles = []
    for color in fixed_centers.values():
        available_tiles.extend([color] * 8)  # 8 tiles per color

    # Shuffle tiles to randomize
    random.shuffle(available_tiles)

    # Assign scrambled colors to non-center positions
    for face in cube:
        for i in range(9):
            if i != 4:  # Skip center tile
                cube[face][i] = available_tiles.pop()

    return cube

# Function to convert cube state to Kociemba notation
def cube_to_kociemba(cube):
    """
    Kociemba expects a 54-character string in the order: U, R, F, D, L, B
    We need to remap our cube net to this format.
    """

    face_mapping = {
        "up": "U",
        "right": "R",
        "front": "F",
        "down": "D",
        "left": "L",
        "back": "B"
    }

    # Convert cube dictionary into a Kociemba formatted string
    kociemba_input = ""
    for face in ["up", "right", "front", "down", "left", "back"]:
        for tile in cube[face]:
            kociemba_input += face_mapping[face][0].upper() if tile in fixed_centers.values() else tile[0].upper()

    return kociemba_input

@app.route('/scramble', methods=['GET'])
def scramble():
    scrambled_cube = scramble_cube()
    return jsonify({"cube_state": scrambled_cube})

@app.route('/solve', methods=['POST'])
def solve():
    try:
        # Get cube state from frontend
        cube_state = request.json.get("cube_state")

        # Convert to Kociemba format
        kociemba_input = cube_to_kociemba(cube_state)

        # Solve using the local solver.py
        solution = solver.solve(kociemba_input)  # solver.py provides the solve() function

        return jsonify({"solution": solution})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/")
def home():
    return render_template("front.html")  # Ensure 'front.html' is inside the 'templates' folder

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
