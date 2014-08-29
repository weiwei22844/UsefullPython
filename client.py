#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      Lenovo
#
# Created:     25/12/2013
# Copyright:   (c) Lenovo 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# client

import socket

address = ('192.168.1.102', 5060)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)

data = s.recv(512)
print 'the data received is',data

s.send('hihi')

s.close()
