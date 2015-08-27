import RPi.GPIO as GPIO
import pygame 

debug = 0

pygame.mixer.init()
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(32, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#initialize variables
note_C0 = pygame.mixer.Sound("snd/39187__jobro__piano-ff-040.wav")
note_CS0 = pygame.mixer.Sound("snd/39188__jobro__piano-ff-041.wav")
note_D0 = pygame.mixer.Sound("snd/39189__jobro__piano-ff-042.wav")
note_DS0 = pygame.mixer.Sound("snd/39190__jobro__piano-ff-042.wav")
note_E0 = pygame.mixer.Sound("snd/39191__jobro__piano-ff-044.wav")
note_F0 = pygame.mixer.Sound("snd/39193__jobro__piano-ff-045.wav")
note_FS0 = pygame.mixer.Sound("snd/39194__jobro__piano-ff-046.wav")
note_G0 = pygame.mixer.Sound("snd/39195__jobro__piano-ff-047.wav")
note_A0 = pygame.mixer.Sound("snd/39197__jobro__piano-ff-049.wav")
note_B0 = pygame.mixer.Sound("snd/39199__jobro__piano-ff-051.wav")
note_C1 = pygame.mixer.Sound("snd/39200__jobro__piano-ff-052.wav")


def harp_callback_1(channel):
	if debug == 1:
		print "falling edge detected on 11"
	pygame.mixer.Channel(0).play(note_C0,0,0,0)

def harp_callback_2(channel):
	if debug == 1:
		print "falling edge detected on 13"
	pygame.mixer.Channel(1).play(note_D0,0,0,0)

def harp_callback_3(channel):
	if debug == 1:
		print "falling edge detected on 15"
	pygame.mixer.Channel(2).play(note_E0,0,0,0)

def harp_callback_4(channel):
	if debug == 1:
		print "falling edge detected on 29"
	pygame.mixer.Channel(3).play(note_F0,0,0,0)

def harp_callback_5(channel):
	if debug == 1:
		print "falling edge detected on 31"
	pygame.mixer.Channel(4).play(note_G0,0,0,0)

def harp_callback_6(channel):
	if debug == 1:
		print "falling edge detected on 33"
	pygame.mixer.Channel(5).play(note_A0,0,0,0)

def harp_callback_7(channel):
	if debug == 1:
		print "falling edge detected on 35"
	pygame.mixer.Channel(6).play(note_B0,0,0,0)

def harp_callback_8(channel):
	if debug == 1:
		print "falling edge detected on 37"
	pygame.mixer.Channel(7).play(note_C1,0,0,0)

def harp_callback_9(channel):
	if debug == 1:
		print "falling edge detected on 16"

def harp_callback_10(channel):
	if debug == 1:
		print "falling edge detected on 18"

def harp_callback_11(channel):
	if debug == 1:
		print "falling edge detected on 22"

def harp_callback_12(channel):
	if debug == 1:
		print "falling edge detected on 32"

GPIO.add_event_detect(11, GPIO.FALLING, callback=harp_callback_1, bouncetime=50)
GPIO.add_event_detect(13, GPIO.FALLING, callback=harp_callback_2, bouncetime=50)
GPIO.add_event_detect(15, GPIO.FALLING, callback=harp_callback_3, bouncetime=50)
GPIO.add_event_detect(29, GPIO.FALLING, callback=harp_callback_4, bouncetime=50)
GPIO.add_event_detect(31, GPIO.FALLING, callback=harp_callback_5, bouncetime=50)
GPIO.add_event_detect(33, GPIO.FALLING, callback=harp_callback_6, bouncetime=50)
GPIO.add_event_detect(35, GPIO.FALLING, callback=harp_callback_7, bouncetime=50)
GPIO.add_event_detect(37, GPIO.FALLING, callback=harp_callback_8, bouncetime=50)
GPIO.add_event_detect(16, GPIO.FALLING, callback=harp_callback_9, bouncetime=50)
GPIO.add_event_detect(18, GPIO.FALLING, callback=harp_callback_10, bouncetime=50)
GPIO.add_event_detect(22, GPIO.FALLING, callback=harp_callback_11, bouncetime=50)
GPIO.add_event_detect(32, GPIO.FALLING, callback=harp_callback_12, bouncetime=50)

while True:
	pass

