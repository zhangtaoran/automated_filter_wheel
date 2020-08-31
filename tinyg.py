import sys
# !conda install --yes --prefix {sys.prefix} pyserial
import serial
import time
import json
# !{sys.executable} -m pip install opencv-python
import cv2


class tinyg(object):
  def __init__(self):
    self._response = ""
    self._rest = {}   # in this dictionary we store the RESTfull state of the tinyg.

  def open(self, p):
    try:
      self.ser = serial.Serial(port=p, baudrate=115200, timeout=0, xonxoff=False)
    except:
	    print("Error opening serial port ", p)
	    sys.exit()
    self.handle_response()
    self.ser.write(str.encode('{"fv":""\n'))
    time.sleep(0.1)
    self.handle_response()

  def close(self):
      sys.exit()

  def move_x(self, x, speed = 200):
    gcode = "G01 X "+str(x)+ "F"+str(speed)
    self.send_gcode(gcode)

  def move_y(self, y, speed = 200):
    gcode = "G01 Y "+str(y)+ "F"+str(speed)
    self.send_gcode(gcode)

  def move_z(self, z, speed = 200):
    gcode = "G01 Z "+str(z)+ "F"+str(speed)
    self.send_gcode(gcode)

  def check_status(self) :
    status = None
    if "sr" in self._rest:
      sr = self._rest["sr"]
      if "stat" in sr:
        status = sr["stat"]
    return status

  def send_gcode(self,gcode):
    print ("sending gcode", gcode)
    self.ser.write( str.encode('{"gc":"' + gcode + '"}\n') )
    print ("waiting for status ok...")
    while 1:
     time.sleep(0.1)
     self.handle_response()  # ignore the return value
     if self.check_status() == 3:
        break
    print ("status ok")
    cap = cv2.VideoCapture(2)
    ret, frame = cap.read()
#     cv2.imshow('frame',frame)
    cv2.imwrite(str(int(time.time()))+".jpg",frame)
#     cap.release()
#     cv2.destroyAllWindows()
  
  def handle_response(self):
    j = {}
    while self.ser.inWaiting() :
      c = self.ser.read()
      c = c.decode("utf-8")
      if( c == '\n' ) :
        print ("received a line", self._response)
        try:
          j = json.loads(self._response)
          # now merge the current response with the REST dictionary
          self._rest = dict(self._rest, **j)
        except:
          print ("error in json. ignoring line:", self._response)
        self._response = ""
      else:
         self._response += c; # append the character  
    return j

  def move_to_filter(self,num): # num is a integer between 0 to 43, 44 is the same filter as 0
    x = 360*(num/44)
    return self.move_x(x,800)

  def cycle_44_filters(self):
    for i in range(44):
        self.move_to_filter(i+1)

if __name__ == "__main__":
  print("tinyg.py is running as main")
  print("connecting to ttyUSB0")
  tg = tinyg()
  tg.open("/dev/ttyUSB0")
#   tg.move_to_filter(0)
  tg.cycle_44_filters()