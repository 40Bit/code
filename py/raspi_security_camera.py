import time

def picture():
    capture()

def start_video():
    start_recording()

def end_video():
    stop_recording()

def pic_rep_on():
    print('control+c to turn off')
    while True:
        time.sleep(3)
        capture()
        

    

    
