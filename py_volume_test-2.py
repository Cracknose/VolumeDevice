from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume
import time

print("\n+++ Fluffernutters AudioDevice0.1 +++")

PROCESS_LIST = []
PROCESS_BLACKLIST = ['@%SystemRoot%\System32\AudioSrv.Dll,-202']
DEBUG = 1

def MyDebug(msg):
	if DEBUG == 1:
		print("Debug:  ", msg)

def UpdateProcesses():
	TEMP_PROCESS_LIST = []
	sessions = AudioUtilities.GetAllSessions()	

	# GET
	for session in sessions :
		MyDebug("GET -  ", session.DisplayName)		
		# If a AudioProcess isent in PROCESS_LIST add it
		if (session.DisplayName not in TEMP_PROCESS_LIST) and (session.DisplayName not in PROCESS_BLACKLIST):
			TEMP_PROCESS_LIST.append(session.DisplayName)
			MyDebug("'", (session.DisplayName, "'  Added to TEMP_PROCESS_LIST")
		# If a AudioProcess in LIST dosent exist anymore, delete it

	# UPDATE
	for PROCESS in TEMP_PROCESS_LIST:
		if session.DisplayName not in PROCESS_LIST:
			PROCESS_LIST.append(session.DisplayName)
			MyDebug("'", session.DisplayName, "'  Added to PROCESS_LIST")

	# REMOVE
	for PROCESS in PROCESS_LIST:
		MyDebug("REM -  ", session.DisplayName)	
		if PROCESS not in TEMP_PROCESS_LIST:
			PROCESS_LIST.remove(PROCESS)
			MyDebug("'",PROCESS, "'  Removed from PROCESS_LIST")

def GetProcessVolume(session?):
	pass







UpdateProcesses()
print("\nFirst Run Done")
print("Proclist: " +str(PROCESS_LIST))
print("Sleeping for 10s, Shutdown test process")
time.sleep(10)
print("Running seccond attempt")
UpdateProcesses()
print("Proclist: " +str(PROCESS_LIST))

