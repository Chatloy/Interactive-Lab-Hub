

# Staging Interaction

In the original stage production of Peter Pan, Tinker Bell was represented by a darting light created by a small handheld mirror off-stage, reflecting a little circle of light from a powerful lamp. Tinkerbell communicates her presence through this light to the other characters. See more info [here](https://en.wikipedia.org/wiki/Tinker_Bell). 

There is no actor that plays Tinkerbell--her existence in the play comes from the interactions that the other characters have with her.

For lab this week, we draw on this and other inspirations from theatre to stage interactions with a device where the main mode of display/output for the interactive device you are designing is lighting. You will plot the interaction with a storyboard, and use your computer and a smartphone to experiment with what the interactions will look and feel like. 

_Make sure you read all the instructions and understand the whole of the laboratory activity before starting!_



## Prep

### To start the semester, you will need:
1. Set up your own Github "Lab Hub" repository to keep all you work in record by [following these instructions](https://github.com/FAR-Lab/Developing-and-Designing-Interactive-Devices/blob/2021Fall/readings/Submitting%20Labs.md).
2. Set up the README.md for your Hub repository (for instance, so that it has your name and points to your own Lab 1) and [learn how to](https://guides.github.com/features/mastering-markdown/) organize and post links to your submissions on your README.md so we can find them easily.
3. (extra: Learn about what exactly Git is from [here](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F).)

### For this lab, you will need:
1. Paper
2. Markers/ Pens
3. Scissors
4. Smart Phone -- The main required feature is that the phone needs to have a browser and display a webpage.
5. Computer -- We will use your computer to host a webpage which also features controls.
6. Found objects and materials -- You will have to costume your phone so that it looks like some other devices. These materials can include doll clothes, a paper lantern, a bottle, human clothes, a pillow case, etc. Be creative!

### Deliverables for this lab are: 
1. Storyboard
1. Sketches/photos of costumed device
1. Any reflections you have on the process
1. Video sketch of the prototyped interaction
1. Submit the items above in the lab1 folder of your class [Github page], either as links or uploaded files. Each group member should post their own copy of the work to their own Lab Hub, even if some of the work is the same from each person in the group.

### The Report
This README.md page in your own repository should be edited to include the work you have done (the deliverables mentioned above). Following the format below, you can delete everything but the headers and the sections between the **stars**. Write the answers to the questions under the starred sentences. Include any material that explains what you did in this lab hub folder, and link it in your README.md for the lab.

## Lab Overview
For this assignment, you are going to:

A) [Plan](#part-a-plan) 

B) [Act out the interaction](#part-b-act-out-the-interaction) 

C) [Prototype the device](#part-c-prototype-the-device)

D) [Wizard the device](#part-d-wizard-the-device) 

E) [Costume the device](#part-e-costume-the-device)

F) [Record the interaction](#part-f-record)

Labs are due on Mondays. Make sure this page is linked to on your main class hub page.

## Part A. Plan 

To stage the interaction with your interactive device, think about:

_Setting:_ Where is this interaction happening? (e.g., a jungle, the kitchen) When is it happening?

_Players:_ Who is involved in the interaction? Who else is there? If you reflect on the design of current day interactive devices like the Amazon Alexa, it’s clear they didn’t take into account people who had roommates, or the presence of children. Think through all the people who are in the setting.

_Activity:_ What is happening between the actors?

_Goals:_ What are the goals of each player? (e.g., jumping to a tree, opening the fridge). 

The interactive device can be anything *except* a computer, a tablet computer or a smart phone, but the main way it interacts needs to be using light.

\*\***Describe your setting, players, activity and goals here.**\*\*

**_Setting:_** 
It happens in Iris's home or any other users' home or workplace.

**_Players:_**
It involves one lonely user occupied by working, studying or exercising. In my storyboard, Iris is working out while watch fitness video so she couldn't pay attention to the dangerous boiling kettle. Since she is living alone, her families and friends couldn't help her with boiling water and the only helper might be our TickerBell.

**_Activity:_**
Iris is working out and her room is little far from kitchen and she is fully concentrated on the fitness exercises. She wanted to drink warm water, neither hot nor cold. 
And the boiling water could be dangerous since boiling water will overflow from the pot.

**_Goals:_**
Iris's goal is to exercise and to lose weight. And after she finished, she wants to drink warm water for she sweats a lot and feels extremely thirsty.
The goal of the TickerBell activity is to remind the user when the water or food in impropriate temperature.


Sketch a storyboard of the interactions you are planning. It does not need to be perfect, but must get across the behavior of the interactive device and the other characters in the scene. 

\*\***Include a picture of your storyboard here**\*\*

![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%201/assignment1_story_board_pic.jpg)


Present your idea to the other people in your breakout room. You can just get feedback from one another or you can work together on the other parts of the lab.

\*\***Summarize feedback you got here.**\*\*

1. Beautifully drawing.
2. This idea is brilliant and it can free us from keeping an eye on the boiling pot all the time.
3. I think Jiejun has done a great job in the picturing of the setting-up and background story-telling. However, it may lack of imagination for the idea of using tinkerbelle as the temperature reminder is a little bit common.


## Part B. Act out the Interaction

Try physically acting out the interaction you planned. For now, you can just pretend the device is doing the things you’ve scripted for it. 

\*\***Are there things that seemed better on paper than acted out?**\*\*

Yes. During the implemention, I discovered that I made a mistake in the first version of my story-board for I used two different kinds of semaphore in one project. At first, I employed red color to represent the high temperature, while adopting blue to represent the insufficient volume of water. They are two different variables, but I use the same lind of signal to represent them. It could be really confusing to the users. However, during the logical thinking part, I just wanted to develop the product with more functions and sometimes may ignore user experience.

\*\***Are there new ideas that occur to you or your collaborators that come up from the acting?**\*\*

Yes!(And it's a happy answer.) After I watched some videos of other experiments on using lights or sounds as the reminder, I was inspired to introduce more colors in this project and different color-pairs may represent different signals but in color-pairs, the two colors should be in sharp contrast in each other to indicate the two difference conditions, like hot or cold. 
And I also reconsider the whole idea of the temperature reminder because it does seem a little plain and the intelligent appliances could helper us with the temperature issues.So I came up with the new idea to employ the tinkerbell as the Heart rate detector while Iris is working out to help her figure out whether she is . 

## Part C. Prototype the device

You will be using your smartphone as a stand-in for the device you are prototyping. You will use the browser of your smart phone to act as a “light” and use a remote control interface to remotely change the light on that device. 

Code for the "Tinkerbelle" tool, and instructions for setting up the server and your phone are [here](https://github.com/FAR-Lab/tinkerbelle).

We invented this tool for this lab! 

If you run into technical issues with this tool, you can also use a light switch, dimmer, etc. that you can can manually or remotely control.


\*\***Give us feedback on Tinkerbelle.**\*\*

It seems really cool but a liitle bit troublesome to install it in the environment of Python 3.8.


## Part D. Wizard the device
Take a little time to set up the wizarding set-up that allows for someone to remotely control the device while someone acts with it. Hint: You can use Zoom to record videos, and you can pin someone’s video feed if that is the scene which you want to record. 

\*\***Include your first attempts at recording the set-up video here.**\*\*

https://drive.google.com/file/d/1Bc-J_nJhZCUVlQPPKv8Ap9S0vKgxIF4Z/view?usp=sharing

Now, hange the goal within the same setting, and update the interaction with the paper prototype. 

\*\***Show the follow-up work here.**\*\*

https://drive.google.com/file/d/1QV257R2JEnjhFWkFru8zCuIE-KJ6fohX/view?usp=sharing

## Part E. Costume the device

Only now should you start worrying about what the device should look like. Develop a costume so that you can use your phone as this device.

Think about the setting of the device: is the environment a place where the device could overheat? Is water a danger? Does it need to have bright colors in an emergency setting?

\*\***Include sketches of what your device might look like here.**\*\*

![Chatloy](https://github.com/Chatloy/Interactive-Lab-Hub/blob/Fall2021/Lab%201/imagined-pic.jpg)


\*\***What concerns or opportunitities are influencing the way you've designed the device to look?**\*\*

Part of the reason that makes me this way is resources, and I want to save as much as possible. All the time when the pot is not in use, I want to leave the tinkerbelle in the off state.
But when it approaches boiling point, I want it to go into a very intense red color to alert the user because the boiling stove is very dangerous. 
Just picture it as the smoke alert.

## Part F. Record

\*\***Take a video of your prototyped interaction.**\*\*

The simple version of the prototyoed interaction:

https://drive.google.com/file/d/1lQhKNAn4bGiKox5UcS5_9Hn-g0Zxq8Fu/view?usp=sharing

\*\***Please indicate anyone you collaborated with on this Lab.**\*\*
Be generous in acknowledging their contributions! And also recognizing any other influences (e.g. from YouTube, Github, Twitter) that informed your design. 

Actually, in this project, I haven't collaborated with any classmates, which is of course I need to improve about. 
And thanks my roommates for the feedback of this project.


# Staging Interaction, Part 2 

This describes the second week's work for this lab activity.


## Prep (to be done before Lab on Wednesday)

You will be assigned three partners from another group. Go to their github pages, view their videos, and provide them with reactions, suggestions & feedback: explain to them what you saw happening in their video. Guess the scene and the goals of the character. Ask them about anything that wasn’t clear. 

\*\***Summarize feedback from your partners here.**\*\*

## It seems I just have two partners from another group and I got their feedbacks. 

Their reviews are very real and instructive. And it inspires me to develop a better idea. And here is the summarization of their feedbacks:
1.(From Yehao Zhang) He thinks this device was used to let people know the temperature of the food when they were cooking. And it's intuitive to use colors to indicate the temperature. But he wondered that in what situations would such a device be better than a kitchen thermometer. 

2.(From Lauren Alexis Tran) Lauren liked the storyboard and the idea about different color conveying different information. However, the video 


## Make it your own

Do last week’s assignment again, but this time: 
1) It doesn’t have to (just) use light, 
2) You can use any modality (e.g., vibration, sound) to prototype the behaviors! Again, be creative!
3) We will be grading with an emphasis on creativity. 

\*\***Document everything here. (Particularly, we would like to see the storyboard and video, although photos of the prototype are also great.)**\*\*
