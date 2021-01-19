from sense_emu  import SenseHat
from time import sleep

sdev = SenseHat()

sdev.lop_light = False

while True:
    sdev.show_message("eimon",text_colour=(255, 0, 255),back_colour= (0, 0, 0))

    p = (255, 0, 255)
    b = (0, 0, 0)
    w = (255, 255, 255)

    n96 = [
    b, b, b, b, b, b, b, b,
    p, p, p, p, w, b, b, b,
    p, b, b, p, w, b, b, b,
    p, b, b, p, w, b, b, b,
    p, p, p, p, w, w, w, w,
    b, b, b, p, w, b, b, w,
    b, b, b, p, w, b, b, w,
    b, b, b, p, w, w, w, w
    ]

    sdev.set_pixels(n96)
    
    sleep(2)
