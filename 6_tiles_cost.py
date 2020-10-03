# Find Cost of Tile to Cover W x H Floor -
# Calculate the total cost of tile it would take to cover a floor plan
# of width and height, using a cost entered by the user.

# Floor tile cost calculator
import math

floor_width = float(input("Enter floor width: "))
floor_height = float(input("Enter floor height: "))
tile_width = float(input("Enter tile width: "))
tile_height = float(input("Enter tile height: "))
tile_cost = float(input("Enter cost of single tile: "))

tiles_for_w = math.ceil(floor_width / tile_width)
tiles_for_h = math.ceil(floor_height / tile_height)

total_tiles = tiles_for_w * tiles_for_h
final_cost = tile_cost * total_tiles

print(f"Final cost of tiles for floor plan {floor_width} x {floor_height} is: {final_cost}")