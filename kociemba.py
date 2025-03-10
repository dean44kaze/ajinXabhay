import kociemba

class CubeSolver:
    def __init__(self):
        self._solve = kociemba._solve  # Assigning _solve as an attribute

    def convert_to_kociemba_notation(self, cube_state):
        color_map = {
            'yellow': 'U',
            'white': 'D',
            'red': 'F',
            'orange': 'B',
            'green': 'L',
            'blue': 'R'
        }

        face_order = ['U', 'R', 'F', 'D', 'L', 'B']
        facelet_order = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8],  # U
            [0, 1, 2, 3, 4, 5, 6, 7, 8],  # R
            [0, 1, 2, 3, 4, 5, 6, 7, 8],  # F
            [0, 1, 2, 3, 4, 5, 6, 7, 8],  # D
            [0, 1, 2, 3, 4, 5, 6, 7, 8],  # L
            [0, 1, 2, 3, 4, 5, 6, 7, 8]   # B
        ]

        kociemba_string = ''
        for face, indices in zip(face_order, facelet_order):
            for idx in indices:
                color = cube_state[face][idx]
                kociemba_string += color_map[color]  # Convert colors to Kociemba notation

        return kociemba_string

    def solve_cube(self, cube_state):
        """
        Converts the cube state to Kociemba notation and solves it using self._solve.
        """
        try:
            kociemba_input = self.convert_to_kociemba_notation(cube_state)
            solution = self._solve(kociemba_input)  # Calling _solve from the attribute
            return solution
        except Exception as e:
            return f"Error: {str(e)}"

# Example Usage
if __name__ == "__main__":
    solver = CubeSolver()

    example_cube_state = {
        'U': ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow'],
        'R': ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue'],
        'F': ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'],
        'D': ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white'],
        'L': ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green'],
        'B': ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
    }

    solution = solver.solve_cube(example_cube_state)
    print("Solution:", solution)
