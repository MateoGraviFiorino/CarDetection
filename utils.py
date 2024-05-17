import cv2
import numpy as np

def preprocess_image(img, net):
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    return net.forward(net.getUnconnectedOutLayers())
