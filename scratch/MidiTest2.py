import utils as u, random, time, pyautogui
import pygame.midi
import rtmidi
import sys

from rtmidi.midiutil import open_midiinput
#if pygame doesn't work try: https://pypi.org/project/python-rtmidi/
class MidiInputHandler(object):
    def __init__(self, port):
        self.port = port
        self._wallclock = time.time()

    def __call__(self, event, data=None):
        message, deltatime = event
        self._wallclock += deltatime
        print("[%s] @%0.6f %r" % (self.port, self._wallclock, message))
        print("Call")

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