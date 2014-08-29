#!/usr/bin/python
import select
import socket
import time
import struct
import binascii
host = ''
#port = 12345
port = 6667

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.bind((host,port))

inputs = [sock]

#sockets from which we expect to write
outputs = []

packStruct = struct.Struct('II32s32s128siii')
values = (0xf05a5a41, 0, '', '', '', 11, 0, 0)
#A optional parameter for select is TIMEOUT
timeout = 10
desc = ('<broadcast>',6667)
#desc = ('192.168.1.83',6667)
packed_data = packStruct.pack(*values)
#print packed_data
'''
unpacked_data = packStruct.unpack(packed_data)
print unpacked_data
print 'Packed Value :', binascii.hexlify(packed_data)
'''
#packed_data = packStruct.pack(*values)
#print packed_data
#print "broadcast search data len %d"%(len(packed_data))
#sock.sendto(packed_data,desc)
count = 0
while inputs:
    
    desc = ('<broadcast>',6667)
    packed_data = packStruct.pack(*values)
    sock.sendto(packed_data,desc)
    print "broadcast search data len %d to <broadcast>"%(len(packed_data))
    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)
    if not (readable or writable or exceptional) :
        print "Time out will break2!"
        #break
    #print "packStruct size: %d"%packStruct.size
    for s in readable:
        data,addr = s.recvfrom(512)
        #print "receive from", addr, ":", data,"\n"
        #print "data len: %d"%(len(data))
        #print type(data)
        if (packStruct.size == len(data)):
            #print binascii.hexlify(data)
            packed_data = packStruct.unpack(data)
            #print packed_data
            #print packed_data[2].strip('\x00')
            if packed_data[1] == 1:
                print "find dev %s %s %s"%(packed_data[2].strip('\x00'), packed_data[3].strip('\x00'), packed_data[4].strip('\x00'))
                #count+=1
    
    print "will sleep 10s"
    time.sleep(10)
    desc = ('192.168.255.255',6667)
    packed_data2 = packStruct.pack(*values)
    sock.sendto(packed_data2,desc)
    print "broadcast search data len %d to 192.168.255.255"%(len(packed_data2))
    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)
    if not (readable or writable or exceptional) :
        print "Time out will break2!"
        #break
    #print "packStruct size: %d"%packStruct.size
    for s in readable:
        data,addr = s.recvfrom(512)
        #print "receive from", addr, ":", data,"\n"
        #print "data len: %d"%(len(data))
        #print type(data)
        if (packStruct.size == len(data)):
            #print binascii.hexlify(data)
            packed_data = packStruct.unpack(data)
            #print packed_data
            #print packed_data[2].strip('\x00')
            if packed_data[1] == 1:
                print "find dev %s %s %s"%(packed_data[2].strip('\x00'), packed_data[3].strip('\x00'), packed_data[4].strip('\x00'))
    
print "%d devs found"%count



