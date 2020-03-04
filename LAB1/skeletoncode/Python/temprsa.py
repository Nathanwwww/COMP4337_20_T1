import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import sys
import time


def run(inputfile,outputfile):
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator) #generate pub and priv key

    publickey = key.publickey() # pub key export for exchange

    f = open(inputfile, 'r')
    plain_text = f.read()

    start1 = time.time()
    cipher_text = publickey.encrypt(plain_text, 32)
    encrypt_time = time.time() - start1
    #message to encrypt is in the above line 'encrypt this message'

   
    f = open (outputfile, 'w')
    f.write(str(cipher_text)) #write ciphertext to file
    f.close()

    #decrypted code below

    f = open(outputfile, 'r')
    message = f.read()
    
    start2 = time.time()
    decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
    decrypt_time = time.time() - start2
    

    f = open ('encryption.txt', 'w')
    f.write(str(message))
    f.write(str(decrypted))
    f.close()

    print "Encrypt time is: ",encrypt_time
    print "Decrypt time is: ",decrypt_time

if __name__ == "__main__":
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]

    run(inputfile, outputfile)

#-------------------------------------------------
# random_generator = Random.new().read
# key = RSA.generate(1024, random_generator) #generate pub and priv key

# publickey = key.publickey() # pub key export for exchange

# print '='*100                    
# plain_text = 'abcdefghijklmnopqrst'
# print "Plaintext is: ", plain_text
# print

# cipher_text = publickey.encrypt(plain_text, 32)#message to encrypt is in the above line 'encrypt this message'
# print 'Plaintext encrypted using Public Key is:', cipher_text
# print 
# #decrypted code below
# decrypted = key.decrypt(ast.literal_eval(str(cipher_text)))
# print ('Ciphertext decrypted with Private key is', decrypted)
# print '='*100



