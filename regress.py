#!/usr/bin/python 
import socket
import sys
import time
from ts2000 import AG_TEST
from ts2000 import FA_TEST
from ts2000 import BD_TEST
from ts2000 import BU_TEST
from ts2000 import CN_TEST
from ts2000 import CT_TEST
from ts2000 import FB_TEST
from ts2000 import FT_TEST
from ts2000 import FW_TEST
from ts2000 import GT_TEST
from ts2000 import IF_TEST
from ts2000 import KS_TEST
from ts2000 import LK_TEST
from ts2000 import MD_TEST
from ts2000 import MG_TEST
from ts2000 import MR_TEST
from ts2000 import NB_TEST
from ts2000 import NR_TEST
from ts2000 import NT_TEST
from ts2000 import PA_TEST
from ts2000 import PC_TEST
from ts2000 import RA_TEST
from ts2000 import RC_TEST
from ts2000 import RD_TEST
from ts2000 import RG_TEST
from ts2000 import RT_TEST
from ts2000 import RU_TEST
from ts2000 import SD_TEST
from ts2000 import SQ_TEST
from ts2000 import ST_TEST
from ts2000 import TY_TEST
from ts2000 import VD_TEST
from ts2000 import VG_TEST
from ts2000 import VX_TEST

error = 0
verbose = 1

   
# Define test locations here
RIGCTL_PORT = 19090
RIGCTL_IP_ADDR = 'localhost'
RIGCTL_PROPS = '00-04-A3-D3-A9-60.props'


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (RIGCTL_IP_ADDR, RIGCTL_PORT)

print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Tests with double hashes below have issues with the command
# in rigctl.c or aren't debugged yet.
AG_TEST(sock)
FA_TEST(sock)
BD_TEST(sock)
BU_TEST(sock)
CN_TEST(sock)
CT_TEST(sock)
FB_TEST(sock)
###FT_TEST(sock)
FW_TEST(sock)
GT_TEST(sock)
IF_TEST(sock)
KS_TEST(sock)
LK_TEST(sock)
MD_TEST(sock)
MG_TEST(sock)
MR_TEST(sock)
NB_TEST(sock)
NR_TEST(sock)
NT_TEST(sock)
PA_TEST(sock)
PC_TEST(sock)
RA_TEST(sock)
RC_TEST(sock)
RD_TEST(sock) 
RG_TEST(sock)
RT_TEST(sock)
RU_TEST(sock)
SD_TEST(sock)
#SQ_TEST(sock)
ST_TEST(sock)
TY_TEST(sock)
VD_TEST(sock)
VG_TEST(sock)
VX_TEST(sock)
