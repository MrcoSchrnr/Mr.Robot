import numpy as np
import cv2
import argparse
import os
from time import time
from time import sleep

class ObjectDetection:
    
    def __init__(self, weights, labels, config, resW, resH):  
        

        # import the necessary packages
        current_fps = 0
        myFrame = 0

        myConfidence = 0.4
        myThreshold = 0.4

        self.limitCPUtemp = True
        cpuTempLimit = 64
        limitToVideoFPS = False

        # createOutput = True
        # myOutput = "output.mp4"
        createOutput = False

        from gpiozero import CPUTemperature
        limitToVideoFPS = True
        myWidth = resW
        myHeight = resH
        fps_limit = 5
        my_buffer_size = 1  # number of frames in buffer
            
        # Networks
        # networks = {}

        # networks["64_v4"] = {"folder": "64_v4", "resolution": 256,
        #                     "weights": "yolov3-tiny_last.weights"}

        # selectedNetwork = networks["64_v4"]

        # webcams 0 and 1
        myInput = 0
        # myInput = 1

        myDNNsize = 256

        # load the class labels our YOLO model was trained on
        labelsPath = labels #team5.names
        LABELS = open(labelsPath).read().strip().split("\n")

        # initialize a list of colors to represent each possible class label
        np.random.seed(42)
        COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

        # derive the paths to the YOLO weights and model configuration
        weightsPath = weights
        configPath = config

        # load our trained YOLO object detector (5 classes)
        # and determine only the *output* layer names that we need from YOLO
        print("[INFO] loading YOLO from disk...")
        print(configPath, weightsPath)
        self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
        ln = self.net.getLayerNames()
        ln = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        writer = None
        (W, H) = (None, None)

        # initialize the video stream, pointer to output video file, and
        # frame dimensions
        self.vs = cv2.VideoCapture(myInput)

        if(myInput is 0 or myInput is 1):  # Camera
            self.vs.set(cv2.CAP_PROP_BUFFERSIZE, my_buffer_size)
            # print(f"Buffer size = {vs.get(cv2.CAP_PROP_BUFFERSIZE)}")
            self.vs.set(cv2.CAP_PROP_FRAME_WIDTH, myWidth)
            self.vs.set(cv2.CAP_PROP_FRAME_HEIGHT, myHeight)


    # loop over frames from the video file stream (from camera or file)
    def getLabels(self):
        if self.limitCPUtemp is True:
            # CPU temp
            cpu = CPUTemperature()
            cpuTemp = cpu.temperature
            # print(cpuTemp)
            if cpuTemp > self.cpuTempLimit:
                time.sleep(0.1)
                cpuTemp = cpu.temperature
                print("cooling down...")
                print(cpuTemp)

                return 
        
        (grabbed, frame) = self.vs.read()
        (grabbed, frame) = self.vs.read()

        # if the frame was not grabbed, then we have reached the end
        # of the stream
        if not grabbed:
            return
        
        # if the frame dimensions are empty, grab them
        if W is None or H is None:
            (H, W) = frame.shape[:2]

        start = time.time()

        # construct a blob from the input frame and then perform a forward
        # pass of the YOLO object detector, giving us our bounding boxes
        # and associated probabilities
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (myDNNsize, myDNNsize),
            swapRB=True, crop=False)
        self.net.setInput(blob)
        
        # most CPU intensive part!
        layerOutputs = self.net.forward(ln)
        
        # initialize our lists of detected bounding boxes, confidences,
        # and class IDs, respectively
        boxes = []
        confidences = []
        classIDs = []

        # loop over each of the layer outputs
        for output in layerOutputs:
            # loop over each of the detections
            for detection in output:
                # extract the class ID and confidence (i.e., probability)
                # of the current object detection
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]

                # filter out weak predictions by ensuring the detected
                # probability is greater than the minimum probability
                if confidence > myConfidence:
                    # scale the bounding box coordinates back relative to
                    # the size of the image, keeping in mind that YOLO
                    # actually returns the center (x, y)-coordinates of
                    # the bounding box followed by the boxes' width and
                    # height
                    box = detection[0:4] * np.array([W, H, W, H])
                    (centerX, centerY, width, height) = box.astype("int")

                    # use the center (x, y)-coordinates to derive the top
                    # and and left corner of the bounding box
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))

                    # update our list of bounding box coordinates,
                    # confidences, and class IDs
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)
                    
    
        # some information on processing single frame   
        end = time.time()
        elap = (end - start)

        returnValue = {"boxes": boxes, "confidences": confidences, "classIDs": classIDs, "delta": elap}

        return returnValue


    def destroy(self):
        vs.release()
        cv2.destroyAllWindows()

 




