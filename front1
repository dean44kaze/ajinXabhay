<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Interactive Rubik's Cube (2D Cube Net)</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    body {
      margin: 0;
      font-family: Arial, sans-serif;
      background-color: #f0f0f0;
    }
    #container {
      max-width: 800px;
      margin: 0 auto;
      padding: 20px;
    }
    h1 {
      text-align: center;
      margin-bottom: 20px;
    }
    /* Color Panel */
    .color-selector {
      display: flex;
      justify-content: center;
      gap: 10px;
      margin-bottom: 20px;
    }
    .color-box {
      width: 40px;
      height: 40px;
      border: 2px solid #000;
      cursor: pointer;
    }
    /* Control Buttons */
    #controls {
      display: flex;
      justify-content: center;
      gap: 15px;
      margin-bottom: 20px;
    }
    button {
      padding: 10px 15px;
      border: none;
      border-radius: 5px;
      background-color: #4CAF50;
      color: white;
      font-size: 16px;
      cursor: pointer;
      transition: background-color 0.3s;
    }
    button:hover {
      background-color: #45a049;
    }
    /* Cube Net Layout */
    .cube-net {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      grid-template-rows: repeat(3, auto);
      gap: 10px;
      justify-items: center;
    }
    /* Cube Face */
    .cube-face {
      display: grid;
      grid-template-columns: repeat(3, 50px);
      grid-auto-rows: 50px;
      gap: 2px;
      background-color: #ccc;
      padding: 5px;
    }
    .cube-square {
      width: 50px;
      height: 50px;
      border: 1px solid #000;
      background-color: #ccc;
      cursor: pointer;
    }
    .placeholder {
      visibility: hidden;
      width: 50px;
      height: 50px;
    }
  </style>
</head>
<body>
  <div id="container">
    <h1>Interactive Rubik's Cube (2D Cube Net)</h1>
    
    <!-- Color Panel -->
    <div class="color-selector">
      <div class="color-box" style="background-color: yellow;" data-color="yellow"></div>
      <div class="color-box" style="background-color: white;" data-color="white"></div>
      <div class="color-box" style="background-color: red;" data-color="red"></div>
      <div class="color-box" style="background-color: orange;" data-color="orange"></div>
      <div class="color-box" style="background-color: green;" data-color="green"></div>
      <div class="color-box" style="background-color: blue;" data-color="blue"></div>
    </div>
    
    <!-- Control Buttons -->
    <div id="controls">
      <button id="scrambleBtn">Scramble</button>
      <button id="solveBtn">Solve</button>
      <button id="resetBtn">Reset</button>
    </div>
    
    <!-- Cube Net (T-Shape) -->
    <div class="cube-net">
      <!-- Row 1: Up face -->
      <div class="placeholder"></div>
      <div class="cube-face" id="up"></div>
      <div class="placeholder"></div>
      <div class="placeholder"></div>
      
      <!-- Row 2: Left, Front, Right, Back -->
      <div class="cube-face" id="left"></div>
      <div class="cube-face" id="front"></div>
      <div class="cube-face" id="right"></div>
      <div class="cube-face" id="back"></div>
      
      <!-- Row 3: Down face -->
      <div class="placeholder"></div>
      <div class="cube-face" id="down"></div>
      <div class="placeholder"></div>
      <div class="placeholder"></div>
    </div>
  </div>
  
  <script>
    let selectedColor = "yellow";
    const faces = ["up", "down", "left", "right", "front", "back"];
    
    // Fixed center colors (these match your scramble backend configuration)
    const fixedCenters = {
      up: "yellow",
      down: "white",
      left: "green",
      front: "orange",
      right: "blue",
      back: "red"
    };
    
    // Initialize cube net with solved state
    function initializeCube() {
      faces.forEach(face => {
        const faceDiv = document.getElementById(face);
        faceDiv.innerHTML = "";
        for (let i = 0; i < 9; i++) {
          const square = document.createElement("div");
          square.classList.add("cube-square");
          if (i === 4) {
            square.style.backgroundColor = fixedCenters[face];
            square.dataset.fixed = "true";
          } else {
            square.style.backgroundColor = "#ccc";
          }
          // Allow user to paint non-fixed squares with selected color
          square.addEventListener("click", function() {
            if (!this.dataset.fixed) {
              this.style.backgroundColor = selectedColor;
            }
          });
          faceDiv.appendChild(square);
        }
      });
    }
    
    // Color picker events
    document.querySelectorAll(".color-box").forEach(box => {
      box.addEventListener("click", function() {
        selectedColor = this.dataset.color;
      });
    });
    
    // Scramble function: Fetch scramble data from Flask backend
    function scrambleCube() {
      fetch("http://127.0.0.1:5000/scramble")
        .then(response => response.json())
        .then(data => {
          faces.forEach(face => {
            const faceDiv = document.getElementById(face);
            // data[face] is an array of 9 color strings
            Array.from(faceDiv.children).forEach((square, index) => {
              square.style.backgroundColor = data.cube_state[face][index];
            });
          });
          console.log("Scramble moves:", data.scramble_moves);
        })
        .catch(error => {
          console.error("Error fetching scramble:", error);
          alert("Failed to fetch scramble. Make sure the backend is running.");
        });
    }
    
    // Solve and reset functions for now just reset the cube to the solved state
    function solveCube() {
      initializeCube();
    }
    
    function resetCube() {
      initializeCube();
    }
    
    document.getElementById("scrambleBtn").addEventListener("click", scrambleCube);
    document.getElementById("solveBtn").addEventListener("click", solveCube);
    document.getElementById("resetBtn").addEventListener("click", resetCube);
    
    initializeCube();
  </script>
</body>
</html>
