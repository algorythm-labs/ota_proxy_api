import socket

import requests
from CONFIG import IP, PORT, ACCELERATE_BRAKE_URL, HORN_BLINKERS_URL

def open_socket(ip):
    # Open a socket
    address = (ip, PORT)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return connection

def webpage(state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <head>
            <title>Control Unit Proxy API</title>
            <meta name="viewport" content="width=device-width, initial-scale=1">
            </head>
            <body>
            Secret testing
            <form action="./horn">
            <input type="submit" value="Horn" />
            </form>
            <form action="./accelerate">
            <input type="submit" value="Accelerate" />
            </form>
            <form action="./brake">
            <input type="submit" value="Brake" />
            </form>
            <form action="./left">
            <input type="submit" value="Left" />
            </form>
            <form action="./right">
            <input type="submit" value="Right" />
            </form>
            <p>Status is {state}</p>            
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    #Start a web server
    state = "NONE"  
    while True:
        client, addr = connection.accept()
        print("Connection from", addr)
        request = client.recv(1024)
        request = str(request)
        print(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        
        url = ""
        #endpoints handled
        if request == "/horn?" or request == "/horn":
            state = "HORN"
            url = HORN_BLINKERS_URL + "horn"
        elif request =="/accelerate?" or request =="/accelerate":
            state = "ACCELERATE"
            url = ACCELERATE_BRAKE_URL + "accelerate"
        elif request == "/brake?" or request == "/brake":
            state = "BRAKE"
            url = ACCELERATE_BRAKE_URL + "brake"
        elif request == "/left?" or request == "/left":
            state = "LEFT"
            url = HORN_BLINKERS_URL + "left"
        elif request == "/right?" or request == "/right":
            state = "RIGHT"
            url = HORN_BLINKERS_URL + "right"

        if url != "":
            x = requests.get(url)
            print(x.status_code)
            
        html = webpage(state)
        startStr = "HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n"
        client.send(startStr.encode())
        client.send(html.encode())
        client.close()

try:
    connection = open_socket(IP)
    serve(connection)
except KeyboardInterrupt:
    print("Exit")
