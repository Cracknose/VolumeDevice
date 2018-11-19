"""
	Windows Volym test i Python
	
	res:
		https://linustechtips.com/main/topic/919310-setting-volume-using-python/
"""
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
#ovanstående används för att ändra MasterVolumeLevel
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume, IAudioEndpointVolume

def ConvertVolume(vol):
	vol *= 100
	vol = round(vol, 2)
	vol = str(vol)
	if (len(vol) == 5) and (vol != "100.0"):
		vol = vol[:-3]
	else:
		vol = vol[:-2]
	print(vol)
	#return(vol)


def GetProcesses():
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		print("Process:  "+str(session.Process))

def DisplayProcess():
	"""
	{DisplayName, GroupingParam, IconPath, Identifier, InstanceIdentifier, Process,	ProcessId, SimpleAudioVolume, State}
	"""

	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		#print(str(session.ProcessId) +" - "+ str(session.DisplayName) +" - "+ str(session.SimpleAudioVolume))
		volume = session.SimpleAudioVolume
		volumelevel = volume.GetMasterVolume()	# ==  0.2631579041481018  Baserat på vad Max Volym är   (max var 50%  och firefox 10%)
		print(session.ProcessId, " - ", session.DisplayName, " - ", volumelevel)

def MuteVolume():
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session.SimpleAudioVolume   	# <POINTER(ISimpleAudioVolume) ptr=0x55ea3bec70 at 55eababac8>
		print(str(volume))
		volume.SetMute(1, None)

def UnMuteVolume():
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session.SimpleAudioVolume		# <POINTER(ISimpleAudioVolume) ptr=0x55ea3bec70 at 55eababac8>
		print(str(volume))
		volume.SetMute(0, None)	

def GetVolume():
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		volume = session.SimpleAudioVolume
		processVolume = session.SimpleAudioVolume.GetMasterVolume()		# output   0.7857142686843872
		# OMVANLDA tex:  0.3 Till 30
		# processVolume = round(processVolume, 2)
		# processVolume = processVolume * 100								# output   0.78
		# print(str(session.ProcessId) +" - "+ str(session.DisplayName) +" - "+ str(processVolume))
		# print(processVolume)
		print("Process Volume: ")
		ConvertVolume(processVolume)


def Identification():
	sessions = AudioUtilities.GetAllSessions()
	i = 0
	for session in sessions:

		help(session)


def ChangeFirefox(number):
	# Kan än så länge bara maxa vad Master volume är, Processvolume är procentuell av master volume
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		if session.DisplayName == "Mozilla Firefox":
			volume = session.SimpleAudioVolume
			session.SimpleAudioVolume.SetMasterVolume(number, None)

def GetMasterVolumeLevel():
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))
	# MasterVolume = str(volume.GetMasterVolumeLevelScalar())
	MasterVolume = volume.GetMasterVolumeLevelScalar()
	TEST_VOLUME = MasterVolume
	# MasterVolume = str(volume.GetMasterVolumeLevel()
	# MasterVolume = MasterVolume[:5]		# [:5] chars för att första är -
	
	MasterVolume = MasterVolume * 100
	MasterVolume = round(MasterVolume, 0)
	print("MASTER VOLUME:\n")
	ConvertVolume(TEST_VOLUME)


def SetMasterVolume(nr):
	# Använder Decibel i negativ scala
	"""
	 nr		 Percent
	 0 		 == 100%
	-4.30  	 == 75%
	-10.3 	 == 50%
	-20.4	 == 25
	-65.2	 == 0%
	"""
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(
  	IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))
	
	# Control volume
	volume.SetMasterVolumeLevel(nr, None)

def SetMasterVolumeScalar(nr):
	# Använder ljud nivå 0 - 1.0
	
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(
  	IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))
	
	# Control volume
	volume.SetMasterVolumeLevelScalar(nr, None)
	
	



def main():
	print("\nPycaw Functions:")
	print("Master: ")
	GetMasterVolumeLevel()
	print("")
	GetVolume()
	


	





if __name__ == "__main__":
	main()