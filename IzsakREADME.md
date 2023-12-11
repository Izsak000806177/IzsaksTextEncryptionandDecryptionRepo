#README.md File 
# Izsak Illes 000806177
# Denise Hager
# Due Sunday December 10th 2023
# ChatGPT was used in this project
# Table of Contents 
    - Project Overview
    - Usage Guide
    - Configuration Guidelines
    - Contributing Guidelines
    - Conclusion
#This file is the README.md file that corresponds to my Encryptiona and Decryption Python Script.

#The purpose of this script to be  able to generate a CLI where the user that is using the script is able to give a message of their choosing 
#Along with a key value that will encrypt the message that was given by the user this will be done by using the Cryptography module for python
#The version of the python that I used to run this script was 
#Python 3.11.7
# Cryptography Version and description
    #Cryptography is a module that is connected to python. cryptography is put into place to provide cryptography methods to developers"
    #the version that was used in this script was version 41.0.7 this version was released on November 27th 2023
# The first step that it is going to ask you is if you want to generate a key
#This will be a simple Y/N (Yes No Answer)if the user types yes then it will gnerate a key using the fernet module
#The first line of code that is used to start generate and encrypting a key is listed below 
"""
def generate_the_key():
return Fernet.generate_key()
"""
# for example the prompt will ask the user 
# The next step the user needs to complete is saving the key in binary mode and encrypting the key to file 
# the commands that are used to save and encrypt the key to the saved file aare listed below

def save_the_key(key, filename):

# These command will open a file in write mode from binary
with open(filename, 'wb')

# The next stage of this script is to encrypt the message this 
    def encrypt_the_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

    python IzsakEncryptionDecryptionScript.py/ encrypt --message "This is an example" --encryptfile  C:/Users/CSAIT/Documents/EncryptionDecryption project/IzsakEncryptionDecryptionScript.key --inputfile C:/Users/CSAIT/Documents/EncryptionDecryption project/IzsakEncryptionDecryptionScript/IzsakEncryptionDecryptionFile.txt
# The next step that was included in the is writting the file
after encrypting the data it will write it to a file and which is where these different functions and lines of code play a part it will write the specified data to a file in the encrypyted state 
 
 def write_the_file(filename, data):
with open(filename, 'wb') as file:
file.write(data)
# After that the user will have to read the data 
    the user will go into the directory that it was stored which was 
# The next step is to decrypt the 
    the first function is going to take the message and decrypt it only using the key
# What does the user need to input?
the user has to input the line "python IzsakEncryptionDecryptionScript.py decrypt --encryptfile C:/Users/CSAIT/Documents/EncryptionDecryption project/IzsakEncryptionDecryptionScript.key --inputfile C:/Users/CSAIT/Documents/EncryptionDecryption project/IzsakEncryptionDecryptionScriptfile.txt

# The Bulk of the code with all the arguments 
the main function of the code will allow the user to use the CLI to encrypt the message and as well as give the user a description of what the code is actually doing. 

    def bulk():# "def bulk" this is the main function of the script that is going to perform boh encryption and decryption depending on the CLI
    parser = argparse.ArgumentParser(description="this is using both encryption and decryption methods")#This is an argument that would be use in the CLI and a brief explanation of what it is doing
    parser.add_argument('steps', choices=['encrypt', 'decrypt'], help='define action: encrypt or decrypt')#This will ask the user if the file wants to be encrypted or decrypted
    parser.add_argument('--message', help='the message needs to be either encrypted or decrypted')#Thiis line of code will let the user know if the code needs to be encrypted or decypted
    parser.add_argument('--encryptfile', help='load encryption key')#This line will load the encryption key
    parser.add_argument('--inputfile', help='Read from one file and write to one')#This line will rad the key that is in one file and create and write it to another
    args = parser.parse_args()#The line of code is analyzing the command-line arguments 

# The user needs to send the message that is encrypted to the file 
if args.steps == 'encrypt':#This is the code that is used for encrypting the file
        if not args.message or not args.encryptfile or not args.inputfile:
            print("User needs to --message, --encryptfile, and --inputfile for encryption.")
            return 
# The code above wil encrypt the message inside the file 
the user will have to input the command "python IzsakEncryptionDecryptionScript.py --encryptfile encryptedkeyfile.txt -- "The user types the secret messagee" --inputfile encrypted_message.txt

# the code below will decrypt the message that was just sent to encrypted_message.txt
elif args.action == 'decrypt':#This is the code that is used for decrypting the file
        if not args.encryptfile or not args.inputfile:
            print("Please provide --encryptfile and --inputfile for decryption.")
            return
# on the user end they have to input 
python IzsakEncryptionDecryptionScript.py --action decryp --encryptfile decrypted keyfile.txt --inputfile encrypted_message.txt

# the final step is to read the encrypted text in the file and decrypt it. 
# the code is 
 encrypted_message = read_to_the_file(args.inputfile)
 decrypted_message = decrypt_the_message(encrypted_message, load_the_key(args.encryptfile))
 print(f"This is the Decrypted message: {decrypted_message}")

# the user needs to input the following code to do so 
python IzsakEncryptionDecryptionScript.py --action decryp --encryptfile decrypted keyfile.txt --inputfile encrypted_message.txt


# References 
https://cryptography.io/en/latest/fernet/
https://docs.python.org/3/library/argparse.html
https://docs.python.org/3/library/os.html
https://docs.python.org/3/library/crypto.html
https://chat.openai.com/auth/login
https://docs.python.org/3/tutorial/inputoutput.html
