from PIL import Image

def flamm_upscaler(factor: int) -> None:
    image = Image.open("XX_RandomStuff\UpscalingQuestionMark\input.png")
    print(image.size)
    
    pixel = image.load()
    
    output = Image.new(mode = "RGB", size = (factor * image.width, factor * image.height))
    
    for x in range(image.width):
        for y in range(image.height):
            pixel_color = pixel[x, y]
            for fx in range(factor):
                for fy in range(factor):
                    output.putpixel((x * factor + fx, y * factor + fy), pixel_color)
    
    output.save("XX_RandomStuff\UpscalingQuestionMark\output.png")

flamm_upscaler(3)