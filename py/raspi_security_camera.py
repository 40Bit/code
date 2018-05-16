import time
from picamera import PiCamera

camera = PiCamera()

def pic():
    camera.capture('/var/www/html/photos/pic.jpg')

def start_vid():
    print('do not use auto_vid until you run end_vid')
    camera.start_recording('/var/www/html/photos/vid.h264')
    
def end_vid():
    camera.stop_recording()
    
def pic_rep():
    print('control+c to turn off')
    while True:
        time.sleep(3)
        camera.capture('/var/www/html/photos/pic_rep.jpg')

def auto_vid(a):
    print('do not use start_vid & end_vid until auto_vid is done')
    camera.start_recording('/var/www/html/photos/auto_vid.h264')
    time.sleep(a)
    camera.stop_recording()

    
    
