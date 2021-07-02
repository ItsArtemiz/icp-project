import datetime

from PIL import ImageGrab
# yyyymmdd_hhmmss.png

def time_to_string():
    """Converts the current time to string so it can be used to save the file."""
    now = datetime.datetime.now() # Gives current time.
    return datetime.datetime.strftime(now, '%Y%m%d_%H%M%S')

im = ImageGrab.grab()
im.save(f'{time_to_string()}.png')