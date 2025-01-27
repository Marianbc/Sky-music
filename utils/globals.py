import os

adbId= 62025 #62001 62025 62026
adbCmd= f"adb -s 127.0.0.1:{adbId} "
shellCmd= adbCmd + "shell "
# adbCmd= f"adb -s HT76L0200789 "

#adbDir= r"C:\Program Files (x86)\Nox\bin/"
#os.chdir(adbDir)

cacheDir= r"C:\Users\Brandon\PycharmProjects\coa/cache/"

dct= {
	'atk': (875, 460), # 1750,920), # atk key
	'int': (880, 350), #1750,720), # interact key
	'inv': (860, 160), #1700,290),
	'optns': (875,70), #open options menu for logout
	'logout': (477,357),
	'close': (888,235), #close bank

	'r': 50, # width / height of inv slot
	'inv0': (180, 130), #430,270), # top-left inv slot
	'stor0': (185, 135), #370,270), # top-left storage slot
	'stor00': (500, 135), #1000,270),
	'wcob': (598,285), #withdrawl cobalt ore
	'wvarax': (548,335),

	'left': 0x69,
	'up': 0x67,
	'right': 0x6a,
	'down': 0x6c,

	'hp1': (763, 83),#1525,165),
	'hp2': (663, 83),#1375,165),
	'hp3': (613, 83),#1225,165)
}