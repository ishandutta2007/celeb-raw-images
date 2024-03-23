import os
import math
from PIL import Image

source_path = os.getcwd() + "/loganpaul/"

# f = "bbf18ade-1f5f-11eb-99d6-deeedd63f648_image_hires_124435-removebg-preview.png"

onlyTransFiles = [
    f
    for f in os.listdir(source_path)
    if os.path.isfile(os.path.join(source_path, f)) and "-removebg-preview.png" in f
]
print(onlyTransFiles)

for file in onlyTransFiles:
    print("Starting for", file)
    background = Image.open(os.getcwd() + "/background_1280x720.png")
    foreground = Image.open(source_path + "/" + file)
    foregroundwidth, foregroundheight = foreground.size

    if foregroundheight < 720 and foregroundwidth * 720 / foregroundheight < 1280:
        scalingfactor = 720 / foregroundheight
    elif foregroundwidth < 1280 and foregroundheight * 1280 / foregroundwidth < 720:
        scalingfactor = 1280 / foregroundwidth
    else:
        print(
            "both width height bigeer than background",
            source_path,
            foregroundwidth,
            foregroundheight,
        )
        scalingfactor = 1
        continue

    scalingfactor = 0.8 * scalingfactor

    newforegroundwidth = math.floor(foregroundwidth * scalingfactor)
    newforegroundheight = math.floor(foregroundheight * scalingfactor)
    targetsize = (
        newforegroundwidth,
        newforegroundheight,
    )

    print("targetsize", targetsize)
    foreground = foreground.resize(targetsize)

    dest_path = os.getcwd() + "/mydirectory/"

    overlay_left_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    overlay_left_canvas.paste(background, (0, 0))
    overlay_left_canvas.paste(foreground, (0, 720 - newforegroundheight), foreground)
    overlay_left_canvas.save(
        dest_path + "/" + file.replace(".png", "_overlay_left.png"), "PNG"
    )

    overlay_right_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    overlay_right_canvas.paste(background, (0, 0))
    overlay_right_canvas.paste(
        foreground, (1280 - newforegroundwidth, 720 - newforegroundheight), foreground
    )
    overlay_right_canvas.save(
        dest_path + "/" + file.replace(".png", "_overlay_right.png"), "PNG"
    )

    overlay_centre_canvas = Image.new("RGBA", background.size, (0, 0, 0, 0))
    overlay_centre_canvas.paste(background, (0, 0))
    overlay_centre_canvas.paste(
        foreground, ((1280 - newforegroundwidth)//2, 720 - newforegroundheight), foreground
    )
    overlay_centre_canvas.save(
        dest_path + "/" + file.replace(".png", "_overlay_centre.png"), "PNG"
    )
    print("Done for", file)
