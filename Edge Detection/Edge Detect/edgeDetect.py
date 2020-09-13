from PIL import Image, ImageDraw
import numpy as np

img = Image.open("edge-detection.png")
input_pixels = img.load()

vert = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
hor = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel = np.array([[1, 2, 2], [1, 1, 0], [2, 4, 1]])

kernel = vert

offset = len(kernel) // 2
output_image = Image.new("RGB", img.size)
draw = ImageDraw.Draw(output_image)
for x in range(offset, img.width - offset):
    for y in range(offset, img.height - offset):
        acc = [0, 0, 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] += pixel[0] * kernel[a][b]
                acc[1] += pixel[1] * kernel[a][b]
                acc[2] += pixel[2] * kernel[a][b]

        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))
output_image.show()
output_image.save('Vertical Edge Detection-Dog.jpg')
