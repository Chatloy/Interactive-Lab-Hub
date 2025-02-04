
# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV
A more traditional method to extract information out of images is provided with OpenCV. The RPI image provided to you comes with an optimized installation that can be accessed through python. We included 4 standard OpenCV examples: contour(blob) detection, face detection with the ``Haarcascade``, flow detection (a type of keypoint tracking), and standard object detection with the [Yolo](https://pjreddie.com/darknet/yolo/) darknet.

Most examples can be run with a screen (e.g. VNC or ssh -X or with an HDMI monitor), or with just the terminal. The examples are separated out into different folders. Each folder contains a ```HowToUse.md``` file, which explains how to run the python example. 

Following is a nicer way you can run and see the flow of the `openCV-examples` we have included in your Pi. Instead of `ls`, the command we will be using here is `tree`. [Tree](http://mama.indstate.edu/users/ice/tree/) is a recursive directory colored listing command that produces a depth indented listing of files. Install `tree` first and `cd` to the `openCV-examples` folder and run the command:

```shell
pi@ixe00:~ $ sudo apt install tree
...
pi@ixe00:~ $ cd openCV-examples
pi@ixe00:~/openCV-examples $ tree -l
.
├── contours-detection
│   ├── contours.py
│   └── HowToUse.md
├── data
│   ├── slow_traffic_small.mp4
│   └── test.jpg
├── face-detection
│   ├── face-detection.py
│   ├── faces_detected.jpg
│   ├── haarcascade_eye_tree_eyeglasses.xml
│   ├── haarcascade_eye.xml
│   ├── haarcascade_frontalface_alt.xml
│   ├── haarcascade_frontalface_default.xml
│   └── HowToUse.md
├── flow-detection
│   ├── flow.png
│   ├── HowToUse.md
│   └── optical_flow.py
└── object-detection
    ├── detected_out.jpg
    ├── detect.py
    ├── frozen_inference_graph.pb
    ├── HowToUse.md
    └── ssd_mobilenet_v2_coco_2018_03_29.pbtxt
```

The flow detection might seem random, but consider [this recent research](https://cseweb.ucsd.edu/~lriek/papers/taylor-icra-2021.pdf) that uses optical flow to determine busy-ness in hospital settings to facilitate robot navigation. Note the velocity parameter on page 3 and the mentions of optical flow.

Now, connect your webcam to your Pi and use **VNC to access to your Pi** and open the terminal. Use the following command lines to try each of the examples we provided:
(***it will not work if you use ssh from your laptop***)

```
pi@ixe00:~$ cd ~/openCV-examples/contours-detection
pi@ixe00:~/openCV-examples/contours-detection $ python contours.py
...
pi@ixe00:~$ cd ~/openCV-examples/face-detection
pi@ixe00:~/openCV-examples/face-detection $ python face-detection.py
...
pi@ixe00:~$ cd ~/openCV-examples/flow-detection
pi@ixe00:~/openCV-examples/flow-detection $ python optical_flow.py 0 window
...
pi@ixe00:~$ cd ~/openCV-examples/object-detection
pi@ixe00:~/openCV-examples/object-detection $ python detect.py
```

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

#### Contours Detection<br>
This detection can be used to detect the borders of objects so we could obtain outlines extracted from original image and outlines could be used to tell the difference between objects.<br>
Potential design example: Object classifing system.<br>
We can use the contours detection to classify different objects. For example, the scissors with sharp edges and balls with round angles. We could use it to keep the dangerous objects away from children. <br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/1.jpg)<br>


#### Face Detection<br>
This detection could detect human faces. And it is really helpful when being adopted in the security system. We can build the access control system based on the face detection. <br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/2.jpg)<br>

#### Flow Detection<br>
The detection could be used to track the trajectory of moving objects. We could use it to build the system to record the movement track of objects. <br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/3.jpg)<br>

#### MediaPipe

#### MediaPipe

A more recent open source and efficient method of extracting information from video streams comes out of Google's [MediaPipe](https://mediapipe.dev/), which offers state of the art face, face mesh, hand pose, and body pose detection.

![Alt Text](mp.gif)

To get started, create a new virtual environment with special indication this time:

```
pi@ixe00:~ $ virtualenv mpipe --system-site-packages
pi@ixe00:~ $ source mpipe/bin/activate
(mpipe) pi@ixe00:~ $ 
```

and install the following.

```
...
(mpipe) pi@ixe00:~ $ sudo apt install ffmpeg python3-opencv
(mpipe) pi@ixe00:~ $ sudo apt install libxcb-shm0 libcdio-paranoia-dev libsdl2-2.0-0 libxv1  libtheora0 libva-drm2 libva-x11-2 libvdpau1 libharfbuzz0b libbluray2 libatlas-base-dev libhdf5-103 libgtk-3-0 libdc1394-22 libopenexr23
(mpipe) pi@ixe00:~ $ pip3 install mediapipe-rpi4 pyalsaaudio
```

Each of the installs will take a while, please be patient. After successfully installing mediapipe, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the hand pose detection script we provide:
(***it will not work if you use ssh from your laptop***)


```
(mpipe) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(mpipe) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python hand_pose.py
```


Try the two main features of this script: 1) pinching for percentage control, and 2) "[Quiet Coyote](https://www.youtube.com/watch?v=qsKlNVpY7zg)" for instant percentage setting. Notice how this example uses hardcoded positions and relates those positions with a desired set of events, in `hand_pose.py` lines 48-53. <br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/5.1.jpg)<br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/5.2.jpg)<br>


**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

(You might also consider how this notion of percentage control with hand tracking might be used in some of the physical UI you may have experimented with in the last lab, for instance in controlling a servo or rotary encoder.)

![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/4.jpg)<br>

#### Teachable Machines
Google's [TeachableMachines](https://teachablemachine.withgoogle.com/train) might look very simple. However, its simplicity is very useful for experimenting with the capabilities of this technology.

![Alt Text](tm.gif)

To get started, create and activate a new virtual environment for this exercise with special indication:

```
pi@ixe00:~ $ virtualenv tmachine --system-site-packages
pi@ixe00:~ $ source tmachine/bin/activate
(tmachine) pi@ixe00:~ $ 
```

After activating the virtual environment, install the requisite TensorFlow libraries by running the following lines:
```
(tmachine) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 5
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ sudo chmod +x ./teachable_machines.sh
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ ./teachable_machines.sh
``` 

This might take a while to get fully installed. After installation, connect your webcam to your Pi and use **VNC to access to your Pi**, open the terminal, and go to Lab 5 folder and run the example script:
(***it will not work if you use ssh from your laptop***)

```
(tmachine) pi@ixe00:~ Interactive-Lab-Hub/Lab 5 $ python tm_ppe_detection.py
```


(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/normal.jpg)<br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/hands-up.jpg)<br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/sleepy.jpg)<br>

*Don't forget to run ```deactivate``` to end the Teachable Machines demo, and to reactivate with ```source tmachine/bin/activate``` when you want to use it again.*


#### Filtering, FFTs, and Time Series data. (optional)
Additional filtering and analysis can be done on the sensors that were provided in the kit. For example, running a Fast Fourier Transform over the IMU data stream could create a simple activity classifier between walking, running, and standing.

Using the accelerometer, try the following:

**1. Set up threshold detection** Can you identify when a signal goes above certain fixed values?

**2. Set up averaging** Can you average your signal in N-sample blocks? N-sample running average?

**3. Set up peak detection** Can you identify when your signal reaches a peak and then goes down?

**\*\*\*Include links to your code here, and put the code for these in your repo--they will come in handy later.\*\*\***


### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***<br>
The interaction I chose to design involved the face detection model. The goal of the interaction is to simulate the online lecturing system with facial recognition. The background would be the online teaching in zoom is quite common currently. However, comparing to the physical in-person lessons, the online lecturing could be troublesome in some technical aspects. For example, it's impossible for students who taking courses via zoom to check in when the course is presenting in the hybrided way. Moreover, on online course, students may not be as concentrated as enough.<br>
Targetted at these problems, I was hoping to use this Teachable Machines Model to help with an online system with automatic checking-in and also behavior monitoring functions.  That it to say, this system is able to help students automatically check-in and it will product a report such as "Chatloy has logged in. There are 43 students in class now." on the screen. Also, I would use the classification function to tell the state of students, such as normal, hands-up 🙌  or sleepy. And the abnormal state might be reported to professors.<br>


### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?<br>
When it was required to detect human faces and to clarify the state of students, whether they are sleepy, normal or hands-up.
2. When does it fail?<br>
(1)Lots of times. It was actually pretty interesting to watch the model detect what it thought were facial features. I eventually settled on labeling the face as a "count" only if eyes were detected. In addition, I tried putting several objects in front of it that could possibly trip it up to see how robust it could be in face detection.<br>
(2)Also, to implement the classification function, the boundary between sleepy and normal state is really not clear. At first, I wanted to use the state of eyes to identify the difference between sleepy and normal. Then I discovered it's impossible for keep the eye open all the time for 40 minute. So, if we are capturing the picture when the students are blinking, then it will be classified into wrong state which is the sleepy instead of normal.<br>
So I deliberately selected pictures with a large portion ratio gap between face and hair to train the model.<br>
For example:
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/n1.jpg)<br>
![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%205/imgs/n2.jpg)<br>

(3)About the hands-up state, at first, I didn't think about the difference between the students when they are raising their left hand or right hand. But it is claimed by result that this is one point I need to pay attention to. The position of the hand in the frame will affect the results. So I need to train both raising left hand state and also the raising right hand state.<br>

Why does it fail?<br>
I think it's related to the data pre-processing and the model itself. Sometimes, it will recogize some irrelevant lines as human faces.<br>
Same explanation as above.<br>
(1)The complexity of the background.<br>
(2)The unclear boundary between the sleepy and normal state.<br>
(3)The different directions and positions students raising their hands.<br>

3. Based on the behavior you have seen, what other scenarios could cause problems?<br>
(1)If the setting-up behind the faces is quite complex, it may fail.(Such as the unorganized room).<br>
(2)I also think the amount/color of hair may affect the result for currently, I just used my picture to set up the boundary and my hair is dark-colored. I am sure that for people with light-colored hair might have different testing results for my training dataset is not diversed enough.<br>

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?<br>
Yes. Of course. And in order to achieve better performance of the model, I may suggest them sit in front of the white wall to use it as the background. It will avoid the impact of complex lines. And if the students don't want to be recognized as sleepy state and be reported to the professor, they might need to stare the screen or at least raise their head.

2. How bad would they be impacted by a miss classification?<br>
Actually, the worst case might be the model has recognized some lines as a human face but since there would be no one to log in at that time. So this mis-detection wouldn't cause too much trouble. The worst result would be a hard-working student being recognized as sleepy. <br>

3. Are there optimizations you can try to do on your sense-making algorithm.<br>
(1) If I could, I wanted to skip the log-in part but use the face recognition to get their identity and log in for them automatically. But it is too hard, for I have no access to the face-to-name database and I have no idea about how to connect this database to the RPi.<br>
(2)I also tried the pose project version of the teachable machine. And I really considered for this classification, if I could use dynamic video detection instead of building models based on static images, the results would be more accurate. <br>
The above are the optimizations I haven't implemented. The next one has alreay optimized.
(3)I noticed that while taking courses, students are moving all the time. And it would affect the testing results for when moving, the camera will caputering blurred moving images instead of the standard static pictures which the model required. So I decided to use the button of miniTFT to decide when to capture the picture of students. If we press the button, the camera will take pictures at that moment. So instead of using static model to detect dynamic information, I turned the information static too.


### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***<br>
This interaction video was showing the state switching between the normal and sleepy state.<br>

https://drive.google.com/file/d/1oQ-sqcSnfZAK5kTCOMp-lxzCEBg3IyE3/view?usp=sharing
