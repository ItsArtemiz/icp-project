import datetime # For time related stuff

import tkinter as tk # For GUI

from PIL import ImageGrab, Image
import PIL.ImageTk as ImageTK # Cannot import from PIL for some reason

# yyyymmdd_hhmmss.png

def time_to_string():
    """Converts the current time to string so it can be used to save the file."""
    now = datetime.datetime.now() # Gives current time.
    return datetime.datetime.strftime(now, '%Y%m%d_%H%M%S')+'.png' # python datetime formats, w3s

def display_image(name, size):
    root = tk.Tk()
    root.title(f'Image: {name}')

    width, height = size # (width, height)
    root.geometry(f'{width}x{height}')

    image = Image.open(name)
    pic = ImageTK.PhotoImage(image)

    label = tk.Label(image=pic)
    label.pack()

    root.mainloop()

# def screenshot():
#     main = tk.Tk()
#     main.title('')

im = ImageGrab.grab() # takes screenshot
time = time_to_string()

size = (im.width // 2, im.height // 2) # to fit on screen

im = im.resize(size)
im.save(time)
display_image(time, size)