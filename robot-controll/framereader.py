"""Active ring buffer for frames. 

.start() starts the active buffer. Grabs frames from an input decive.
.read_latest() gives us the most recent frame.

Uses OpenCV, runs in demon thread.

Authors:
    Wolfgang Funk <funk@dhbw-vs.de>

"""
import time
import cv2
from threading import Thread
from collections import deque


class FrameReader:
    """Active buffer for frames."""
    
    BUFFER_SIZE = 1  # No buffering by OpenCV
    
    def __init__(self, width, height, camera=0):
        """Inits buffer with frame dimensions and camera ID

        Args:
            width (int): frame width
            height (int): frame height
            camera (int) camera ID (default: 0)
            
        """
        self.stream = cv2.VideoCapture(camera)
        self.stream.set(cv2.CAP_PROP_BUFFERSIZE, FrameReader.BUFFER_SIZE)
        self.stream.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.stream.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.stopped = False
        self.buffer = deque(maxlen=2)
        # self.frame_cnt = 0
        
    def start(self):
        """Starts grabbing into buffer"""
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
    
    def stop(self):
        """Stops grabbing thread"""
        self.stopped = True
    
    def update(self):
        """Frame grabbing in infinite loop.

        May be stopped by calling .stop()
        
        """
        while True:
            if self.stopped:
                return
            (grabbed, frame) = self.stream.read()
            if not grabbed:
                self.stop()
            self.buffer.append(frame)
            # self.frame_cnt += 1
            # print(f"{self.frame_cnt} {len(self.buffer)}")
            
    def read_latest(self):
        """Get most recent frame from buffer."""
        return self.buffer.pop()  

if __name__ == "__main__":
    reader = FrameReader(1024, 768)
    try:
        reader.read_latest()
    except IndexError:
        print("No frame")
    reader.start()
    print("Wait 3 seconds for buffer to be filled ...")
    time.sleep(3)
    reader.stop()
    f = reader.read_latest()
    print("... most frecent frame of " ,type(f), " read")
    print(f)