import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap

import json

def main():
     controller = Leap.Controller()


     # Keep this process running until Enter is pressed
     print "Press Enter to quit..."
     try:
         sys.stdin.readline()
     except KeyboardInterrupt:
         pass



def thumb_across( prev_frame=frame.id-1, call_number=0):
    frame=controller.frame()
    fingers=frame.hand[0].fingres
    thumb=fingers.finger_type(Finger.TYPE_THUMB)
    thumb_position=type.thumb.jointIX[3]
    pinky_position=type.pinky.jointIX[0]

    def distance (x1,y1,x2,y2,z1,z2):
        dx=x2-x1
        dy=y2-y1
        dz=z2-z1
        dsquared=dx**2+dy**2+dz**2
        return dsquared**.5

    if (frame.id)
    thumb_coord=frame.


