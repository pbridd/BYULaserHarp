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

def harp_callback_1(channel):
	print "falling edge detected on 17"
	pygame.mixer.music.load("snd/c1.wav")
	pygame.mixer.music.play()

def harp_callback_2(channel):
	print "falling edge detected on 27"

def harp_callback_3(channel):
	print "falling edge detected on 22"

def harp_callback_4(channel):
	print "falling edge detected on 5"

def harp_callback_5(channel):
	print "falling edge detected on 6"

def harp_callback_6(channel):
	print "falling edge detected on 13"

def harp_callback_7(channel):
	print "falling edge detected on 26"

def harp_callback_8(channel):
	print "falling edge detected on 23"

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

