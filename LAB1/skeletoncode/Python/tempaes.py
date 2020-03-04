#finished!
from Crypto.Cipher import AES
from Crypto import Random
import sys
import codecs
import time
     
def fulfill_file(name):
    patch = '\x00'
    block_size = 16
    
    with open(name) as f:
        x = f.read()
        y = x

    if x:
        for i in range(0, len(x), block_size):
            if i + block_size < len(x):
                pass
            
            else:
                patch_num = block_size - len(x[i:])
                y = x + patch * (patch_num)

    return y

def encrypt(des1,plain_text):
   
    cipher_text = des1.encrypt(plain_text)
    return cipher_text

def write_file(output, cipher_text):
    
    f = open(output, "wb+")
    f.write(cipher_text)
    f.close()


def decrept(des2, cipher_text):
    
    msg = des2.decrypt(cipher_text)
    return msg
    
     
def main(cbc_key, iv,inputfile,output):

    chunk_size = 8          # may need to chagne later
    aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
    aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

    encrypt_time = 0
    decrept_time = 0

    #encrypt file
    plain_text = fulfill_file(inputfile)

    start1 = time.time()
    cipher_text = encrypt(aes1,plain_text)
            
    encrypt_time += time.time() - start1
    write_file(output,cipher_text)



    #decrept file 
    with open(output, "rb") as d:
        cipher = d.read()

        start2 = time.time()
        plain_text = decrept(aes2,cipher)
            
        decrept_time = time.time() - start2
        write_file(inputfile+"_decrept.txt",plain_text)
            

    print("encrypt time is: ",encrypt_time)
    print("decrept time is: ",decrept_time)

if __name__ == "__main__":
   
    decode_hex = codecs.getdecoder("hex_codec")
    cbc_key = sys.argv[1]
    iv = sys.argv[2]
    inputfile = sys.argv[3]
    output = sys.argv[4]

    main(cbc_key,iv,inputfile,output)   


# from Crypto.Cipher import AES
# from Crypto import Random

# cbc_key = Random.get_random_bytes(16)
# print '='*100                    
# print 'Key used: ', [x for x in cbc_key]

# iv = Random.get_random_bytes(16)
# print "IV used: ",[x for x in iv]
# print '='*100                    
# aes1 = AES.new(cbc_key, AES.MODE_CBC, iv)
# aes2 = AES.new(cbc_key, AES.MODE_CBC, iv)

# plain_text = 'hello world 1234' # <- 16 bytes
# print "Plaintext is: ", plain_text

# cipher_text = aes1.encrypt(plain_text)
# print"Ciphertext is: ",cipher_text

# msg=aes2.decrypt(cipher_text)
# print"Decrypted message: ", msg
# print '='*100                    
