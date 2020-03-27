# **DogRobot with RaspberryPi**

## **AUTHOR**

* Manel Lurbe Sempere (malursem@inf.upv.es)

## **ABSTRACT**

<p align=justify>

</p>

## **PROGRAMS AVAILABLE ON THIS PROJECT**



## **DOCUMENTATION AND SET UP**

### **LEGS CHANNELS**

- peu_davanter_dret = kit.servo[0]

- peu_davanter_esquerre = kit.servo[1]

- genoll_davanter_esquerre = kit.servo[2]

- genoll_davanter_dret = kit.servo[3]

- cama_davantera_esquerra = kit.servo[4]

- cama_posterior_dreta = kit.servo[5]

- cama_posterior_esquerra = kit.servo[6]

- cama_davantera_dreta = kit.servo[7]

- cola = kit.servo[8]

- coll = kit.servo[9]

- cara = kit.servo[10]

- nada = kit.servo[11]# No hay nada

- peu_posterior_dret = kit.servo[12]

- genoll_posterior_esquerre = kit.servo[13]

- peu_posterior_esquerre = kit.servo[14]

- genoll_posterior_dret = kit.servo[15]

### **Initial servo values**

- [peu_davanter_dret,60]
- [genoll_davanter_dret,130]
- [cama_davantera_dreta,40]

**cama2**

- [peu_davanter_esquerre,60]
- [genoll_davanter_esquerre,25]
- [cama_davantera_esquerra,160]

**cama3**

- [peu_posterior_dret,130]
- [genoll_posterior_dret,160]
- [cama_posterior_dreta,160])

**cama4**
- [peu_posterior_esquerre,85]
- [genoll_posterior_esquerre,150]
- [cama_posterior_esquerra,150])


### **SOFTWARE REQUISITES**

- Install python3 for develop (Ubuntu/Debian based systems):

    ```sudo apt install python3-dev python3-pip python3-tk build-essential libi2c-dev i2c-tools libffi-dev```

- Install libs for python 3:

    ```sudo -H python3 -m pip install adafruit-circuitpython-busdevice adafruit-circuitpython-servokit adafruit-circuitpython-pca9685 PCA9685-driver RPi.GPIO```

### **HARDWARE REQUISITES**

### **SET UP HARDWARE CONNECTIONS**


### **HOW TO USE**

- Set execution permissions:

    ```chmod +x program.py```

- Usage:

     ```python3 program.py music_sheets/music_sheet.txt```

     or:

    ```./program.py music_sheets/music_sheet.txt```

**NOTE: Replace "program" with the name of the program you want to execute and "music_sheet" with the name of the song you want to play from the folder "music_sheets".**

- ONLY IN *pianoPlayPi.pay* FOR DUAL HAND EMULATION WITH THREADS:

     ```python3 pianoPlayPi.py music_sheets/music_sheet_hand_1.txt music_sheets/music_sheet_hand_2.txt```

     or:

    ```./pianoPlayPi.py music_sheets/music_sheet_hand_1.txt music_sheets/music_sheet_hand_2.txt```

**NOTE: Music sheets for dual hand simulated piano, as in real life, shouldn't contains the same notes (or piano keys) at the same time, there is no reason to play with two hands the same notes.**