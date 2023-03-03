import cv2
import os
from PIL import Image
from PIL import ImageChops
import math, operator
import functools
from datetime import datetime
import argparse
import art
import sys
#import other file
sys.path.append('lib')
import slow
import fast

parser = argparse.ArgumentParser(description ='Slide from video grabber')
parser.add_argument('-v', '--video', dest = 'video', 
                    required = True,
                    help ='Insert the video name and location (with extension)')
parser.add_argument('-s', '--speed', dest = 'speed', default ='fast', choices = ['fast', 'slow'],
                    help ='Insert the speed of the scan (fast or slow), see documentation for more info')
parser.add_argument('-d', '--directory', dest = 'directory',
                    default = 'slide',
                    help ='Slide save location')
parser.add_argument('-t', '--time', dest = 'time', 
                    default = '10', type = float,
                    help ='Enter the minimum duration (in seconds) of a frame to be considered a slide')
parser.add_argument('-fd', '--frame_difference', dest = 'frame_diffrence', 
                    default = '40', type = float,
                    help ='Enter the maximum root-mean-square (RMS) value of the difference between two successive frames to be considered equal')
args = parser.parse_args()

video = args.video
speed = args.speed
directory = args.directory
time = args.time
frameDifference = args.frame_diffrence

print(art.text2art("Slode"))
print("A simple tool to grab slide from a video")

#create directory if dont exist
try:
    if not os.path.exists(directory):
        os.makedirs(directory)
except OSError:
    exit('Error: Creating directory of data')
    
print()

try:
    if(speed=="fast"):
        print("Starting with fast mode")
        fast.fast(directory, video, time, frameDifference)
        
    elif(speed=="slow"):
        print("Starting with slow mode")
        slow.slow(directory, video, time, frameDifference)
        
except Exception:
    exit("unhandled error, please report it on github")
