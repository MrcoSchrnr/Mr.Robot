# import the necessary packages
import numpy as np
import time
import cv2
import os
import imutils
from gpiozero import CPUTemperature
import framereader

class Detector():
    def __init__(self, weights, labels, config, resW, resH, treshhold = 0.4, cpu_temp_limit = 70):
        self.limitCPUtemp = True
        self.weights = weights
        self.labels = labels
        self.config = config
        self.resH = resH
        self.resW = resW
        self.treshhold = treshhold
        self.cpu_temp_limit = cpu_temp_limit
        self.buffer_size = 1 #1 # number of frames in buffer

        # webcams 0 and 1
        myInput = 0

        # load the class labels our YOLO model was trained on
        labelsPath = self.labels
        #LABELS = open(labelsPath).read().strip().split("\n")

        # derive the paths to the YOLO weights and model configuration
        #weightsPath = os.path.sep.join(["models", self.weights])
        #configPath = os.path.sep.join(["models", self.config])
        weightsPath = self.weights
        configPath = self.config

        self.vs = framereader.FrameReader(self.resW, self.resH)
        self.vs.start()
        time.sleep(3)

        # load our trained YOLO object detector (5 classes)
        # and determine only the *output* layer names that we need from YOLO
        print("[INFO] loading YOLO from disk...")
        print(configPath, weightsPath)
        self.net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
        self.ln = self.net.getLayerNames()
        self.ln = [self.ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        self.writer = None
        self.W = None
        self.H = None

        # initialize the video stream, pointer to output video file, and
        # frame dimensions



    def get_label_map(self):
        if self.limitCPUtemp is True:
            # CPU temp
            cpu = CPUTemperature()
            cpuTemp = cpu.temperature
            # print(cpuTemp)
            if cpuTemp > self.cpu_temp_limit:
                time.sleep(0.1)
                return None
        try:
            frame = self.vs.read_latest()
        except IndexError:
            print("No frame")
            return None
        # except:
        #     print("Other Error")
        #     return None

        
        # if the frame dimensions are empty, grab them
        if self.W is None or self.H is None:
            (HHolder, WHolder) = frame.shape[:2]
            self.H = HHolder
            self.W = WHolder

        start = time.time()

        # construct a blob from the input frame and then perform a forward
        # pass of the YOLO object detector, giving us our bounding boxes
        # and associated probabilities
        # blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (myDNNsize, myDNNsize),
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (self.resH, self.resW),
            swapRB=True, crop=False)
        self.net.setInput(blob)
        
        # most CPU intensive part!
        layerOutputs = self.net.forward(self.ln)
        
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
                if confidence > self.treshhold:
                    # scale the bounding box coordinates back relative to
                    # the size of the image, keeping in mind that YOLO
                    # actually returns the center (x, y)-coordinates of
                    # the bounding box followed by the boxes' width and
                    # height
                    # box = detection[0:4]
                    box = detection[0:4] * np.array([self.W, self.H, self.W, self.H])
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
                    
        
        end = time.time()
        elap = (end - start)
        return {"delta": elap, "boxes": boxes, "confidents": confidences, "classIds": classIDs}

    def destroy(self):
        self.vs.stop()

