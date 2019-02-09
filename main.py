
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

ZAP_RANGE = 520.0;

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

while True:
  data_1, addr = sock_1.recvfrom(1024) # buffer size is 1024 bytes
  data_2, addr = sock_2.recvfrom(1024)  # buffer size is 1024 bytes
  data_3, addr = sock_3.recvfrom(1024)  # buffer size is 1024 bytes
  data_4, addr = sock_4.recvfrom(1024)  # buffer size is 1024 bytes
  data_5, addr = sock_5.recvfrom(1024)  # buffer size is 1024 bytes
  print "received message:", data_1
  print "received message:", data_2
  print "received message:", data_3
  print "received message:", data_4
  print "received message:", data_5

  data_1_split = data_1.split(" ")
  data_2_split = data_2.split(" ")
  data_3_split = data_3.split(" ")
  data_4_split = data_4.split(" ")
  data_5_split = data_5.split(" ")

  if (data_1_split[0] == "TRACK" and float(data_1_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_1_split[1]
      sock_1.sendto("FIRE " + "1 " + data_1_split[1], (UDP_IP, SIMULATOR_UDP_PORT))

  if (data_2_split[0] == "TRACK"and float(data_2_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_2_split[1]
      sock_2.sendto("FIRE " + "2 " + data_2_split[1], (UDP_IP, SIMULATOR_UDP_PORT))

  if (data_3_split[0] == "TRACK" and float(data_3_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_3_split[1]
      sock_3.sendto("FIRE " + "3 " + data_3_split[1], (UDP_IP, SIMULATOR_UDP_PORT))

  if (data_4_split[0] == "TRACK" and float(data_4_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_4_split[1]
      sock_4.sendto("FIRE " + "4 " + data_4_split[1], (UDP_IP, SIMULATOR_UDP_PORT))

  if (data_5_split[0] == "TRACK" and float(data_5_split[3]) < ZAP_RANGE):
      print "Target Acquired: Missile No:" + data_5_split[1]
      sock_5.sendto("FIRE " + "5 " + data_5_split[1], (UDP_IP, SIMULATOR_UDP_PORT))

