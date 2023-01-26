import socket


def server_program():
    # get the hostname
    host = "192.168.164.161"
    port = 5000  

    server_socket = socket.socket()  
    server_socket.bind((host, port))


    server_socket.listen(4)
    conn, address = server_socket.accept()  
    print("Connection from: " + str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode()) 

    conn.close()


server_program()