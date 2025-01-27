import utils as u, random, time, pyautogui
import pygame.midi
#Shit didn't work

#if pygame doesn't work try: https://pypi.org/project/python-rtmidi/

#gives midi connected devices info
pygame.midi.init()
print(pygame.midi.get_default_input_id())
print(pygame.midi.get_count())
for r in range(pygame.midi.get_count()):
    print(f'device #: {r}')
    print(pygame.midi.get_device_info(r))
#set input device:
midy = pygame.midi.Input(1)

while True:
    print(1)
    while midy.poll():
        data = midy.read(1)
        if len(data) == 0:
            break
        print(data[0][0])
midy.close()
#pygame.midi.quit()