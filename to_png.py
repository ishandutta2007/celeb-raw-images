import os
from PIL import Image

onlyfiles = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]
for file in onlyfiles:
    if ".webp" in file:
        print("yeah we need to process", file)
        im = Image.open(file)
        im.save(file.replace(".webp", ".png"), "PNG")
