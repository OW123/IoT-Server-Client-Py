***Client - Server Comunication Program with Python***

*Server File*

The port and the host must be defined with the same conexion parameters . The*socket.socket() is an API used to send messages accross a network; is the form for Intern Process Comunication*. In the*socket .listen()*  goes the accepted number of conexions to the server script.

The server receives the conexion from the client and the address, so it continues printing and sending data from the client.

Always closing the conexion


*Client File*

The same logic goes to the client side. We need a defined IP and unused port.  The conexions are stablished and the comunication process continues until the client writes **bye** on the terminal. The client can sends and receives messages from the server.
