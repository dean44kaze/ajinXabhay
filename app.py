from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Allow requests from any origin

# Fixed center colors for each face
fixed_centers = {
    "up": "yellow",
    "down": "white",
    "left": "green",
    "front": "orange",
    "right": "blue",
    "back": "red"
}

# Function to generate a scrambled cube state (excluding centers)
def scramble_cube():
    cube = {face: [None] * 9 for face in fixed_centers.keys()}  # Initialize cube faces

    # Set fixed center colors
    for face, center_color in fixed_centers.items():
        cube[face][4] = center_color  # Center tile (index 4)

    # Create a list of available tiles (each color appears 9 times in total)
    available_tiles = sum([[color] * 8 for color in fixed_centers.values()], [])  # 8 tiles per color

    # Shuffle available tiles to ensure randomness
    random.shuffle(available_tiles)

    # Assign scrambled colors to non-center positions
    for face in cube:
        for i in range(9):
            if i != 4:  # Skip center position
                cube[face][i] = available_tiles.pop()

    return cube

@app.route('/scramble', methods=['GET'])
def scramble():
    return jsonify({"cube_state": scramble_cube()})  # Return JSON response

@app.route("/")
def home():
    return render_template("front.html")  # Ensure 'front.html' is inside the 'templates' folder

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
