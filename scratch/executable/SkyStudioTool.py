import time
#import pygame.midi #shit didn't work D:   https://www.pygame.org/docs/ref/midi.html?highlight=midi#module-pygame.midi
#import rtmidi #package is python-rtmidi
import sys
from rtmidi.midiutil import open_midiinput
#If you get error creating midi input: https://forum.openmpt.org/index.php?topic=5915.0
#If you need to troubleshoot your MIDI device: https://www.youtube.com/watch?v=AAF-5Soc-ds
#Midi input function for rtmidi: https://github.com/SpotlightKid/python-rtmidi/blob/fcf8214ecba9497bd92fb33bf1f0248ce36e7426/examples/basic/midiin_callback.py
#Rtmidi docs: https://spotlightkid.github.io/python-rtmidi/genindex.html
#a JSON solution to MIDI if rtmidi is too slow I can try this next: https://github.com/BasselR/MIDI-Visualizer/search?q=pygame&unscoped_q=pygame
#old info on sendevent /blah/blah/event2   http://ktnr74.blogspot.com/2013/06/emulating-touchscreen-interaction-with.html
#bad ideas on sending keys: https://stackoverflow.com/questions/3437686/how-to-use-adb-to-send-touch-events-to-device-using-sendevent-command
#For when I want to auto get the event#   https://stackoverflow.com/questions/54228228/adb-how-to-programmatically-determine-which-input-device-is-used-for-sending-to
#
t = 0
def midiPiano(note, length=.25):
    global t
    #48 = (1,1)
    #72 = (5,3)
    if length == 0:
        None
    else:
        #47 C - C
        #44 A - A
        #Different key formula needed based on, what key you want to compose in

        key = round((1/344)*((200*(note-keyDict[keySignature]))+101)) - 1

        print(key)
        if (key < 15) and (key > -1):
            log_note('{\"time\":' + f'{t},' + '\"key\":\"1Key' + f'{key}' + '\"},')
            t = t + 250
fileName= input("Name of Piece?: ")
keySignature= input("Key Signature Letter (b for flat): ")
keyDict = {
    "A": 44,
    "Bb": 45,
    "B": 46,
    "C": 47,
    "Db": 48,
    "D": 49,
    "Eb": 50,
    "E": 51,
    "F": 52,
    "Gb": 53,
    "G": 54,
    "Ab": 55
}

def log_note(code):
    #global error_Count
    #error_Count += 1
    fw = open(f"{fileName}.txt", "a+")
    fw.write(code)
    fw.close()

pitchLevel=keyDict[keySignature]-47
if pitchLevel < 0:
    pitchLevel += 12
print(pitchLevel)
log_note("[{\"name\":\"" + f"{fileName}\",\"bpm\":240,\"bitsPerPage\":16,\"pitchLevel\":{pitchLevel},\"songNotes\":[")


#if pygame doesn't work try: https://pypi.org/project/python-rtmidi/
class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        #print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))
        #print(f'Call: {message[1]}')
        midiPiano(message[1], message[2]) #message is [something, key, time(ms?)]

port = sys.argv[1] if len(sys.argv) > 1 else None


try:
    midiin, port_name = open_midiinput(port)
except (EOFError, KeyboardInterrupt):
    sys.exit()

print("Attaching MIDI input callback handler.")
midiin.set_callback(MidiInputHandler(port_name))

print("Entering main loop. Press Control-C to exit.")
try:
    # Just wait for keyboard interrupt,
    # everything else is handled via the input callback.
    while True:
        print("wait?")

        time.sleep(1)
except KeyboardInterrupt:
    print("HELLO?!?!")
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin