 # Slode
A simple tool to grab slide from a video
## How to use
### Install requirements
In the command prompt, go to the Slode folder and run

	pip install -r requirements.txt

### Run Slode
To run slode you need to type in the command promt

	python3 slode.py [arguments] -v VIDEO

Possible arguments are:

 - -h, --help => show help message and exit  
 - -v VIDEO, --video VIDEO  => Chose the video name and location (with extension)  
 - -s {fast,slow}, --speed {fast,slow}  Chose the speed of the scan (fast or slow), default is fast (more information about the difference here)
 - -d DIRECTORY, --directory DIRECTORY  => chose the slide save location , default is slide/  
 - -t TIME, --time TIME =>Chose the minimum duration (in seconds) of a frame to be considered a slide, default is 10  
 - -fd FRAME_DIFFRENCE, --frame_difference FRAME_DIFFRENCE  => Chose the maximum root-mean-square (RMS) value of the difference between two successive frames to be considered equal, default is 40 (more information here)
##### Example
Save all the slide of presentation.mp4 to slide/
	
	python3 slode.py -v presentation.mp4

## How it works
### Slow
The tool works by scanning the video and taking every frame of it.
It then compares two successive frames and if they have the root mean square value (RMS) of the difference lower than the chosen one (default is 40) it considers the two frames equal.
When the number of equal frames is equal to the chosen number of frames, i.e. the fps of video for the minimum duration of a slide, it proceed with a process that tries to eliminate everything that is different in the various "equal" frames, removing any moving faces and highlighting the movement of the cursor during the presentation.
It proceeds by saving the frame in the chosen directory as slideN.jpg and restarts with the scanning of the following frames.
##### Pro

 - It's very accurate
 - Remove faces

##### Cons

 - It's really slow (like 60 video seconds in 75 seconds)
 - It can be difficult to read if the cursor has been moved a lot
 - The names of those present are not removed
 - It does not remove the part around the slides

### Fast
The tool works by scanning the video and taking one frame per second of it.
Then it compares two successive frames and if they have the root mean square value (RMS) of the difference lower than the one set (by default it is 40) it considers the two frames equal.
When the number of equal frames is equal to the chosen number of frames, i.e. the fps of the video for the minimum duration of a slide, it proceeds by saving the frame in the selected directory as slideN.jpg and then restarts the scan with the following frames.

##### Pro
 
 - Has an acceptable speed (like 60 video seconds in 5 seconds)

##### Cons

 - Does not work with non-integer slide duration
 - Sometimes it risks losing slides
 - It does not remove the part around the slides

## Work in progress

 - [ ] Part removal around the slide
 - [ ] Possibility of using a GUI
 - [ ] possibility of choosing the number of frames per second to take
