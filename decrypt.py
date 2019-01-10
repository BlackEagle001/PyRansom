import os
import argparse
from Crypto.Cipher import AES

# Check arguments used
parser = argparse.ArgumentParser()
parser.add_argument("iv", help="The iv to use to decrypt", type=str)
parser.add_argument("key", help="The key to use to decrypt", type=str)
parser.add_argument("-d", "--directory", help="Directory to decrypt", type=str, default=".")
args = parser.parse_args()
# Get arguments
iv = args.iv.encode("utf-8")
key = args.key.encode("utf-8")
directory = args.directory
os.chdir(directory)
print("Current directory : {}".format(os.getcwd()))

# List files from the current directory
filename_list = os.listdir(directory)

print("Decryption starts")
for filename in filename_list:
    # Check whether the file should be decrypt
    if filename.split(".")[-1] == "lock":
        # If yes
        # Open ".lock" file and create the corresponding original file
        filename_original = ".".join(filename.split(".")[:-1])
        print(filename_original)
        file_encrypt = open(filename, "rb")
        file_decrypt = open(filename_original, "wb")
        # Read datas, decrypt them and write then into the file
        data_encrypt = file_encrypt.read()
        cipher = AES.new(key, AES.MODE_CFB, iv=iv)
        data_decrypt = cipher.decrypt(data_encrypt)
        file_decrypt.write(data_decrypt)
        # Close files
        file_encrypt.close()
        file_decrypt.close()
        os.remove(filename)

print("Finish")
