import tkinter as tk
from tkinter import font
from PIL import Image, ImageFilter

# Get the watermark image
watermark = "logo.png"

with Image.open(watermark) as img_watermark:
    img_watermark.load()

img_watermark = Image.open(watermark)

# Change the watermark image to grayscale and threshold it
img_watermark = img_watermark.convert("L")
threshold = 50
img_watermark = img_watermark.point(lambda x: 255 if x > threshold else 0)

# Reduce its size and transform it into a contour image
img_watermark = img_watermark.resize((img_watermark.width // 2, img_watermark.height // 2))
img_watermark = img_watermark.filter(ImageFilter.CONTOUR)

# Reverse the colors
img_watermark = img_watermark.point(lambda x: 0 if x == 255 else 255)


def image_1():
    sunset = "sunset.png"

    with Image.open(sunset) as img_sunset:
        img_sunset.load()

    img_sunset = Image.open(sunset)

    # Paste img_watermark onto img_sunset
    img_sunset.paste(img_watermark, (3700, 2800), img_watermark)
    img_sunset.show()


def image_2():
    sink = "test_sink.png"

    with Image.open(sink) as img_sink:
        img_sink.load()

    img_sink = Image.open(sink)

    # Paste img_watermark onto img_sunset
    img_sink.paste(img_watermark, (2600, 3800), img_watermark)
    img_sink.show()


window = tk.Tk()
window.title('Add a watermark to a picture')

labelFont = font.Font(family='Helvetica', name='appHighlightFont', slant='italic', size=17, weight='bold')
buttonFont = font.Font(family='Helvetica', underline=1, size=16, weight='bold')

# Configure row INDEX of a grid
window.rowconfigure(0, minsize=100, weight=1)
# Configure column INDEX of a grid
window.columnconfigure([0, 1, 2], minsize=100, weight=1)

btn_image_1 = tk.Button(master=window, font=buttonFont, text='Choose picture number 1', command=image_1)
btn_image_1.grid(row=0, column=0, sticky='nsew')

lbl_info = tk.Label(master=window, font=labelFont, text=' <= Choose one of the pictures => ')
lbl_info.grid(row=0, column=1)

btn_image_2 = tk.Button(master=window, font=buttonFont, text='Choose picture number 2', command=image_2)
btn_image_2.grid(row=0, column=2, sticky='nsew')

window.mainloop()
