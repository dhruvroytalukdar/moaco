import numpy as np
from noise import pnoise2

# --- Environment Parameters ---
GRID_SIZE = 60
SCALE = 9.8
OCTAVES = 2
PERSISTENCE = 0.3
LACUNARITY = 1.7
SEED = 70

# Lowering this threshold makes obstacles larger/denser
THRESHOLD = 0.3

# Initialize the 60x60 grid
binary_map = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Generate the Binarized Noise Map
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        noise_val = pnoise2(
            i / SCALE, 
            j / SCALE, 
            octaves=OCTAVES, 
            persistence=PERSISTENCE, 
            lacunarity=LACUNARITY, 
            repeatx=1024, 
            repeaty=1024, 
            base=SEED
        )
        
        # Binarize: Values above the threshold become obstacles (1), else free space (0)
        if noise_val > THRESHOLD:
            binary_map[i][j] = 1
        else:
            binary_map[i][j] = 0

# Convert to a standard Python list of lists 
map_list = binary_map.tolist()

# --- Visualization ---
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 6))
plt.imshow(binary_map, cmap="gray")
plt.title(f"Binary Obstacle Map ({GRID_SIZE}x{GRID_SIZE})")
plt.colorbar(label='Obstacle (1) vs Free Space (0)')
plt.show()

with open(f"{GRID_SIZE}x{GRID_SIZE}/obstacle_map{GRID_SIZE}x{GRID_SIZE}.pickle", "wb") as file:
    import pickle
    pickle.dump(map_list, file)
