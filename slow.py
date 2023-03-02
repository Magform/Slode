import cv2
import os
from PIL import Image
from PIL import ImageChops
import math, operator
import functools
from datetime import datetime

def rmsdiff(im1, im2):
    h = ImageChops.difference(im1, im2).histogram()
    return math.sqrt(functools.reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))

def equalPart(im1, im2):
    difference = cv2.subtract(im1, im2)
    results = cv2.subtract(im1, difference)
    return results
    
def slow(directory, video, time, frameDifference):
    vidcap = cv2.VideoCapture(video)

    totalScannedFrame=0
    minuti=0
    initTime = datetime.now().timestamp()
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    requestFrame = fps * float(time)
    goodFrame = 0
    slidePrinted = 1
    success, image1 = vidcap.read()
    totalScannedFrame = 0
    secs = 0
    loaded = 0
    result = image1


    while success:
        success, image2 = vidcap.read()
        totalScannedFrame+=1

        #convert image to cv2 to PIL to use rmsdiff function
        color_converted = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
        im1=Image.fromarray(color_converted)
        color_converted = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
        im2=Image.fromarray(color_converted)
    
        if(((totalScannedFrame/fps)/60)%1==0):
            secs +=60
            actualTime= datetime.now().timestamp()
            timeDifference= actualTime-initTime
            print("scanned "+ str(secs)+" seconds in "+str(timeDifference)+" seconds")
        
        difference = rmsdiff(im1, im2)
        if(difference <= frameDifference):
            result = equalPart(result, image2)
            goodFrame +=1
            if(goodFrame==requestFrame):
                name = './'+ directory +'/slide' + str(slidePrinted) + '.jpg'
                slidePrinted += 1
                print ('Creating...' + name)
                cv2.imwrite(name, result)
            if(goodFrame>requestFrame):
                cv2.imwrite(name, result)
        else:
            success, image1 = vidcap.read()
            result = image1
            goodFrame=0











