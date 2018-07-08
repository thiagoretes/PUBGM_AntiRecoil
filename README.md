# PUBG Mobile Anti-Recoil
This is a simple script written in python to auto-shoot + control recoil of weapons in pubg mobile using feature detection for calculating the translation of the screen, just like a camera stabilizer would do probably.
I made this for learning purposes, so don't expect it to run perfectly, it may be buggy sometimes.
# How it works
The algorithm is simple:
1. Wait for the middle button of mouse to be pressed.
    1. Grab the central part of screen(for this I use mss, as it claims to be the fastest way to grab screen in python), I'll call this as OLD_IMG.
1. While middle button of mouse is pressed do.
    1. Grab another image of the same part of screen. This I'll call as NEW_IMG.
    1. Just call ORB using OLD_IMG and NEW_IMG as the parameters. It'll detect some high quality points in image for detecting it's translation. Returns the keypoints and their respective descriptors.
    1. Using the descriptors of both images, use a brute force matcher to match them between the OLD_IMG and NEW_IMG.
    1. Sort them according to their distance.
    1. Use the best X matches to calculate the translation vector between imgs.
    1. Use the translation vector(dx,dy) to send mouse input and correct the recoil.
##Note: It works using the mouse events of **WINDOWS** so, it won't run in linux.
