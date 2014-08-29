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

import socket

#address = ('localhost', 5060)
address = ('0.0.0.0', 4028)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "server will bind"
s.bind(address)
print "server will listen"
s.listen(5)

ss, addr = s.accept()
print 'got connected from',addr

ss.send('byebye')
ra = ss.recv(512)
print ra

ss.close()
s.close()
