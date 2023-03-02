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

directory = input("Chose directory were to save all the slide: ")
video = input("Enter name of the file to transform in slide: ")
seconds = input("Insert the number of seconds that need to be equal to grab that as a slide ")

initTime = datetime.now().timestamp()

try:
    if not os.path.exists(directory):
        os.makedirs(directory)
except OSError:
    print ('Error: Creating directory of data')

vidcap = cv2.VideoCapture(video)

fps = vidcap.get(cv2.CAP_PROP_FPS)
nFrame = fps * float(seconds)

sFrame = 0
printed = 1
success, image1 = vidcap.read()
result = image1

totalScannedFrame=0
minuti=0

while success:
    success, image2 = vidcap.read()
    totalScannedFrame+=1

    #convert image to cv2 to PIL to use rmsdiff function
    color_converted = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
    im1=Image.fromarray(color_converted)
    color_converted = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
    im2=Image.fromarray(color_converted)
    
    if(((totalScannedFrame/fps)/60)%1==0):
        minuti +=60
        actualTime= datetime.now().timestamp()
        difference= actualTime-initTime
        print("scanned "+ str(minuti)+" seconds in "+str(difference)+" seconds")
        
    difference = rmsdiff(im1, im2)
    if(difference <= 40):
       result = equalPart(result, image2)
       sFrame +=1
       if(sFrame==nFrame):
          name = './'+ directory +'/slide' + str(printed) + '.jpg'
          printed += 1
          print ('Creating...' + name)
          cv2.imwrite(name, result)
       if(sFrame>nFrame):
          cv2.imwrite(name, result)
    else:
        success, image1 = vidcap.read()
        result = image1
        sFrame=0











