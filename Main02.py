import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume

"""
	TODO
		Gör en lista med alla Audio Processer med Unika Namn
			gör en blacklist med processer, tex  "0 - @%SystemRoot%\System32\AudioSrv.Dll,-202"
		



	Jag har haft lite svårigheter när det kommer till att läsa in X bittar från serial samtidigt
	så lösningen blev att skicka siffror istället för strängar med info, får kollar på en ordentlig lösning


	Input from Arduino
	1	Button
	2	UP
	3	DOWN
	4	RIGHT
	5	LEFT

"""
print("\n------ MySoundDevice V0.1 ------\n")

try:
	ARDUINO_SERIAL = serial.Serial('COM3', 115200, timeout=0)
	print("SERIAL PORT FOUND")
except:
	print("ERROR NO SERIAL PORT FOUND\n")
	exit()


X_VAL = 0
Y_VAL = 0
BUTTON_PRESSES = 0

def NewValue():
	print("\nY-Value:  "+str(Y_VAL))
	print("X-Value:  "+str(X_VAL))
	print("Button:  "+str(BUTTON_PRESSES))

def JoystickInput(nr):
	# Button) Select Master Volume
	if nr == "1":
		BUTTON_PRESSES += 1		

	# Up) Increase Volume
	if nr == "2":
		Y_VAL += 1

	# Down) Decrease Volume
	if nr == "3":
		Y_VAL -= 1

	# Right) Change Audio Process
	if nr == "4":
		X_VAL += 1

	# Left) Change Audio Process
	if nr == "5":
		X_VAL -=1

	NewValue()


while True:
		if ARDUINO_SERIAL.in_waiting:
			SERIAL_INPUT = str((ARDUINO_SERIAL.readline()).rstrip(), "utf-8")

			if SERIAL_INPUT.isdigit():
				JoystickInput(SERIAL_INPUT)
			
			
			
