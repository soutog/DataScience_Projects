import sys 
import os, glob
from PIL import Image

# grab the first and second argument
folder = sys.argv[1]
new_folder = sys.argv[2]

# check if new/ exists if not create it
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

# loop through Pokedex, convert images to png save them to the new folder
for file in os.listdir(folder):
    img = Image.open(f"./{folder}/{file}")
    outfile = os.path.splitext(file)[0]
    img.save(f"./{new_folder}/{outfile}_converted.png", "png")


    