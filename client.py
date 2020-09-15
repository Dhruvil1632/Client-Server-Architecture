#!/usr/bin/env python
# coding: utf-8

# In[1]:


import io
import socket
import struct
import time
import cv2
import requests


# In[2]:


#creating socket , defining values of host and port as per server's value
s = socket.socket()
host = '192.168.43.187'
port = 9999


# In[3]:


# binding host and port with socket
s.connect((host , port))


# In[4]:


for i in range(0,100):
    time.sleep(2)
    message = input("Enter your message")
    s.send(str.encode(message))
    server_response = str(s.recv(1024),'utf-8')
    print(server_response)


# In[ ]:





# In[ ]:





# In[5]:



#connection.close()
s.close()

