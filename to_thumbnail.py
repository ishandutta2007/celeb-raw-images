import os
from PIL import Image

source_path = os.getcwd() + "/donaldtrump/bbf18ade-1f5f-11eb-99d6-deeedd63f648_image_hires_124435-removebg-preview.png"
image = Image.open(source_path)
image.thumbnail((1280,720), Image.LANCZOS)
image.save(source_path.replace(".png","_1280x720.png"), "PNG")
