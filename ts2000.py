from net import send_message
from net import recv_message
from net import check
import time

verbose = 0

#######################################################################
# 
# AG Test - Audio Gain Test
# AG<0/1><0-260>
#   #1 - Primary/Sub
#   #2 - Set Value range
#
#######################################################################
def AG_TEST(sock):
  print "AG Test"
  if(verbose==1):
      print "Checking AG0000"
  send_message(sock,"AG0000;"); # Set gain value to 0
  send_message(sock,"AG0;");    # Read back value
  check(sock,"AG0000;",recv_message(sock))

  if(verbose==1):
      print "Checking AG0260"
  send_message(sock,"AG0260;"); # Set gain value to 123
  send_message(sock,"AG0;"); # Set gain value to 0
  check(sock,"AG0260;",recv_message(sock))

  if(verbose==1):
      print "Checking AG>260"
  send_message(sock,"AG0261;"); # Set gain value to 0
  check(sock,"?;",recv_message(sock))
  
  if(verbose==1):
      print "Checking AG0100"
  send_message(sock,"AG0100;"); # Set gain value to 123
  send_message(sock,"AG0;"); # Set gain value to 0
  check(sock,"AG0100;",recv_message(sock))
  

#######################################################################
# 
# FA Test - Set Primary VFO and readback
#    FA<11Digits>;
#
#######################################################################
def FA_TEST(sock):
  print "FA Test"
  if(verbose==1):
      print "Checking FA000028000000;"
  send_message(sock,"FA00028000000;")
  time.sleep(0.2)
  send_message(sock,"FA;")  
  check(sock,"FA00028000000;",recv_message(sock))

#######################################################################
# 
# BD Test - Band Down
#
#######################################################################
def BD_TEST(sock):
  print "BD Test"

  if(verbose==1):
      print "BD Test: Set Frequency to 28MHz;"
  send_message(sock,"FA00028000000;")
  time.sleep(0.2)
  send_message(sock,"FA;")  
  check(sock,"FA00028000000;",recv_message(sock))

  if(verbose==1):
     print "BD Test: Step down to 24;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,24,new_val)

  if(verbose==1):
     print "BD Test: Step down to 21;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,21,new_val)
   
  if(verbose==1):
     print "BD Test: Step down to 18;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,18,new_val)
   

  if(verbose==1):
     print "BD Test: Step down to 14;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,14,new_val)
   
  
  if(verbose==1):
     print "BD Test: Step down to 10;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,10,new_val)
   
  if(verbose==1):
     print "BD Test: Step down to 7;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,7,new_val)
   
  if(verbose==1):
     print "BD Test: Step down to 5;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,5,new_val)

  if(verbose==1):
     print "BD Test: Step down to 3;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,3,new_val)
   
   
  if(verbose==1):
     print "BD Test: Step down to 1.8;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,1,new_val)
   
  if(verbose==1):
     print "BD Test: Step down wrap to 50;"
  send_message(sock,"BD;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,50,new_val)
   

#######################################################################
# 
# BU Test - Band Up
#
#######################################################################

def BU_TEST(sock):
  print "BU Test";
  if(verbose==1):
      print "BU Test: Set Frequency to 1.8MHz;"
  send_message(sock,"FA00001850000;")
  time.sleep(0.2)
  send_message(sock,"FA;")  
  check(sock,"FA00001850000;",recv_message(sock))

  if(verbose==1):
     print "BU Test: Step up to 3.5;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,3,new_val)

  if(verbose==1):
     print "BU Test: Step up to 5;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,5,new_val)
   
  if(verbose==1):
     print "BU Test: Step up to 7;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,7,new_val)
   
  if(verbose==1):
     print "BU Test: Step up to 10;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,10,new_val)
   

  if(verbose==1):
     print "BU Test: Step up to 14;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,14,new_val)
   
  
  if(verbose==1):
     print "BU Test: Step up to 18;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,18,new_val)
   
  if(verbose==1):
     print "BU Test: Step up to 21;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,21,new_val)
   
  if(verbose==1):
     print "BU Test: Step up to 24;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,24,new_val)

  if(verbose==1):
     print "BU Test: Step up to 28;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,28,new_val)
   
   
  if(verbose==1):
     print "BU Test: Step up to 50;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,50,new_val)
   
  if(verbose==1):
     print "BU Test: Wrap to 1.8;"
  send_message(sock,"BU;");
  time.sleep(0.2)
  send_message(sock,"FA;")  
  str = recv_message(sock)
  str= str.replace('FA000','')
  str = str.replace(";","")
  new_val = int(str)/1000000
  check(sock,1,new_val)
   

#######################################################################
# 
# CN Test - Sets/read CTSS Function 01-38 are legal values
#    Verify settings from 01-39
#
#######################################################################

def CN_TEST(sock):
  print "CN Test"
 
  send_message(sock,"CN01;");
  send_message(sock,"CN;");
  check(sock,"CN01;",recv_message(sock))

  send_message(sock,"CN02;");
  send_message(sock,"CN;");
  check(sock,"CN02;",recv_message(sock))
   
  send_message(sock,"CN03;");
  send_message(sock,"CN;");
  check(sock,"CN03;",recv_message(sock))

  send_message(sock,"CN04;");
  send_message(sock,"CN;");
  check(sock,"CN04;",recv_message(sock))

  send_message(sock,"CN05;");
  send_message(sock,"CN;");
  check(sock,"CN05;",recv_message(sock))

  send_message(sock,"CN06;");
  send_message(sock,"CN;");
  check(sock,"CN06;",recv_message(sock))

  send_message(sock,"CN07;");
  send_message(sock,"CN;");
  check(sock,"CN07;",recv_message(sock))

  send_message(sock,"CN08;");
  send_message(sock,"CN;");
  check(sock,"CN08;",recv_message(sock))

  send_message(sock,"CN09;");
  send_message(sock,"CN;");
  check(sock,"CN09;",recv_message(sock))
 
  send_message(sock,"CN11;");
  send_message(sock,"CN;");
  check(sock,"CN11;",recv_message(sock))

  send_message(sock,"CN12;");
  send_message(sock,"CN;");
  check(sock,"CN12;",recv_message(sock))
   
  send_message(sock,"CN13;");
  send_message(sock,"CN;");
  check(sock,"CN13;",recv_message(sock))

  send_message(sock,"CN14;");
  send_message(sock,"CN;");
  check(sock,"CN14;",recv_message(sock))

  send_message(sock,"CN15;");
  send_message(sock,"CN;");
  check(sock,"CN15;",recv_message(sock))

  send_message(sock,"CN16;");
  send_message(sock,"CN;");
  check(sock,"CN16;",recv_message(sock))

  send_message(sock,"CN17;");
  send_message(sock,"CN;");
  check(sock,"CN17;",recv_message(sock))

  send_message(sock,"CN18;");
  send_message(sock,"CN;");
  check(sock,"CN18;",recv_message(sock))

  send_message(sock,"CN19;");
  send_message(sock,"CN;");
  check(sock,"CN19;",recv_message(sock))

 
  send_message(sock,"CN21;");
  send_message(sock,"CN;");
  check(sock,"CN21;",recv_message(sock))

  send_message(sock,"CN22;");
  send_message(sock,"CN;");
  check(sock,"CN22;",recv_message(sock))
   
  send_message(sock,"CN23;");
  send_message(sock,"CN;");
  check(sock,"CN23;",recv_message(sock))

  send_message(sock,"CN24;");
  send_message(sock,"CN;");
  check(sock,"CN24;",recv_message(sock))

  send_message(sock,"CN25;");
  send_message(sock,"CN;");
  check(sock,"CN25;",recv_message(sock))

  send_message(sock,"CN26;");
  send_message(sock,"CN;");
  check(sock,"CN26;",recv_message(sock))

  send_message(sock,"CN27;");
  send_message(sock,"CN;");
  check(sock,"CN27;",recv_message(sock))

  send_message(sock,"CN28;");
  send_message(sock,"CN;");
  check(sock,"CN28;",recv_message(sock))

  send_message(sock,"CN29;");
  send_message(sock,"CN;");
  check(sock,"CN29;",recv_message(sock))

  send_message(sock,"CN31;");
  send_message(sock,"CN;");
  check(sock,"CN31;",recv_message(sock))

  send_message(sock,"CN32;");
  send_message(sock,"CN;");
  check(sock,"CN32;",recv_message(sock))
   
  send_message(sock,"CN33;");
  send_message(sock,"CN;");
  check(sock,"CN33;",recv_message(sock))

  send_message(sock,"CN34;");
  send_message(sock,"CN;");
  check(sock,"CN34;",recv_message(sock))

  send_message(sock,"CN35;");
  send_message(sock,"CN;");
  check(sock,"CN35;",recv_message(sock))

  send_message(sock,"CN36;");
  send_message(sock,"CN;");
  check(sock,"CN36;",recv_message(sock))

  send_message(sock,"CN37;");
  send_message(sock,"CN;");
  check(sock,"CN37;",recv_message(sock))

  send_message(sock,"CN38;");
  send_message(sock,"CN;");
  check(sock,"CN38;",recv_message(sock))

  send_message(sock,"CN39;");
  send_message(sock,"CN;");
  check(sock,"CN39;",recv_message(sock))


#######################################################################
# 
# CT Test - Sets/read CTSS Enable
#    Verify settings 0, 1, X
#
#######################################################################

def CT_TEST(sock):
  print "CN Test"

  if(verbose==1):
     print "CT Test: Disable CTCSS "
  send_message(sock,"CT0;");
  send_message(sock,"CT;");
  check(sock,"CT0;",recv_message(sock))

  if(verbose==1):
     print "CT Test: Enable CTCSS "
  send_message(sock,"CT1;");
  send_message(sock,"CT;");
  check(sock,"CT1;",recv_message(sock))

  if(verbose==1):
     print "CT Test: Illegal value"
  send_message(sock,"CT2;");
  check(sock,"?;",recv_message(sock))

#######################################################################
# 
# FB Test - Sets/read VFOB
#    Verify settings 0, 1, X
#
#######################################################################

def FB_TEST(sock):
  print "FB Test"
  if(verbose==1):
      print "Checking FB000028000000;"
  send_message(sock,"FB00028000000;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00028000000;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000024000000;"
  send_message(sock,"FB00024000000;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00024000000;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014000000;"
  send_message(sock,"FB00014000000;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014000000;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014000001;"
  send_message(sock,"FB00014000001;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014000001;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014000010;"
  send_message(sock,"FB00014000010;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014000010;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014000200;"
  send_message(sock,"FB00014000200;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014000200;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014008000;"
  send_message(sock,"FB00014008000;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014008000;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014010000;"
  send_message(sock,"FB00014010000;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014010000;",recv_message(sock))

  if(verbose==1):
      print "Checking FB000014200000;"
  send_message(sock,"FB00014200000;")
  time.sleep(0.2)
  send_message(sock,"FB;")  
  check(sock,"FB00014200000;",recv_message(sock))

#######################################################################
# 
# FS Test - Sets/read Fine state 0,1,x
#
#######################################################################

  print "FS Test"
  send_message(sock,"FS0;")
  send_message(sock,"FS;")  
  check(sock,"FS0;",recv_message(sock))
  send_message(sock,"FS1;")
  send_message(sock,"FS;")  
  check(sock,"FS1;",recv_message(sock))
  send_message(sock,"FS2;")
  check(sock,"?;",recv_message(sock))


#######################################################################
# 
# FT Test - Sets/read active transmitter
#    Verify settings 0, 1, X
#    Not debugged???
#
#######################################################################

def FT_TEST(sock):
  print "FT Test"

  if(verbose==1):
      print "FT Test - Set transmitter 0 active"
  #print "send set"
  #send_message(sock,"FT0");
  #time.sleep(1)
  #print "send read"
  #send_message(sock,"FT;")  
  #lcl_result =  recv_message(sock)
  #print "FT="+lcl_result
  #check(sock,"FT0;",lcl_result)
  #print "End check"

  #if(verbose==1):
  #    print "FT Test Set Active Transmitter 1"
  #send_message(sock,"FT1");
  #time.sleep(1)
  #send_message(sock,"FT;")  
  #check(sock,"FT1;",recv_message(sock))
 
  #if(verbose==1):
  #    print "FT Test Set Active Transmitter 1"
  #send_message(sock,"FT1");
  #time.sleep(1)
  #send_message(sock,"FT;")  
  #check(sock,"FT1;",recv_message(sock))
 
#######################################################################
# 
# FW Test - Sets/read DSP filter
#
#######################################################################

def FW_TEST(sock):
  print "FW Test"
  if(verbose==1):
     print "FW Test - set CW mode"
  send_message(sock,"MD3;")
  time.sleep(1)
  if(verbose==1):
     print "FW Test - set Filter 50"
  send_message(sock,"FW0050;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0050;",recv_message(sock))

  if(verbose==1):
     print "FW Test - set Filter 100"
  send_message(sock,"FW0100;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0100;",recv_message(sock))

  if(verbose==1):
     print "FW Test - set Filter 150->maps to 100"
  send_message(sock,"FW0150;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0100;",recv_message(sock))


  if(verbose==1):
     print "FW Test - set Filter 150->maps to 200->maps to 300"
  send_message(sock,"FW0200;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0300;",recv_message(sock))

  # Originally was 250- an illegal value for TS-2000
  if(verbose==1):
     print "FW Test - set Filter 300"
  send_message(sock,"FW0300;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0300;",recv_message(sock))

  if(verbose==1):
     print "FW Test - set Filter 400"
  send_message(sock,"FW0400;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0400;",recv_message(sock))

  if(verbose==1):
     print "FW Test - set Filter 500"
  send_message(sock,"FW0500;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0500;",recv_message(sock))

  if(verbose==1):
     print "FW Test - set Filter 600"
  send_message(sock,"FW0600;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW0600;",recv_message(sock))

  if(verbose==1):
     print "FW Test - set Filter 1000"
  send_message(sock,"FW1000;")
  time.sleep(0.1)
  send_message(sock,"FW;")  
  check(sock,"FW1000;",recv_message(sock))

  send_message(sock,"MD3;")
  time.sleep(1)

#######################################################################
# 
# GT Test - Sets/read AGC Constant
#
#######################################################################

def GT_TEST(sock):
  print "GT Test"
  if(verbose==1):
     print "AGC Off"
  send_message(sock,"GT000;")
  send_message(sock,"GT;")  
  check(sock,"GT000;",recv_message(sock))
  
  if(verbose==1):
     print "AGC Fast"
  send_message(sock,"GT005;")
  send_message(sock,"GT;")  
  check(sock,"GT005;",recv_message(sock))
  
  if(verbose==1):
     print "AGC Medium"
  send_message(sock,"GT010;")
  send_message(sock,"GT;")  
  check(sock,"GT010;",recv_message(sock))
  
  if(verbose==1):
     print "AGC Slow"
  send_message(sock,"GT015;")
  send_message(sock,"GT;")  
  check(sock,"GT015;",recv_message(sock))
  
  if(verbose==1):
     print "AGC Long"
  send_message(sock,"GT020;")
  send_message(sock,"GT;")
  check(sock,"GT020;",recv_message(sock))
  
#######################################################################
# 
# ID Test - Read Radio ID - TS2000=19
#
#######################################################################

def ID_TEST(sock):
  print "ID Test"
  send_message(sock,"ID;")
  check(sock,"ID019;",recv_message(sock))


#######################################################################
# 
# IF Test - Radio Status
#
#######################################################################

def IF_TEST(sock):
  print "IF Test"
  # First set up conditions for test
  # 28MHz
  # LSB
  # step = 5KHz
  # RIT OFF
  # Receive operation
  send_message(sock,"FA00028000000;")
  time.sleep(1)
  send_message(sock,"MD3;")
  time.sleep(1)
  send_message(sock,"ST02;")
  send_message(sock,"RC;")  # Clear RIT Offset
  send_message(sock,"RT0;")
  send_message(sock,"RX;")
  send_message(sock,"CN01;");
  send_message(sock,"CT0;");

  send_message(sock,"IF;");
  check(sock,"IF00028000000500000000000000030000010;",recv_message(sock))
   
  if(verbose==1):
     print "Change step"
  send_message(sock,"ST03;")
  send_message(sock,"IF;")
  check(sock,"IF00028000000100000000000000030000010;",recv_message(sock))
 

  if(verbose==1):
     print "Change mode"
  send_message(sock,"MD4;")
  send_message(sock,"IF;")
  check(sock,"IF00028000000100000000000000040000010;",recv_message(sock))

  if(verbose==1):
     print "Change freq"
  send_message(sock,"FA00028123456;")
  time.sleep(1)


  send_message(sock,"IF;")
  check(sock,"IF00028123456100000000000000040000010;",recv_message(sock))



#######################################################################
# 
# KS Test - Set/reads CW speed from 0 to 060 max
#
#######################################################################

def KS_TEST(sock):
  print "KS Test" 

  if(verbose==1):
     print "Set CW speed to 1"
  send_message(sock,"KS001;")
  send_message(sock,"KS;")  
  check(sock,"KS001;",recv_message(sock))

  if(verbose==1):
     print "Set CW speed to 60"
  send_message(sock,"KS060;")
  send_message(sock,"KS;")  
  check(sock,"KS060;",recv_message(sock))

  if(verbose==1):
     print "Set CW speed to 0 - response?;"
  send_message(sock,"KS000;")
  check(sock,"?;",recv_message(sock))

  if(verbose==1):
     print "Set CW speed to 61 - response?;"
  send_message(sock,"KS061;")
  check(sock,"?;",recv_message(sock))

#######################################################################
# 
# LK Test - Set/reads lock state
#
#######################################################################

def LK_TEST(sock):

  print "LK Test"
  if(verbose==1):
     print "LK Test - set Lock Off"
  send_message(sock,"LK00;")
  send_message(sock,"LK;")
  check(sock,"LK00;",recv_message(sock))

  if(verbose==1):
     print "LK Test - set Lock On"
  send_message(sock,"LK10;")
  send_message(sock,"LK;")
  check(sock,"LK11;",recv_message(sock))

  # Now return things to nominal
  send_message(sock,"LK00;")

#######################################################################
# 
# MD Test - Set/reads Radio Mode
#
#######################################################################

def MD_TEST(sock):
  print "MD Test"

  if(verbose==1):
     print "MD Test - LSB "
  send_message(sock,"MD1;")
  send_message(sock,"MD;")
  check(sock,"MD1;",recv_message(sock))

  if(verbose==1):
     print "MD Test - USB "
  send_message(sock,"MD2;")
  send_message(sock,"MD;")
  check(sock,"MD2;",recv_message(sock))

  if(verbose==1):
     print "MD Test - CWU "
  send_message(sock,"MD3;")
  send_message(sock,"MD;")
  check(sock,"MD3;",recv_message(sock))

  if(verbose==1):
     print "MD Test - FMN "
  send_message(sock,"MD4;")
  send_message(sock,"MD;")
  check(sock,"MD4;",recv_message(sock))

  if(verbose==1):
     print "MD Test - AM "
  send_message(sock,"MD5;")
  send_message(sock,"MD;")
  check(sock,"MD5;",recv_message(sock))

  if(verbose==1):
     print "MD Test - DIGL "
  send_message(sock,"MD6;")
  send_message(sock,"MD;")
  check(sock,"MD6;",recv_message(sock))

  if(verbose==1):
     print "MD Test - CWL "
  send_message(sock,"MD7;")
  send_message(sock,"MD;")
  check(sock,"MD7;",recv_message(sock))

  if(verbose==1):
     print "MD Test - DIGU "
  send_message(sock,"MD9;")
  send_message(sock,"MD;")
  check(sock,"MD9;",recv_message(sock))


#######################################################################
# 
# MG Test - Set/reads Mic Gain
#           3 digits: Range 0-100
#
#######################################################################

def MG_TEST(sock):
  print "MG Test"

  if(verbose==1):
     print "MG Test - off "
  send_message(sock,"MG000;")
  time.sleep(0.2)
  send_message(sock,"MG;")
  check(sock,"MG000;",recv_message(sock))

  if(verbose==1):
     print "MG Test - Max "
  send_message(sock,"MG100;")
  time.sleep(0.2)
  send_message(sock,"MG;")
  check(sock,"MG100;",recv_message(sock))

  if(verbose==1):
     print "MG Test - Mid "
  send_message(sock,"MG050;")
  time.sleep(0.2)
  send_message(sock,"MG;")
  check(sock,"MG050;",recv_message(sock))

#######################################################################
# 
# MR Test - Read Memory Channel - partially implemented
#           No memories as such.
#
#######################################################################

def MR_TEST(sock):
  print "MR Test"

  # Set P4 to known value
  send_message(sock,"FA00028123456;")
  time.sleep(0.2)
  send_message(sock,"MD4;")
  send_message(sock,"LK00;")
  send_message(sock,"CN01;")
  send_message(sock,"CT0;");
  send_message(sock,"MR;");
  check(sock,"MR00000002812345640001010000000000000000000000000;",recv_message(sock))
     
  if(verbose==1):
     print "MG Test - Change Frequency "
  send_message(sock,"FA00028000000;")
  time.sleep(0.2)
  send_message(sock,"MR;");
  check(sock,"MR00000002800000040001010000000000000000000000000;",recv_message(sock))

  if(verbose==1):
     print "MG Test - Change Mode "
  send_message(sock,"MD3;")
  time.sleep(0.2)
  send_message(sock,"MR;");
  check(sock,"MR00000002800000030001010000000000000000000000000;",recv_message(sock))

  if(verbose==1):
     print "MG Test - Change Tone "
  send_message(sock,"CN39;")
  send_message(sock,"MR;");
  check(sock,"MR00000002800000030039390000000000000000000000000;",recv_message(sock))

  if(verbose==1):
     print "MG Test - Change Tone Enable"
  send_message(sock,"CT1;")
  send_message(sock,"MR;");
  check(sock,"MR00000002800000030139390000000000000000000000000;",recv_message(sock))

  if(verbose==1):
     print "MG Test - Change Locked"
  send_message(sock,"LK11;")
  send_message(sock,"MR;");
  check(sock,"MR00000002800000031139390000000000000000000000000;",recv_message(sock))

  
#######################################################################
# 
# NB Test - Set/Read Noise Blanker
#
#######################################################################

def NB_TEST(sock):
  print "NB Test"

  if(verbose==1):
     print "NB Test - off "
  send_message(sock,"NB0;")
  time.sleep(0.2)
  send_message(sock,"NB;")
  check(sock,"NB0;",recv_message(sock))

  if(verbose==1):
     print "NB Test - on "
  send_message(sock,"NB1;")
  time.sleep(0.2)
  send_message(sock,"NB;")
  check(sock,"NB1;",recv_message(sock))

#######################################################################
# 
# NR Test - Set/Read Noise Reduction -0,1,2,X
#
#######################################################################

def NR_TEST(sock):
  print "NR Test"

  if(verbose==1):
     print "NR Test - off "
  send_message(sock,"NR0;")
  time.sleep(0.2)
  send_message(sock,"NR;")
  check(sock,"NR0;",recv_message(sock))

  if(verbose==1):
     print "NR Test - NR1 "
  send_message(sock,"NR1;")
  time.sleep(0.2)
  send_message(sock,"NR;")
  check(sock,"NR1;",recv_message(sock))

  if(verbose==1):
     print "NR Test - NR2 "
  send_message(sock,"NR2;")
  time.sleep(0.2)
  send_message(sock,"NR;")
  check(sock,"NR2;",recv_message(sock))

  if(verbose==1):
     print "NR Test - X "
  send_message(sock,"NR3;")
  time.sleep(0.2)
  check(sock,"?;",recv_message(sock))

#######################################################################
# 
# NT Test - Set/Read Auto Noise Filter 0,1,X
#
#######################################################################

def NT_TEST(sock):

  print "NT Test"

  if(verbose==1):
     print "NT Test - off "
  send_message(sock,"NT0;")
  send_message(sock,"NT;")
  check(sock,"NT0;",recv_message(sock))

  if(verbose==1):
     print "NT Test - on "
  send_message(sock,"NT1;")
  send_message(sock,"NT;")
  check(sock,"NT1;",recv_message(sock))

  if(verbose==1):
     print "NT Test - X "
  send_message(sock,"NT2;")
  check(sock,"?;",recv_message(sock))


#######################################################################
# 
# PA Test - Set/Read Preamp function status
#
#######################################################################

def PA_TEST(sock):
  print "PA Test"

  if(verbose==1):
     print "PA Test - off "
  send_message(sock,"PA0;")
  send_message(sock,"PA;")
  check(sock,"PA00;",recv_message(sock))

  if(verbose==1):
     print "PA Test - on "
  send_message(sock,"PA1;")
  send_message(sock,"PA;")
  check(sock,"PA11;",recv_message(sock))

  if(verbose==1):
     print "PA Test - X "
  send_message(sock,"PA2;")
  check(sock,"?;",recv_message(sock))

#######################################################################
# 
# RC Test - Set/Read Drive Power Level 0-100,x
#
#######################################################################

def PC_TEST(sock):
  print "RC Test"

  # Set the RIT so we know it is set... RT hasn't been tested in sequence yet!
  send_message(sock,"RT1;")
  send_message(sock,"RT;")
  check(sock,"RT1;",recv_message(sock))

  if(verbose==1):
     print "PC Test - max "
  send_message(sock,"PC100;")
  time.sleep(0.2)
  send_message(sock,"PC;")
  check(sock,"PC100;",recv_message(sock))

  if(verbose==1):
     print "PC Test - mid "
  send_message(sock,"PC050;")
  time.sleep(0.2)
  send_message(sock,"PC;")
  check(sock,"PC050;",recv_message(sock))

  if(verbose==1):
     print "PC Test - lsb "
  send_message(sock,"PC053;")
  time.sleep(0.2)
  send_message(sock,"PC;")
  check(sock,"PC053;",recv_message(sock))

  if(verbose==1):
     print "PC Test - X "
  send_message(sock,"PC153;")
  time.sleep(0.2)
  check(sock,"?;",recv_message(sock))


#######################################################################
# 
# RA Test - Set/Read Attenuation 00-99 
#
#######################################################################

def RA_TEST(sock):
  print "RA Test"

  if(verbose==1):
     print "RA Test - min "
  send_message(sock,"RA00;")
  time.sleep(0.2)
  send_message(sock,"RA;")
  check(sock,"RA0000;",recv_message(sock))

  if(verbose==1):
     print "RA Test - max "
  send_message(sock,"RA99;")
  time.sleep(0.2)
  send_message(sock,"RA;")
  check(sock,"RA9999;",recv_message(sock))

  if(verbose==1):
     print "RA Test - mid "
  send_message(sock,"RA50;")
  time.sleep(0.2)
  send_message(sock,"RA;")
  check(sock,"RA5050;",recv_message(sock))

  if(verbose==1):
     print "RA Test - X "
  send_message(sock,"RA100;")
  time.sleep(0.2)
  check(sock,"?;",recv_message(sock))


#######################################################################
# 
# RC Test - clear RIT function
#
#######################################################################

def RC_TEST(sock):
  print "RC Test"
  
  # Set the RIT Frequency Incremn
  send_message(sock,"RD99999;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  #print "extracted valuae:"+lcl_val[18:24]+":"
  new_val = lcl_val[18:24]
  #print "New val = "+new_val
  if int(new_val) != -99999:
     print "RD failed to set to -99999, got "+new_val; 
   
  # Now clear RIT frequency with RC 
  send_message(sock,"RC;")
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 0:
     print "RC Command failed to clear rit frequency, got "+new_val
  
#######################################################################
# 
# RD Test - Decrement RIT frequency
#
#######################################################################

def RD_TEST(sock):
  print "RD Test"

  send_message(sock,"RD00001;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -1:
      print "RD Test - Error - Frequency not set to -1"

  send_message(sock,"RD00010;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -10:
      print "RD Test - Error - Frequency not set to -10"

  send_message(sock,"RD00100;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -100:
      print "RD Test - Error - Frequency not set to -100"

  send_message(sock,"RD01000;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -1000:
      print "RD Test - Error - Frequency not set to -1000"

  send_message(sock,"RD10000;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -10000:
      print "RD Test - Error - Frequency not set to -10000"

  send_message(sock,"RD99999;") # Note RD not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -99999:
      print "RD Test - Error - Frequency not set to -99999"

  
  send_message(sock,"FS0;") # Turn off FINE decrement - 10hz expected
  send_message(sock,"RD10000;") # Note RD not test yet in sequence
  send_message(sock,"RD;")  # Decrement from 99999 to 99989
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -10010:
      print "RD Test - Error - Decrement by 10Hz didn't function,val="+new_val

  send_message(sock,"FS1;") # Turn on FINE decrement - 1hz expected
  send_message(sock,"RD;")  # Decrement from 99999 to 99989
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != -10011:
      print "RD Test - Error - Decrement by 1Hz didn't function,val="+new_val


#######################################################################
# 
# RG Test - AGC Gain - 0-255 values allowed
#
#######################################################################

def RG_TEST(sock):
  print "RG Test"

  if(verbose==1):
     print "RG Test - max "
  send_message(sock,"RG255;")
  time.sleep(1)
  send_message(sock,"RG;")
  check(sock,"RG255;",recv_message(sock))

  if(verbose==1):
     print "RG Test - min "
  send_message(sock,"RG000;")
  time.sleep(1)
  send_message(sock,"RG;")
  check(sock,"RG000;",recv_message(sock))

  if(verbose==1):
     print "RG Test - mid "
  send_message(sock,"RG126;")
  time.sleep(1)
  send_message(sock,"RG;")
  check(sock,"RG126;",recv_message(sock))

#######################################################################
# 
# RT Test - Test RIT state,0,1,X
#
#######################################################################

def RT_TEST(sock):
  print "RT Test"

  send_message(sock,"RT0;")
  send_message(sock,"RT;")
  check(sock,"RT0;",recv_message(sock))
  send_message(sock,"RT1;")
  send_message(sock,"RT;")
  check(sock,"RT1;",recv_message(sock))
  send_message(sock,"RT2;")
  check(sock,"?;",recv_message(sock))

#######################################################################
# 
# RU Test - Decrement RIT frequency
#
#######################################################################

def RU_TEST(sock):
  print "RU Test"

  send_message(sock,"RU00001;") # Note RU not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 1:
      print "RU Test - Error - Frequency not set to 1"

  send_message(sock,"RU00010;") # Note RU not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 10:
      print "RU Test - Error - Frequency not set to 10"

  send_message(sock,"RU00100;") # Note RU not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 100:
      print "RU Test - Error - Frequency not set to 100"

  send_message(sock,"RU01000;") # Note RU not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 1000:
      print "RU Test - Error - Frequency not set to 1000"

  send_message(sock,"RU10000;") # Note RU not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 10000:
      print "RU Test - Error - Frequency not set to 10000"

  send_message(sock,"RU99999;") # Note RU not test yet in sequence
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 99999:
      print "RU Test - Error - Frequency not set to 99999"

  
  send_message(sock,"FS0;") # Turn off FINE increment - 10hz expected
  send_message(sock,"RU10000;") 
  send_message(sock,"RU;")  # Decrement from 99999 to 99989
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 10010:
      print "RU Test - Error - Increment by 10Hz didn't function,val="+new_val

  send_message(sock,"FS1;") # Turn on FINE increment - 1hz expected
  send_message(sock,"RU;")  # Decrement from 99999 to 99989
  send_message(sock,"IF;")
  lcl_val = recv_message(sock)
  new_val = lcl_val[18:24]
  if int(new_val) != 10011:
      print "RU Test - Error - Increment by 1Hz didn't function,val="+new_val

#######################################################################
# 
# SD Test - Set/Read Break-in Delay
#
#######################################################################

def SD_TEST(sock):
  print "SD Test"


  if(verbose==1):
     print "SD Test - max "
  send_message(sock,"SD1000;")
  send_message(sock,"SD;")
  check(sock,"SD1000;",recv_message(sock))

  if(verbose==1):
     print "SD Test - min "
  send_message(sock,"SD0000;")
  send_message(sock,"SD;")
  check(sock,"SD0000;",recv_message(sock))

  if(verbose==1):
     print "SD Test - mid "
  send_message(sock,"SD0500;")
  send_message(sock,"SD;")
  check(sock,"SD0500;",recv_message(sock))

  if(verbose==1):
     print "SD Test - smallest "
  send_message(sock,"SD0050;")
  send_message(sock,"SD;")
  check(sock,"SD0050;",recv_message(sock))

#######################################################################
# 
# SQ Test - Set/Read Squelch 0-255 values - only for NON-FM
#           FM uses 0-100 - need to code that...
#
#######################################################################

def SQ_TEST(sock):
 
  print "SQ Test"

  if(verbose==1):
     print "SQ Test - max "
  send_message(sock,"SQ0255;")
  send_message(sock,"SD;")
  check(sock,"SQ0255;",recv_message(sock))

  if(verbose==1):
     print "SQ Test - min "
  send_message(sock,"SQ0000;")
  send_message(sock,"SD;")
  check(sock,"SQ0000;",recv_message(sock))

  if(verbose==1):
     print "SQ Test - min "
  send_message(sock,"SQ0100;")
  send_message(sock,"SD;")
  check(sock,"SQ0100;",recv_message(sock))

  if(verbose==1):
     print "SQ Test - X "
  send_message(sock,"SQ0256;")
  check(sock,"?;",recv_message(sock))
  
#######################################################################
# 
# ST Test - Set/Read Step
#
#######################################################################

def ST_TEST(sock):

  print "ST Test"

  send_message(sock,"MD3;") # Change to LSB
  if(verbose==1):
     print "ST Test - LSB 1Khz "
  send_message(sock,"ST00;")
  send_message(sock,"ST;")
  check(sock,"ST00;",recv_message(sock))

  if(verbose==1):
     print "ST Test - LSB 2.5Khz "
  send_message(sock,"ST01;")
  send_message(sock,"ST;")
  check(sock,"ST01;",recv_message(sock))

  if(verbose==1):
     print "ST Test - LSB 5 Khz "
  send_message(sock,"ST02;")
  send_message(sock,"ST;")
  check(sock,"ST02;",recv_message(sock))

  if(verbose==1):
     print "ST Test - LSB 10 Khz "
  send_message(sock,"ST03;")
  send_message(sock,"ST;")
  check(sock,"ST03;",recv_message(sock))

  send_message(sock,"MD5;") # Change to AM
  if(verbose==1):
     print "ST Test - AM 5 Khz "
  send_message(sock,"ST00;")
  send_message(sock,"ST;")
  check(sock,"ST00;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 6.25 Khz "
  send_message(sock,"ST01;")
  send_message(sock,"ST;")
  check(sock,"ST01;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 10 Khz "
  send_message(sock,"ST02;")
  send_message(sock,"ST;")
  check(sock,"ST02;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 12 Khz "
  send_message(sock,"ST03;")
  send_message(sock,"ST;")
  check(sock,"ST03;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 15 Khz "
  send_message(sock,"ST04;")
  send_message(sock,"ST;")
  check(sock,"ST04;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 20 Khz "
  send_message(sock,"ST05;")
  send_message(sock,"ST;")
  check(sock,"ST05;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 25 Khz "
  send_message(sock,"ST06;")
  send_message(sock,"ST;")
  check(sock,"ST06;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 30 Khz "
  send_message(sock,"ST07;")
  send_message(sock,"ST;")
  check(sock,"ST07;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 50 Khz "
  send_message(sock,"ST08;")
  send_message(sock,"ST;")
  check(sock,"ST08;",recv_message(sock))

  if(verbose==1):
     print "ST Test - AM 100 Khz "
  send_message(sock,"ST09;")
  send_message(sock,"ST;")
  check(sock,"ST09;",recv_message(sock))

  
#######################################################################
# 
# TY Test - Software type
#
#######################################################################
def TY_TEST(sock):

  print "TY Test"

  send_message(sock,"TY;")
  check(sock,"TY000;",recv_message(sock))

#######################################################################
# 
# VD Test - Set/Read Vox delay
#
#######################################################################
def VD_TEST(sock):

  print "VD Test"

  if(verbose==1):
     print "VD Test - min"
  send_message(sock,"VD0000;")
  send_message(sock,"VD;")
  check(sock,"VD0000;",recv_message(sock))

  if(verbose==1):
     print "VD Test - max"
  send_message(sock,"VD1000;")
  send_message(sock,"VD;")
  check(sock,"VD1000;",recv_message(sock))

  if(verbose==1):
     print "VD Test - mid"
  send_message(sock,"VD0500;")
  send_message(sock,"VD;")
  check(sock,"VD0500;",recv_message(sock))

#######################################################################
# 
# VG Test - Vox Gain
#
#######################################################################
def VG_TEST(sock):

  print "VG Test"

  if(verbose==1):
     print "VG Test - 0"
  send_message(sock,"VG000;")
  send_message(sock,"VG;")
  check(sock,"VG000;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 1"
  send_message(sock,"VG001;")
  send_message(sock,"VG;")
  check(sock,"VG001;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 2"
  send_message(sock,"VG002;")
  send_message(sock,"VG;")
  check(sock,"VG002;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 3"
  send_message(sock,"VG003;")
  send_message(sock,"VG;")
  check(sock,"VG003;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 4"
  send_message(sock,"VG004;")
  send_message(sock,"VG;")
  check(sock,"VG004;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 5"
  send_message(sock,"VG005;")
  send_message(sock,"VG;")
  check(sock,"VG005;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 6"
  send_message(sock,"VG006;")
  send_message(sock,"VG;")
  check(sock,"VG006;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 7"
  send_message(sock,"VG007;")
  send_message(sock,"VG;")
  check(sock,"VG007;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 8"
  send_message(sock,"VG008;")
  send_message(sock,"VG;")
  check(sock,"VG008;",recv_message(sock))

  if(verbose==1):
     print "VG Test - 9"
  send_message(sock,"VG009;")
  send_message(sock,"VG;")
  check(sock,"VG009;",recv_message(sock))

  if(verbose==1):
     print "VG Test - X"
  send_message(sock,"VG010;")
  check(sock,"?;",recv_message(sock))

#######################################################################
# 
# VX Test - Vox State
#
#######################################################################
def VX_TEST(sock):

  print "VX Test"

  if(verbose==1):
     print "VX Test - 0"
  send_message(sock,"VX0;")
  send_message(sock,"VX;")
  check(sock,"VX0;",recv_message(sock))

  if(verbose==1):
     print "VX Test - 1"
  send_message(sock,"VX1;")
  send_message(sock,"VX;")
  check(sock,"VX1;",recv_message(sock))

