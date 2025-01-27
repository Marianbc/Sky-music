import utils as u, random, time, pyautogui
#https://pypi.org/project/pure-python-adb/

#id= input("id:")
driver= u.Driver(id)
#driver.press(480,358) #logout
def piano(x1,y1,wait=0): # 1-5, 1-3
    #driver.device.shell(f'input tap {480+(x*200)} {10+(y*200)}')  # +200 x, + 200y?
    #driver.press(350 + (x * 200), 40 + (y * 200))  # 480+(x*200), 10+(y*200))
    pyautogui.click(x=180 + (x1 * 80), y=40 + (y1 * 80))  # 260,120,+80
    #time.sleep(wait)
#pyautogui.MINIMUM_DURATION = 0
pyautogui.PAUSE = 0
#driver.device.shell("input tap 680 210") # +200 x, + 200y?
piano(5,3)
piano(2,3)
piano(5,2)
piano(5,3)
piano(4,3)
piano(2,3)
#time.sleep(.2)
piano(2,3)
piano(5,3)
piano(4,3)
piano(3,3)
piano(4,3)
piano(5,3)
piano(2,3)
piano(5,2)
piano(5,3)
piano(4,3)
piano(2,3)
#time.sleep(.2)
piano(2,3)
piano(5,3)
piano(4,3)
piano(3,3)
piano(2,3)
piano(1,3)

piano(5,3)
piano(5,3)
piano(5,3)

piano(1,3)
piano(1,3)

piano(5,3)
piano(5,3)
piano(5,3)

piano(4,3)
piano(5,3)
piano(4,3)
piano(5,3)
piano(4,3)
piano(2,3)

piano(4,3)
piano(5,3)
piano(4,3)
piano(4,3)
piano(5,3)
piano(4,3)
piano(3,3)
piano(4,3)