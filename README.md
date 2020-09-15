# block diagram of model
![](https://github.com/Dhruvil1632/output/blob/master/output%20images/client%20server%20archietecture.png)

# Client Side Setup
In computer networking , We familier with Master-slave , client server archietecture. Here client.py file contain source code , which is running in bakcend side of client. To make 
inorder and reliable communication , I used TCP protocol and which is functionality of transport layer. In code , I passed IP address of server and port number. In TCP , For communication
we are using socket address. So I binded port number with IP address in order to get socket address. After making connection with server , If client wants to terminate then , it send message like "quit".

# Server Side Setup
Here server.py file contain source code , which is running in server side. This code can able to every conncetion and maintain server side conncection. Server Side code is always is running mode. It has ability to establish connection and termination with client. In order to make connection with server , client has to make connection request. When server accept the connection request and for acknowledgment it produce message like "connection establish successfully" . After that server and client can communicate. Termination is de
When server gets message as "quit" , then it will terminate the connection.

