import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

# --- Parameters ---
GRID_SIZE = 70

# Lower scale makes the features smaller, creating more "chunks" across the 50x50 space.
SCALE = 9.8

# Lower octaves remove the fuzzy, high-frequency static, leaving solid blobs.
OCTAVES = 2

# Return to standard persistence so the noise doesn't blow out into pure black/white
PERSISTENCE = 0.3

LACUNARITY = 1.7
SEED = 42

# Initialize the 50x50 grid
elevation_data = np.zeros((GRID_SIZE, GRID_SIZE))

# Generate the 2D Noise
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
        
        # Normalize to a positive range
        elevation_data[i][j] = ((noise_val + 1) / 2) * 10

# save the elevation data as a pickle file
import pickle
TYPE = f"{GRID_SIZE}x{GRID_SIZE}"
with open(f"{TYPE}\elevation_data{TYPE}.pickle" ,"wb") as file:
    elevation_data = np.array(elevation_data)
    pickle.dump(elevation_data, file)


# --- Visualization ---
plt.figure(figsize=(6, 6))
plt.imshow(elevation_data, cmap="gray")
plt.title(f"Rougher High-Res Perlin Noise ({GRID_SIZE}x{GRID_SIZE})")
plt.colorbar(label='Elevation')
plt.show()


# def generate_obstacle_map(grid_size, scale=8.0, threshold=0.2, seed=None):
#     """
#     Generates a binary obstacle map using thresholded Perlin noise.
    
#     Parameters:
#     - grid_size: Integer, size of the grid (e.g., 50 for 50x50).
#     - scale: Float, controls the size of the obstacle clusters.
#     - threshold: Float (-1.0 to 1.0). Higher = fewer obstacles, Lower = more obstacles.
#     - seed: Integer for reproducibility.
#     """
#     if seed is None:
#         seed = random.randint(0, 100000)
        
#     obstacle_map = np.zeros((grid_size, grid_size), dtype=int)
    
#     for i in range(grid_size):
#         for j in range(grid_size):
#             # Generate base noise between roughly -1.0 and 1.0
#             noise_val = pnoise2(
#                 i / scale, 
#                 j / scale, 
#                 octaves=2,       # Low octaves keep the edges relatively smooth
#                 persistence=0.3, 
#                 lacunarity=1.7, 
#                 repeatx=1024, 
#                 repeaty=1024, 
#                 base=seed
#             )
            
#             # Apply threshold: 1 if above threshold, 0 otherwise
#             if noise_val > threshold:
#                 obstacle_map[i][j] = 1
#             else:
#                 obstacle_map[i][j] = 0
                
#     return obstacle_map

# # --- Parameters ---
# GRID_SIZE = 50

# # A scale of 6.0 to 10.0 gives nice medium-sized clusters like your 30x30 map.
# SCALE = 8.0 

# # Adjust this to change obstacle density. 
# # 0.2 to 0.4 usually gives a nice 15% - 30% obstacle coverage.
# THRESHOLD = 0

# SEED = 12345 

# # Generate the map
# obstacle_map = generate_obstacle_map(GRID_SIZE, SCALE, THRESHOLD, SEED)

# # Print the matrix format (if you want to copy-paste the raw array)
# # print(repr(obstacle_map))

# # --- Visualization ---
# plt.figure(figsize=(6, 6))
# # Using a binary colormap: 0 = white (free space), 1 = black (obstacle)
# plt.imshow(obstacle_map, cmap="binary")
# plt.title(f"Clustered Obstacle Map ({GRID_SIZE}x{GRID_SIZE})")

# # Add a grid to make it easier to see individual cells
# plt.grid(which='major', color='gray', linestyle='-', linewidth=0.5, alpha=0.5)
# plt.xticks(np.arange(-.5, GRID_SIZE, 1), [])
# plt.yticks(np.arange(-.5, GRID_SIZE, 1), [])
# plt.tick_params(axis='both', length=0) # Hide tick marks

# plt.show()