import numpy as np
import time
import cv2
import os
import imutils

class VideoStream:

    def __init__(self):

        current_fps = 0
        myFrame = 0
        myConfidence = 0.76
        myThreshold = 0.4
        limitCPUtemp = True
        cpuTempLimit = 64
        limitToVideoFPS = False
        createOutput = False
        device = "pi"

        from gpiozero import CPUTemperature
        limitToVideoFPS = True
        myWidth = 256
        myHeight = 192
        fps_limit = 5
        my_buffer_size = 1  # number of frames in buffer

        # Networks
        networks = {}
        networks["256_version"] = {"folder": "256_version", "resolution": 256,
                        "weights": "yolov3-tiny.weights"}
        
        selectedNetwork = networks["256_version"]
        myInput = 0

        myDNNsize = selectedNetwork["resolution"]
        winname = selectedNetwork["folder"]
        cv2.namedWindow(winname)
        cv2.moveWindow(winname, 10, 10)

        # load the class labels our YOLO model was trained on
        labelsPath = os.path.sep.join(["yolov3", selectedNetwork["folder"],
                                "obj.names"])
        LABELS = open(labelsPath).read().strip().split("\n")

        # initialize a list of colors to represent each possible class label
        np.random.seed(42)
        COLORS = np.random.randint(0, 255, size=(len(LABELS), 3), dtype="uint8")

        # derive the paths to the YOLO weights and model configuration
        weightsPath = os.path.sep.join(["yolov3", selectedNetwork["folder"],
                                    selectedNetwork["weights"] ])
        configPath = os.path.sep.join(["yolov3", selectedNetwork["folder"],"yolov3-tiny.cfg"])

        # load our trained YOLO object detector (5 classes)
        # and determine only the *output* layer names that we need from YOLO
        print("[INFO] loading YOLO from disk...")
        print(configPath, weightsPath)
        net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
        ln = net.getLayerNames()
        ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        writer = None
        (W, H) = (None, None)


    def getAnimalAndDirection():

        #return animal's name and the direction

        #   top-left  #   top-softleft  #  top-middle   #  top-softright   #  top-right   #        TODO: CHECK VALUE OF BOXES
        # ------------#-----------------#---------------#------------------#------------- #
        # middle-left # middle-softleft # middle-middle # middle-softright # middle-right #
        # ------------#-----------------#---------------#------------------#------------- #
        # bottom-left # bottom-softleft # bottom-middle # bottom-softright # bottom-right #

        animalName = "none"
        animalDirection = "none"
        
        # initialize the video stream, pointer to output video file, and
        # frame dimensions
        vs = cv2.VideoCapture(myInput)

        if(myInput is 0 or myInput is 1):  # Camera
            vs.set(cv2.CAP_PROP_BUFFERSIZE, my_buffer_size)
            # print(f"Buffer size = {vs.get(cv2.CAP_PROP_BUFFERSIZE)}")
            vs.set(cv2.CAP_PROP_FRAME_WIDTH, myWidth)
            vs.set(cv2.CAP_PROP_FRAME_HEIGHT, myHeight)

        # loop over frames from the video file stream (from camera or file)
        while True:
            if limitCPUtemp is True and device is "pi":
                # CPU temp
                cpu = CPUTemperature()
                cpuTemp = cpu.temperature
                # print(cpuTemp)
                while cpuTemp > cpuTempLimit:
                    time.sleep(0.1)
                    cpuTemp = cpu.temperature
                    print("cooling down...")
                    print(cpuTemp)
            
            (grabbed, frame) = vs.read()

            # if the frame was not grabbed, then we have reached the end
            # of the stream
            if not grabbed:
                break
            
            # if the frame dimensions are empty, grab them
            if W is None or H is None:
                (H, W) = frame.shape[:2]

            start = time.time()

            # construct a blob from the input frame and then perform a forward
            # pass of the YOLO object detector, giving us our bounding boxes
            # and associated probabilities
            blob = cv2.dnn.blobFromImage(frame, 1 / 255.0, (myDNNsize, myDNNsize),
                swapRB=True, crop=False)
            net.setInput(blob)
            
            # most CPU intensive part!
            layerOutputs = net.forward(ln)
            
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
                        
            # apply non-maxima suppression to suppress weak, overlapping
            # bounding boxes
            idxs = cv2.dnn.NMSBoxes(boxes, confidences, myConfidence, myThreshold)
            
            # ensure at least one detection exists
            if len(idxs) > 0:
                # loop over the indexes we are keeping
                for i in idxs.flatten():
                    # extract the bounding box coordinates
                    (x, y) = (boxes[i][0], boxes[i][1])
                    (w, h) = (boxes[i][2], boxes[i][3])

                    # draw a bounding box rectangle and label on the frame
                    color = [int(c) for c in COLORS[classIDs[i]]]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 8)
                    text = "{}: {:.4f}".format(LABELS[classIDs[i]],
                        confidences[i])
                    cv2.putText(frame, text, (x, y - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, color, 4)
            
            if createOutput:
                if writer is None:
                    # initialize our video writer
                    fourcc = cv2.VideoWriter_fourcc(*"X264")
                    writer = cv2.VideoWriter(myOutput, fourcc, 30,
                        (frame.shape[1], frame.shape[0]), True)
                # write the output frame to disk
                writer.write(frame)

            # some information on processing single frame   
            myFrame += 1
            end = time.time()
            elap = (end - start)
            current_fps = "{:.2f}".format(1/elap)

            fps = current_fps
            if limitToVideoFPS:
                timeToSleepForFPS = (1 / fps_limit)
                if( timeToSleepForFPS > elap ):
                    timeToSleepForFPS -= elap
                time.sleep(timeToSleepForFPS)
                end = time.time()
                elap_with_delay = end - start
                fps = "{:.2f}".format(1 / elap_with_delay)

            cv2.putText(frame, "DNN FPS: " + current_fps, (5, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0,255,0), 4)
            cv2.putText(frame, "FPS: " + fps, (5, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0,255,0), 4)

            # frame = imutils.resize(frame, height=myHeight, width=myWidth)
            cv2.imshow(selectedNetwork["folder"], frame)

            return animalName + "|" + animalDirection


    def shutDown():

        break
        vs.release()
        cv2.destroyAllWindows()

