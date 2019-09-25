import time
import serial
import multiprocessing



HIGH=1
LOW=0

global int_val
int_val = 0

global grp
grp = 0


###########################
# voice command functions #
###########################

def g1204():
  #passing error block
  global grp
  global int_val
  int_val = 0


def g1empty():
  #passing error block
  global grp
  global int_val
  int_val = 0


def g1one():
  global grp
  global int_val
  global series
  #Function definition for first voice command of Group 1
  grp = 2				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0


def g1two():           
  global grp
  global int_val
  global series
  #Function definition for second voice command of Group 1
  grp = 2				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0


def g1three():
  global grp
  global int_val
  global series
  #Function definition for third voice command of Group 1
  grp = 2				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0


def g1four():
  global grp
  global int_val
  global series
  #Function definition for fourth voice command of Group 1
  grp = 2				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0


def g1five():
  global grp
  global int_val
  global series
  #Function definition for fifth voice command of Group 1
  grp = 2				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0


##################


def g2204():
  #passing error block
  global grp
  global int_val
  int_val = 0


def g2empty():
  #passing error block
  global grp
  global int_val
  int_val = 0


def g2one():
  global grp
  global int_val
  global series
  #Function definition for first voice command of Group 2
  grp = 3				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0


def g2two():
  global grp
  global int_val
  global series
  #Function definition for second voice command of Group 2
  grp = 3				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0



def g2three():
  global grp
  global int_val
  global series
  #Function definition for third voice command of Group 2
  grp = 3				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0



def g2four():
  global grp
  global int_val
  global series
  #Function definition for fourth voice command of Group 2
  grp = 3				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0



def g2five():
  global grp
  global int_val
  global series
  #Function definition for fifth voice command of Group 2
  grp = 3				#comment this line if no group change is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change is needeed
  int_val = 0



#######################


def g3204():
  #passing error block
  global grp
  global int_val
  int_val = 0


def g3empty():
  #passing error block
  global grp
  global int_val
  int_val = 0


def g3one():
  global grp
  global int_val
  global series
  #Function definition for first voice command of Group 3
  grp = 1				#comment this line if no group change (back to 1) is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change (back to 1) is needeed
  int_val = 0


def g3two():
  global grp
  global int_val
  global series
  #Function definition for second voice command of Group 3
  grp = 1				#comment this line if no group change (back to 1) is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change (back to 1) is needeed
  int_val = 0


def g3three():
  global grp
  global int_val
  global series
  #Function definition for third voice command of Group 3
  grp = 1				#comment this line if no group change (back to 1) is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change (back to 1) is needeed
  int_val = 0


def g3four():
  global grp
  global int_val
  global series
  #Function definition for fourth voice command of Group 3
  grp = 1				#comment this line if no group change (back to 1) is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change (back to 1) is needeed
  int_val = 0


def g3five():
  global grp
  global int_val
  global series
  #Function definition for fifth voice command of Group 3
  grp = 1				#comment this line if no group change (back to 1) is needeed
  series = (series * 10) + int_val - 16	#comment this line if no group change (back to 1) is needeed
  int_val = 0





# Function ot convert bytes into integer
def ByteToInt(x):
  if (x == '\xCC'):
    return 204
  elif (x == '\x11'):
    return 17
  elif (x == '\x12'):
    return 18
  elif (x == '\x13'):
    return 19
  elif (x == '\x14'):
    return 20
  elif (x == '\x15'):
    return 21
  else:
    return 0


    

############################
# Functions Start sequence #
############################


# integers mapped to voice command functions

grpone = {204:g1204, 0:g1empty, 17:g1one, 18:g1two, 19:g1three, 20:g1four, 21:g1five}
grptwo = {204:g2204, 0:g2empty, 17:g2one, 18:g2two, 19:g2three, 20:g2four, 21:g2five}
grpthree = {204:g3204, 0:g3empty, 17:g3one, 18:g3two, 19:g3three, 20:g3four, 21:g3five}



# serial settings for voice module (connect to USB0)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=0.05
)
ser.flushInput()

# run twice to make sure it's in the correct mode
for i in range(2):
  ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
  time.sleep(0.1)
  ser.write(serial.to_bytes([0x00])) # import group 1 and await voice input
  time.sleep(0.1)

for i in range(2):
  ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
  time.sleep(0.1)
  ser.write(serial.to_bytes([0x37])) # import group 1 and await voice input
  time.sleep(0.1)
print('initialisation complete')

#global grp 
grp = 1
#global int_val
int_val = 0
#global series
series = 0

while True:
    #global grp
    #global int_val  
    if grp == 1:
      for i in range(1):
        ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
        time.sleep(0.05)
        ser.write(serial.to_bytes([0x00])) # import group 1 and await voice input
        time.sleep(0.05)

      for i in range(1):
        ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
        time.sleep(0.05)
        ser.write(serial.to_bytes([0x21])) # import group 1 and await voice input
        time.sleep(0.05)
        print('Group 1 loaded')
      while int_val == 0:
         data_byte = ser.read() # read serial data (one byte)
         int_val = ByteToInt(data_byte) # convert to integer function since python 2 doesnt have inbuilt function
         #print(int_val)
         grpone[int_val]() # call voice command function
         if grp == 2:
           print(series)
           break
        #############################################################################
    if grp == 2:
      for i in range(1):
        ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
        time.sleep(0.05)
        ser.write(serial.to_bytes([0x00])) # import group 1 and await voice input
        time.sleep(0.05)

      for i in range(1):
        ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
        time.sleep(0.05)
        ser.write(serial.to_bytes([0x22])) # import group 1 and await voice input
        time.sleep(0.05)
        print('Group 2 loaded')
      while int_val == 0:
         data_byte = ser.read() # read serial data (one byte)
         int_val = ByteToInt(data_byte) # convert to integer
         #print(int_val)
         grptwo[int_val]() # call voice command function
         if grp == 3:
           print(series)
           break
    ################################################################################
    if grp == 3:
      for i in range(1):
        ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
        time.sleep(0.05)
        ser.write(serial.to_bytes([0x00])) # import group 1 and await voice input
        time.sleep(0.05)

      for i in range(1):
        ser.write(serial.to_bytes([0xAA])) # set speech module to waiting state
        time.sleep(0.05)
        ser.write(serial.to_bytes([0x23])) # import group 1 and await voice input
        time.sleep(0.05)
        print('Group 3 loaded')
      while int_val == 0:
         data_byte = ser.read() # read serial data (one byte)
         int_val = ByteToInt(data_byte) # convert to integer
         #print(int_val)
         grpthree[int_val]() # call voice command function
         if grp == 1:
           print(series)
           break
 ###################################################################################

