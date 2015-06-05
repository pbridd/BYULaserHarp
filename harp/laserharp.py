import RPi.GPIO as GPIO
import pygame 

pygame.mixer.init()
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#initialize variables
snd1 = pygame.mixer.Sound("snd/c1.wav")
snd2 = pygame.mixer.Sound("snd/d.wav")
snd3 = pygame.mixer.Sound("snd/e.wav")
snd4 = pygame.mixer.Sound("snd/f1.wav")
snd5 = pygame.mixer.Sound("snd/g1.wav")
snd6 = pygame.mixer.Sound("snd/a.wav")
snd7 = pygame.mixer.Sound("snd/b.wav")
snd8 = pygame.mixer.Sound("snd/c2.wav")


def harp_callback_1(channel):
	print "falling edge detected on 17"
	pygame.mixer.Channel(0).play(snd1,0,0,0)

def harp_callback_2(channel):
	print "falling edge detected on 27"
	pygame.mixer.Channel(1).play(snd2,0,0,0)

def harp_callback_3(channel):
	print "falling edge detected on 22"
	pygame.mixer.Channel(2).play(snd3,0,0,0)

def harp_callback_4(channel):
	print "falling edge detected on 5"
	pygame.mixer.Channel(3).play(snd4,0,0,0)

def harp_callback_5(channel):
	print "falling edge detected on 6"
	pygame.mixer.Channel(4).play(snd5,0,0,0)

def harp_callback_6(channel):
	print "falling edge detected on 13"
	pygame.mixer.Channel(5).play(snd6,0,0,0)

def harp_callback_7(channel):
	print "falling edge detected on 26"
	pygame.mixer.Channel(6).play(snd7,0,0,0)

def harp_callback_8(channel):
	print "falling edge detected on 23"
	pygame.mixer.Channel(7).play(snd8,0,0,0)

def harp_callback_9(channel):
	print "falling edge detected on 24"

def harp_callback_10(channel):
	print "falling edge detected on 25"

def harp_callback_11(channel):
	print "falling edge detected on 12"

def harp_callback_12(channel):
	print "falling edge detected on 16"

GPIO.add_event_detect(17, GPIO.FALLING, callback=harp_callback_1, bouncetime=200)
GPIO.add_event_detect(27, GPIO.FALLING, callback=harp_callback_2, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=harp_callback_3, bouncetime=200)
GPIO.add_event_detect(5, GPIO.FALLING, callback=harp_callback_4, bouncetime=200)
GPIO.add_event_detect(6, GPIO.FALLING, callback=harp_callback_5, bouncetime=200)
GPIO.add_event_detect(13, GPIO.FALLING, callback=harp_callback_6, bouncetime=200)
GPIO.add_event_detect(26, GPIO.FALLING, callback=harp_callback_7, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=harp_callback_8, bouncetime=200)
GPIO.add_event_detect(24, GPIO.FALLING, callback=harp_callback_9, bouncetime=200)
GPIO.add_event_detect(25, GPIO.FALLING, callback=harp_callback_10, bouncetime=200)
GPIO.add_event_detect(12, GPIO.FALLING, callback=harp_callback_11, bouncetime=200)
GPIO.add_event_detect(16, GPIO.FALLING, callback=harp_callback_12, bouncetime=200)

while True:
	pass

