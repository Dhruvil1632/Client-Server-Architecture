

# In[1]:


import socket
import sys


# In[2]:


#creating socket for connection with client
def create_socket():
    try:
        global port
        global host
        global s
        host = '192.168.43.187'
        port = 9999
        s = socket.socket()
        print("port number is :" + str(port))
        print("socket binding successfully")
    except socket.error as msg:
        print("socket creation error :" + str(msg))
create_socket()


# In[3]:


#binding host and port with socket
def bind_socket():
    try:
        global port
        global host
        global s
        s.bind((host,port))
        s.listen(0)
    except socket.error as msg:
        print("socket binding error" + str(msg) + "retrying......")
        bind_socket()
bind_socket()


# In[4]:


#establish connection with client (socket must be listining)
def socket_accept():
    print("waiting for client request")
    connection , address = s.accept()
    print("connection has been established " + " IP is "  + str(address[0]) + " port is  " + str(address[1]))
    #send_command(connection)
    #connection.close()
    return connection


# In[5]:


connection = socket_accept()


# In[6]:


client_response = 'sample'
while client_response != "quit":
    client_response = str(connection.recv(1024),'utf-8')
    # preprocesing of client response
    # cleint response = model.predict(client_response)
    print(client_response)
    sample = "server response " + client_response
    connection.send(str.encode(sample))


# In[ ]:





# In[ ]:





# In[ ]:




