#!/usr/bin/python
import select
import socket
import time
import struct
import binascii
host = ''
#port = 12345
port = 6667
'''
UDP_PACK* pPack = (UDP_PACK*)chSendBuf;
pPack->magic = PACK_MAGIC;
pPack->pack_type = 0;
pPack->nFlag=11;            // È«ÍøËÑË÷
pPack->nPackSize = sizeof(UDP_PACK);
nRet = sendto(m_BroadSock, chSendBuf, sizeof(UDP_PACK), 0, (SOCKADDR*)&addrTo, sizeof(SOCKADDR));
if(nRet <= 0)
{
    OutputDebugString("send search package failed\n");
}

#define DEVSEARCH_PORT 6667
#define PACK_MAGIC 0xf05a5a41
typedef struct UDP_PACK_ {
    unsigned int magic;     /*header of package: 0xf05a5a41*/
    unsigned int pack_type;   /*specify the type of the UDP package, 0 request, 1 answer, 2 set*/
    char IpAddr[32];
    char MacAddr[32];
    char hostname[125];
    int nFlag;
    int nRes[2];
}UDP_PACK;
'''
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
sock.bind((host,port))
print "Listen on the port 12345......"

inputs = [sock]

#sockets from which we expect to write
outputs = []

packStruct = struct.Struct('II32s32s128siii')
values = (0xf05a5a41, 0, '', '', '', 11, 0, 0)
#A optional parameter for select is TIMEOUT
timeout = 20
desc = ('<broadcast>',6667)
#desc = ('192.168.1.83',6667)
packed_data = packStruct.pack(*values)
#print packed_data
'''
unpacked_data = packStruct.unpack(packed_data)
print unpacked_data
print 'Packed Value :', binascii.hexlify(packed_data)
'''
packed_data = packStruct.pack(*values)
#print packed_data
#print "send len %d"%(len(packed_data))
#sock.sendto(packed_data,desc)
while inputs:
    readable , writable , exceptional = select.select(inputs, outputs, inputs, timeout)
    # When timeout reached , select return three empty lists
    if not (readable or writable or exceptional) :
        print "Time out will continue!"
        continue
    print "packStruct size: %d"%packStruct.size
    for s in readable:
        data,addr = s.recvfrom(512)
        #print "receive from", addr, ":", data,"\n"
        print "data len: %d"%(len(data))
        #print type(data)
        if(packStruct.size == len(data)):
            print binascii.hexlify(data)
            packed_data = packStruct.unpack(data)
            print packed_data
            print packed_data[2].strip('\x00')
    #time.sleep(5)


