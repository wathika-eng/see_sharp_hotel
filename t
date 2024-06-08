import socket
import select
import time

# Create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server.bind(("0.0.0.0", 6677))

# Listen for incoming connections
server.listen(4)
print("Server is listening on 10.0.0.1:6677")

try:
    # Accept a connection
    client_socket, client_address = server.accept()
    print(client_address, "has connected")

    # Set the timeout for receiving data
    timeout = 10  # 10 seconds
    end_time = time.time() + timeout

    while time.time() < end_time:
        # Use select to wait for data with a timeout
        ready_sockets, _, _ = select.select([client_socket], [], [], 1)
        if ready_sockets:
            received_data = client_socket.recv(1024)
            if not received_data:
                # If no data is received, break the loop
                break
            print("Received data:", received_data.decode())
        else:
            print("Waiting for data...")

except Exception as e:
    print("An error occurred:", e)
finally:
    # Clean up: close the client socket and server socket
    client_socket.close()
    server.close()
    print("Server has been closed")

