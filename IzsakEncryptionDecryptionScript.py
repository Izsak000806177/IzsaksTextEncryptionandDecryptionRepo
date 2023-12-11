
from cryptography.fernet import Fernet
import argparse #the import argparse command is used for parsing arguments that are in the command-line. This just means that by importing this module it makes it easier to write commmands in the command-line interface. The argparse module is also capable of generating help and usage messages along with error messages
import os#The import os module is in this script becuase it provides functions for creating and deleting directories as well as changing the current directory


def generate_the_key():#This function is put into place to be able to generate a new encryption key
    return Fernet.generate_key()#This line of code will be able to generate a key using Fornet

def save_the_key(key, filename):#This function is put into palce to be able to save the encrypted key to a file
    with open(filename, 'wb') as key_file:#This command is put into place to open the file in a binary write mode
        key_file.write(key)#This command will be able to encrypt a key to a file

def load_the_key(filename):#This function is put into place to load the encryption key from a file
    return open(filename, 'rb').read()#This function will open the file in the read mode for binary and it will be able to read the key

def encrypt_the_message(message, key):#This function will encrypt a message only using a specific key though
    cipher_suite = Fernet(key)#This code will create a object thats connected to Fernet with the specifc key
    encrypted_message = cipher_suite.encrypt(message.encode())#This line of code will ENCRYPT THE MESSAGE 
    return encrypted_message

def decrypt_the_message(encrypted_message, key):#This function will decrypt a message only using a specific key though
    cipher_suite = Fernet(key)#This code will create a object thats connected to Fernet with the specifc key
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()#This line of code will DECRYPT THE MESSAGE 
    return decrypted_message

def write_the_file(filename, data):#This function will write specific data the the file
    with open(filename, 'wb') as file:#This line of code will be able to open the code in the write mode for binary
        file.write(data)#This line of code will write data to the file

def read_to_the_file(filename): # This function will do the oposite and read the data that is contained in the file
    with open(filename, 'rb') as file:#This line of code will be able to open a file in the read mode of binary though
        return file.read()#This line of code will read the data that is contained in the file

def bulk():# "def bulk" this is the main function of the script that is going to perform boh encryption and decryption depending on the CLI
    parser = argparse.ArgumentParser(description="this is using both encryption and decryption methods")#This is an argument that would be use in the CLI and a brief explanation of what it is doing
    parser.add_argument('steps', choices=['encrypt', 'decrypt'], help='define action: encrypt or decrypt')#This will ask the user if the file wants to be encrypted or decrypted
    parser.add_argument('--message', help='the message needs to be either encrypted or decrypted')#Thiis line of code will let the user know if the code needs to be encrypted or decypted
    parser.add_argument('--encryptfile', help='load encryption key')#This line will load the encryption key
    parser.add_argument('--inputfile', help='Read from one file and write to one')#This line will rad the key that is in one file and create and write it to another
    args = parser.parse_args()#The line of code is analyzing the command-line arguments 

    if args.steps == 'encrypt':#This is the code that is used for encrypting the file
        if not args.message or not args.encryptfile or not args.inputfile:
            print("User needs to --message, --encryptfile, and --inputfile for encryption.")
            return

        key = generate_the_key()#This line of code is put into place to make a key that is encrypted
        save_the_key(key, args.encryptfile)#This line of code will do the next step and will save the file that will contain the encrypted key
        message = args.message.encode()#This line of code will package the message and encrypt it using a specific key, the next step is sending the data to a file
        encrypted_message = encrypt_the_message(message, load_the_key(args.encryptfile))
        write_the_file(args.inputfile, encrypted_message)
        print(f"encrypted text was sent to {args.inputfile}.")

    elif args.action == 'decrypt':#This is the code that is used for decrypting the file
        if not args.encryptfile or not args.inputfile:
            print("Please provide --encryptfile and --inputfile for decryption.")
            return

        encrypted_message = read_to_the_file(args.inputfile)#This line of code will be able to look and read the content that is contained in the file 
        decrypted_message = decrypt_the_message(encrypted_message, load_the_key(args.encryptfile))#This line of code will decrypt the message using the encryption key
        print(f"This is the Decrypted message: {decrypted_message}")#This line of code will print the decrypted message 

if __name__ == '__bulk__':#this line of code is in place to make sure that the script is running
    bulk()#This line of code is calling the main "def bulk()"

# Izsak Illes 000806177
#Due December 10 2023 
#Denise Hager
# References 
#https://cryptography.io/en/latest/fernet/
#https://docs.python.org/3/library/argparse.html
#https://docs.python.org/3/library/os.html
#https://docs.python.org/3/library/crypto.html
#https://chat.openai.com/auth/login
#https://docs.python.org/3/tutorial/inputoutput.html
