# import the necessary packages
import numpy as np
import time
import cv2
import os
import imutils
from gpiozero import CPUTemperature
import framereader

class ObjectDetector():

    def __init__(self, treshhold = 0.4, cpu_temp_limit = 70):
        self.limitCPUtemp = True
        self.weights = "none"
        self.labels = "none"
        self.config = "none"
        self.resolutionHeight = 256
        self.resolutionWidth = 192
        self.treshhold = treshhold
        self.cpu_temp_limit = cpu_temp_limit
        self.buffer_size = 1 #1 # number of frames in buffer


        # Testing Arrays

        self.animalArray = []
        self.verticalPositionArray = []
        self.horizontalPositionArray = []


    def startDetector(self, weights, labels, config, resolutionWidght, resolutionHeight):

        # getting data from probs

        self.weights = weights
        self.labels = labels
        self.config = config
        self.resolutionWidght = resolutionWidght
        self.resolutionHeight = resolutionHeight

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

        self.vs = framereader.FrameReader(self.resolutionWidth, self.resolutionHeight)
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
        blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (self.resolutionHeight, self.resolutionWidth),
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

                    if x <= 100:
                        self.horizontalPositionArray.append("left")
                    
                    elif x >= 160:
                        self.horizontalPositionArray.append("right")
                    
                    else:
                        self.horizontalPositionArray.append("middle")



                    if y <= 64:
                        self.verticalPositionArray.append("bottom")
                    
                    elif y >= 150:
                        self.verticalPositionArray.append("top")
                    
                    else:
                        self.verticalPositionArray.append("middle")


                    confidences.append(float(confidence))


                    # appending Animals to animalArray
                    classIDs.append(classID)

                    if classID == 0:
                        self.animalArray.append("elephant")

                    elif classID == 1:
                        self.animalArray.append("tiger")
            
                    elif classID == 2:
                        self.animalArray.append("star")

                    elif classID == 3:
                        self.animalArray.append("cat")

                    elif classID == 4:
                        self.animalArray.append("frog")
        
        end = time.time()
        elap = (end - start)

        #print(self.animalArray)
        #print(self.horizontalPositionArray)
        #print(self.verticalPositionArray)

        #return {"delta": elap, "boxes": boxes, "confidents": confidences, "classIds": classIDs}

        #return animalDictionary

    def resetArrays(self):
        self.animalArray.clear()
        self.horizontalPositionArray.clear()
        self.verticalPositionArray.clear()

    def destroy(self):
        self.vs.stop()


# Testing Area 

#Test = ObjectDetector()
#Test.startDetector("object-detection/yolov3/yolov3/64_v4/yolov3-tiny_last.weights", "object-detection/yolov3/yolov3/64_v4/team5.names", "object-detection/yolov3/yolov3/64_v4/team5.cfg", 256, 192)
#Test.get_label_map()