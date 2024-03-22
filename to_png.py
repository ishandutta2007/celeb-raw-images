import os
from PIL import Image
import pillow_avif

onlyfiles = [
    f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))
]
for file in onlyfiles:
    if ".webp" in file:
        print("webp_to_png:yeah we need to process", file)
        im = Image.open(file)
        im.save(file.replace(".webp", ".png"), "PNG")

for file in onlyfiles:
    if ".avif" in file:
        print("avif_to_png:yeah we need to process", file)
        im = Image.open(file)
        im.save(file.replace(".avif", ".png"), "PNG")
