from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (192,192)
camera.framerate = 15


camera.start_preview()
sleep(5)
camera.stop_preview()