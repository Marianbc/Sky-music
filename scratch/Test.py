import utils as u, random, time, pyautogui
import pygame.midi #shit didn't work D:   https://www.pygame.org/docs/ref/midi.html?highlight=midi#module-pygame.midi
import rtmidi #package is python-rtmidi
import sys
import mido
#If you get error creating midi input: https://forum.openmpt.org/index.php?topic=5915.0
#If you need to troubleshoot your MIDI device: https://www.youtube.com/watch?v=AAF-5Soc-ds
#Midi input function for rtmidi: https://github.com/SpotlightKid/python-rtmidi/blob/fcf8214ecba9497bd92fb33bf1f0248ce36e7426/examples/basic/midiin_callback.py
#Rtmidi docs: https://spotlightkid.github.io/python-rtmidi/genindex.html
#a JSON solution to MIDI if rtmidi is too slow I can try this next: https://github.com/BasselR/MIDI-Visualizer/search?q=pygame&unscoped_q=pygame
#old info on sendevent /blah/blah/event2   http://ktnr74.blogspot.com/2013/06/emulating-touchscreen-interaction-with.html
#bad ideas on sending keys: https://stackoverflow.com/questions/3437686/how-to-use-adb-to-send-touch-events-to-device-using-sendevent-command
#For when I want to auto get the event#   https://stackoverflow.com/questions/54228228/adb-how-to-programmatically-determine-which-input-device-is-used-for-sending-to
#
#driver= u.Driver(id)
def piano(x1,y1): # 1-5, 1-3
    #driver.device.shell(f'input tap {480+(x*200)} {10+(y*200)}')  # +200 x, + 200y?
    #driver.press(350+(x*200), 40+(y*200))#480+(x*200), 10+(y*200))
    pyautogui.click(x=180+(x1*80),y=40+(y1*80))#260,120,+80
def midiPiano(note, length=.25):
    #48 = (1,1)
    #72 = (5,3)
    if length == 0:
        None
    else:
        key = round((1/344)*((200*(note-47))+101))
        #print(key)
        if key < 6:
            #print(f'{key} , {1}')
            piano(key,1)
        elif key > 10:
            #print(f'{key - 10} , {3}')
            piano(key-10,3)
        else:
            #print(f'{key - 5} , {2}')
            piano(key-5,2)

with mido.open_input() as inport:
    for msg in inport:
        #note_on channel=0 note=59 velocity=84 time=0
        if msg.velocity > 0:
            midiPiano(msg.note)
        #print(msg)