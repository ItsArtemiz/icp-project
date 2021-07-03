import datetime # For time related stuff
import time
import os # To make folder

import tkinter as tk # For GUI

from PIL import ImageGrab, Image
import PIL.ImageTk as ImageTK # Cannot import from PIL for some reason

# yyyymmdd_hhmmss.png

# Pictures/Screenshots

def time_to_string():
    """Converts the current time to string so it can be used to save the file."""
    now = datetime.datetime.now() # Gives current time.
    return f"C:\\Users\\{os.getlogin()}\\Pictures\\Screenshots\\{datetime.datetime.strftime(now, '%Y%m%d_%H%M%S')}.png" # python datetime formats, w3s

def display_image(name, size):
    display = tk.Toplevel(root)
    display.title(f'Image: {name}')
    display.resizable(False, False)

    width, height = size # (width, height)
    
    display.geometry(f'{width}x{height}')

    image = Image.open(name)
    pic = ImageTK.PhotoImage(image)

    label = tk.Label(display, image=pic)
    label.pack(in_=display, expand=True)
    root.deiconify()

    display.mainloop()

def take_screenshot():
    time.sleep(0.5)
    root.iconify()
    time.sleep(0.5)

    im: Image.Image = ImageGrab.grab() # takes screenshot
    name = time_to_string()

    size = (im.width//2, im.height//2) # to fit on screen

    im = im.resize(size, Image.ANTIALIAS)
    try:
        im.save(name)
    except FileNotFoundError:
        os.makedirs(f'C:\\Users\\{os.getlogin()}\\Pictures\\Screenshots')
    display_image(name, size)

def browsefile():
    try:
        os.listdir(path)
    except FileNotFoundError:
        os.makedirs(path)
    finally:
        os.startfile(path)

def update_recents():
    recent = tk.Frame(root)
    recent.pack(pady=10)
    label = tk.Label(recent, text='Recent Pictures', font=('Calibri', 20))
    label.pack(pady=10)
    i=0
    for im in directory:
        if i>=3:
            break
        label = tk.Label(recent, text=str(im))
        label.pack(in_=recent, expand=False, pady=2)
        i+=1
    if not len(directory):
        label = tk.Label(recent, text='No recent screenshots', font=('Calibri'))
        label.pack(pady=10)

root = tk.Tk()
root.title('Take Screenshots')
root.geometry('500x500')
path = f'C:\\Users\\{os.getlogin()}\\Pictures\\Screenshots'

ss_button = tk.Button(root, text='Take Screenshot', command=take_screenshot)
ss_button.pack(side=tk.TOP, pady=50)

file_button = tk.Button(root, text='Open Screenshots', command=browsefile)
file_button.pack(side=tk.TOP, pady=25)

try:
    directory = os.listdir(path)
except FileNotFoundError:
    os.makedirs(path)
else:
    
    update_recents()

root.mainloop()