
#
# Network and check code
#
import socket
import sys
import time

verbose = 0;

def send_message (sock,message):
    if(verbose==2):
       print "sending "+message
    sock.sendall(message)
    # time.sleep(1)
    
   
def recv_message (sock,):

    # Look for the response
    data = sock.recv(200)
    amount_received = len(data)
    if(verbose==2):
       print "recd "+data
    return data 

def check(sock,expected,received):
    if(verbose==2):
       print "checking expected="+str(expected)+" recv="+received
    if(expected != received) :
       print "ERROR: Expected="+str(expected)+"!="+str(received)
       error = 1


