
import socket

UDP_IP = "127.0.0.1"

SIMULATOR_UDP_PORT = 8120

UDP_PORT_1 = 8121
UDP_PORT_2 = 8122
UDP_PORT_3 = 8123
UDP_PORT_4 = 8124
UDP_PORT_5 = 8125

CONNECT_1 = "CONNECT 1"
CONNECT_2 = "CONNECT 2"
CONNECT_3 = "CONNECT 3"
CONNECT_4 = "CONNECT 4"
CONNECT_5 = "CONNECT 5"

ZAP_RANGE = 740.0

print "UDP target IP:", UDP_IP
print "UDP SIMULATOR target port:", SIMULATOR_UDP_PORT

sock_1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_3 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_4 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock_5 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock_1.bind((UDP_IP, UDP_PORT_1))
sock_2.bind((UDP_IP, UDP_PORT_2))
sock_3.bind((UDP_IP, UDP_PORT_3))
sock_4.bind((UDP_IP, UDP_PORT_4))
sock_5.bind((UDP_IP, UDP_PORT_5))

sock_1.sendto(CONNECT_1,(UDP_IP,SIMULATOR_UDP_PORT))
sock_2.sendto(CONNECT_2,(UDP_IP,SIMULATOR_UDP_PORT))
sock_3.sendto(CONNECT_3,(UDP_IP,SIMULATOR_UDP_PORT))
sock_4.sendto(CONNECT_4,(UDP_IP,SIMULATOR_UDP_PORT))
sock_5.sendto(CONNECT_5,(UDP_IP,SIMULATOR_UDP_PORT))

def spaceDroneLocations():
    #####Assumes Drone 4 dies, as it always does in the simulation####
  print "Spacing Drones out"
  sock_1.sendto("MOVE " + "1 " + str(0), (UDP_IP, SIMULATOR_UDP_PORT))
  sock_2.sendto("MOVE " + "2 " + str(90), (UDP_IP, SIMULATOR_UDP_PORT))
  sock_3.sendto("MOVE " + "3 " + str(180), (UDP_IP, SIMULATOR_UDP_PORT))
  sock_5.sendto("MOVE " + "5 " + str(270), (UDP_IP, SIMULATOR_UDP_PORT))


while True:

  data_1, addr = sock_1.recvfrom(1024) # buffer size is 1024 bytes
  data_2, addr = sock_2.recvfrom(1024)  # buffer size is 1024 bytes
  data_3, addr = sock_3.recvfrom(1024)  # buffer size is 1024 bytes
  data_4, addr = sock_4.recvfrom(1024)  # buffer size is 1024 bytes
  data_5, addr = sock_5.recvfrom(1024)  # buffer size is 1024 bytes
  print "received message_1:", data_1
  print "received message_2:", data_2
  print "received message_3:", data_3
  print "received message_4:", data_4
  print "received message_5:", data_5

  data_1_split = data_1.split(" ")
  data_2_split = data_2.split(" ")
  data_3_split = data_3.split(" ")
  data_4_split = data_4.split(" ")
  data_5_split = data_5.split(" ")

  if (data_1_split[0] == "DRONE_STATE"):
      DRONE_STATE_ID_1      = data_1_split[1]
      DRONE_STATE_ANGLE_1   = data_1_split[2]
      DRONE_STATE_ALIVE_1   = data_1_split[3]

      if DRONE_STATE_ALIVE_1 == "DISABLED":
          print "***DRONE 1 DISABLED***"
          spaceDroneLocations()

  if (data_2_split[0] == "DRONE_STATE"):
      DRONE_STATE_ID_2      = data_2_split[1]
      DRONE_STATE_ANGLE_2   = data_2_split[2]
      DRONE_STATE_ALIVE_2   = data_2_split[3]

      if DRONE_STATE_ALIVE_2 == "DISABLED":
          print "***DRONE 2 DISABLED***"
          spaceDroneLocations()

  if (data_3_split[0] == "DRONE_STATE"):
      DRONE_STATE_ID_3      = data_3_split[1]
      DRONE_STATE_ANGLE_3   = data_3_split[2]
      DRONE_STATE_ALIVE_3   = data_3_split[3]

      if DRONE_STATE_ALIVE_3 == "DISABLED":
          print "***DRONE 3 DISABLED***"
          spaceDroneLocations()

  if (data_4_split[0] == "DRONE_STATE"):
      DRONE_STATE_ID_4      = data_4_split[1]
      DRONE_STATE_ANGLE_4   = data_4_split[2]
      DRONE_STATE_ALIVE_4   = data_4_split[3]

      if DRONE_STATE_ALIVE_4 == "DISABLED":
          print "***DRONE 4 DISABLED***"
          spaceDroneLocations()

  if (data_5_split[0] == "DRONE_STATE"):
      DRONE_STATE_ID_5      = data_5_split[1]
      DRONE_STATE_ANGLE_5   = data_5_split[2]
      DRONE_STATE_ALIVE_5   = data_5_split[3]

      if DRONE_STATE_ALIVE_5 == "DISABLED":
          print "***DRONE 5 DISABLED***"
          spaceDroneLocations()



  if (data_1_split[0] == "TRACK"):
      TRACK_ID_1          = data_1_split[1]
      TRACK_ANGLE_1       = data_1_split[2]
      TRACK_DISTANCE_1    = data_1_split[3]
      TRACK_SPEED_1       = data_1_split[4]
      TRACK_HEALTH_1      = data_1_split[5]


  if (data_2_split[0] == "TRACK"):
      TRACK_ID_2          = data_2_split[1]
      TRACK_ANGLE_2       = data_2_split[2]
      TRACK_DISTANCE_2    = data_2_split[3]
      TRACK_SPEED_2       = data_2_split[4]
      TRACK_HEALTH_2      = data_2_split[5]

  if (data_3_split[0] == "TRACK"):
      TRACK_ID_3          = data_3_split[1]
      TRACK_ANGLE_3       = data_3_split[2]
      TRACK_DISTANCE_3    = data_3_split[3]
      TRACK_SPEED_3       = data_3_split[4]
      TRACK_HEALTH_3      = data_3_split[5]


  if (data_4_split[0] == "TRACK"):
      TRACK_ID_4          = data_4_split[1]
      TRACK_ANGLE_4       = data_4_split[2]
      TRACK_DISTANCE_4    = data_4_split[3]
      TRACK_SPEED_4       = data_4_split[4]
      TRACK_HEALTH_4      = data_4_split[5]


  if (data_5_split[0] == "TRACK"):
      TRACK_ID_5          = data_5_split[1]
      TRACK_ANGLE_5       = data_5_split[2]
      TRACK_DISTANCE_5    = data_5_split[3]
      TRACK_SPEED_5       = data_5_split[4]
      TRACK_HEALTH_5      = data_5_split[5]


  if (data_1_split[0] == "TRACK" and float(data_1_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_1_split[1]
      sock_1.sendto("FIRE " + "1 " + TRACK_ID_1, (UDP_IP, SIMULATOR_UDP_PORT))


  if (data_2_split[0] == "TRACK"and float(data_2_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_2_split[1]
      sock_2.sendto("FIRE " + "2 " + TRACK_ID_2, (UDP_IP, SIMULATOR_UDP_PORT))


  if (data_3_split[0] == "TRACK" and float(data_3_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_3_split[1]
      sock_3.sendto("FIRE " + "3 " + TRACK_ID_3, (UDP_IP, SIMULATOR_UDP_PORT))


  if (data_4_split[0] == "TRACK" and float(data_4_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_4_split[1]
      sock_4.sendto("FIRE " + "4 " + TRACK_ID_4, (UDP_IP, SIMULATOR_UDP_PORT))


  if (data_5_split[0] == "TRACK" and float(data_5_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_5_split[1]
      sock_5.sendto("FIRE " + "5 " + TRACK_ID_5, (UDP_IP, SIMULATOR_UDP_PORT))



