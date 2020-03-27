#!/usr/bin/python3
# -*- coding: utf-8 -*-

#	Dog Bot  Copyright (C) 2020  Manel Lurbe Sempere
#	This program comes with ABSOLUTELY NO WARRANTY for details type `show w'.
#	This is free software, and you are welcome to redistribute it
#	under certain conditions type `show c' for details.

########################################
#			Imports					   #
########################################
import time
import sys
from adafruit_servokit import ServoKit
#end Imports.

########################################
#		Initialize I2C bus             #
########################################

# Create the servo connection.
kit = ServoKit(channels=16)
#end Initialize I2C bus.

########################################
#		Global variables               #
########################################

# Servo angles.
left = 0
off = 90
right = 180

# Commands
orden_avant = 1
orden_arrere = 0

#end Global variables.

########################################
#		Servos positions               #
########################################

# Channel of each servo motor.
#part posicio costat
peu_davanter_dret = kit.servo[0]
peu_davanter_esquerre = kit.servo[1]
genoll_davanter_esquerre = kit.servo[2]
genoll_davanter_dret = kit.servo[3]
ingle_davantera_esquerra = kit.servo[4]
ingle_posterior_dreta = kit.servo[5]
ingle_posterior_esquerra = kit.servo[6]
ingle_davantera_dreta = kit.servo[7]
cola = kit.servo[8]
coll = kit.servo[9]
cara = kit.servo[10]
nada = kit.servo[11]# No hay nada
peu_posterior_dret = kit.servo[12]
genoll_posterior_esquerre = kit.servo[13]
peu_posterior_esquerre = kit.servo[14]
genoll_posterior_dret = kit.servo[15]

# for mt in range(16):
# 	print(str(mt)+"\t"+str(kit.servo[mt].angle)+"\n")

# Servo motors available.
motor_list = [peu_davanter_dret,peu_davanter_esquerre,genoll_davanter_esquerre,genoll_davanter_dret,ingle_davantera_esquerra,ingle_posterior_dreta,ingle_posterior_esquerra,ingle_davantera_dreta,cola,coll,cara,nada,peu_posterior_dret,genoll_posterior_esquerre,peu_posterior_esquerre,genoll_posterior_dret]

########################################
#			pierna class               #
########################################
class pierna():
	peu = nada
	genoll = nada
	ingle = nada
	peu_pos1 = off
	peu_pos2 = off
	ingle_pos1 = off
	ingle_pos2 = off
	genoll_pos1 = off
	genoll_pos2 = off
	def __init__(self,peu,genoll,ingle):
		self.peu = peu[0]
		self.genoll = genoll[0]
		self.ingle = ingle[0]
		self.peu_pos1 = peu[1]
		self.genoll_pos1 = genoll[1]
		self.ingle_pos1 = ingle[1]
		self.peu_pos2 = peu[2]
		self.genoll_pos2 = genoll[2]
		self.ingle_pos2 = ingle[2]
		#self.reset()
	def reset(self):
		self.avant()
	def avant(self):
		self.ingle.angle = self.ingle_pos1
		self.genoll.angle = self.genoll_pos1
		self.peu.angle = self.peu_pos1
		#self.ingle.angle = self.ingle_val+20
	def arrere(self):
		self.ingle.angle = self.ingle_pos2
		self.genoll.angle = self.genoll_pos2
		self.peu.angle = self.peu_pos2
		#self.ingle.angle = self.ingle_val-20
# Initialize legs
# [Direccion, Position1, Position2]
cama_davantera_dreta = pierna([peu_davanter_dret,60,60],[genoll_davanter_dret,130,0],[ingle_davantera_dreta,40,160])
cama_davantera_esquerra = pierna([peu_davanter_esquerre,60,60],[genoll_davanter_esquerre,25,160],[ingle_davantera_esquerra,160,35])
cama_posterior_dreta = pierna([peu_posterior_dret,130,130],[genoll_posterior_dret,160,20],[ingle_posterior_dreta,160,30])
cama_posterior_esquerra = pierna([peu_posterior_esquerre,85,85],[genoll_posterior_esquerre,150,20],[ingle_posterior_esquerra,150,25])

# Legs list
cames = [cama_davantera_dreta,cama_davantera_esquerra,cama_posterior_esquerra,cama_posterior_dreta]

########################################
#			usage function             #
########################################
def usage(program_name):
	print("Usage:\n\tpython3 "+program_name+" action\nor:\n\t./"+program_name+" action")
#end usage function.

########################################
#		mover_mt function             #
########################################
def mover_mt(motor):
	mt = motor_list[motor]
	mt.angle = left
	time.sleep(0.2)
	mt.angle = right
	time.sleep(0.2)

########################################
#		mover_mt function             #
########################################
def mover_mt_angle(motor,angle):
	mt = motor_list[motor]
	mt.angle = angle
	time.sleep(0.2)
	print("movido")

########################################
#		mover_cola function             #
########################################
def mover_cola(mt):
	while True:
		mt.angle = left
		time.sleep(0.2)
		mt.angle = right
		time.sleep(0.2)
#end mover_cola function.

########################################
#		sentarse  function             #
########################################
def sentarse():
	sys.exit(1)
#end sentarse function.

########################################
#		moure_cap  function            #
########################################
def moure_cap(costat,altura):
	cara.angle = costat
	coll.agle = altura
#end moure_cap function.

########################################
#		moure_cama  function           #
########################################
def moure_cama(cama_actual,orden):
	if orden == orden_avant:
		cama_actual.avant()
	elif orden == orden_arrere:
		cama_actual.arrere()
#end moure_cama function.

########################################
#		caminar  function             #
########################################
def caminar():
	cont0 = 0
	cont1 = 0 
	while True:
		if cont1%2 == 0:
			moure_cap(left,left)
		else:
			moure_cap(off,off)
		cont0 = cont1
		for cama in cames:
			if cont0%2 == 0:
				cama.avant()
			else:
				cama.arrere()
			cont0 = cont0+1
			time.sleep(0.1)
		cont1 = cont1+1
#end caminar function.

########################################
#		caminarV2  function            #
########################################
def caminarV2():
	cont0 = 0
	cont1 = 0 
	while True:
		if cont1%2 == 0:
			moure_cap(left,left)
		else:
			moure_cap(off,off)
		cont0 = cont1
		for cama_actual in cames:# bucle te 4 elements (0,2)(1,3)
			moure_cama(cama_actual,cont0%2)
			cont0 = cont0+1
			time.sleep(0.1)
		cont1 = cont1+1
#end caminar function.

########################################
#			reset function             #
########################################
def reset():
	moure_cap(off,off)
	for cama in cames:
		cama.reset()
#end reset function.

#########################################
#    Read arguments and get partitures  #
#########################################

# Get program name.
program_name = sys.argv[0].replace("./","")

# Get number of arguments.
num_args = len(sys.argv)

# Exit program if no command are selected.
if num_args <= 1:
	print("Ninguna orden seleccionada")
	usage(program_name)
	sys.exit(1)

#Get dog command
orden = sys.argv[1]

# If partiture name is reset, reset motors and end program.
if orden == "reset":
	reset()
	print("Reset dog")
	sys.exit(1)

try:
	if orden == "cola":
		mover_cola(cola)
except KeyboardInterrupt:#Ctrl+c
	cola.angle = off
	print("El perrito deja de mover la cola")
	sys.exit(1)

if orden == "sentarse":
	sentarse()
	print("El perrito se ha sentado")
	sys.exit(1)

if orden == "motor":
	if num_args <= 3:
		print("Selecciona un motor del 0 al 15 y el angulo")
		sys.exit(1)
	mt = int(sys.argv[2])
	angle = int(sys.argv[3])
	mover_mt_angle(mt,angle)
	print("Motor movido")
	sys.exit(1)

def worker2(num_thread):	
	try:
		while True:
			reset()
			if num_thread == 0:
				caminarV2()
			if num_thread == 1:
				mover_cola(cola)
	except KeyboardInterrupt:
		if num_thread == 0:
			reset()
			print("Turning off the dog.")
		sys.exit(1)
#end function worker.

def worker(num_thread):	
	try:
		while True:
			reset()
			if num_thread == 0:
				caminar()
			if num_thread == 1:
				mover_cola(cola)
	except KeyboardInterrupt:
		if num_thread == 0:
			reset()
			print("Turning off the dog.")
		sys.exit(1)
#end function worker.

if orden == "caminar":
	try:
		import threading
		threads = list()
		print('Doggy start, press Ctrl-C to quit...')
		for i in range(2):
		    t = threading.Thread(target=worker,args=(i,))
		    threads.append(t)
		    t.start()
	except KeyboardInterrupt:
		reset()
		print("Reset dog")
		sys.exit(1)

if orden == "caminar2":
	try:
		import threading
		threads = list()
		print('Doggy start, press Ctrl-C to quit...')
		for i in range(2):
		    t = threading.Thread(target=worker2,args=(i,))
		    threads.append(t)
		    t.start()
	except KeyboardInterrupt:
		reset()
		print("Reset dog")
		sys.exit(1)