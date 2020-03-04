# finished!
from Crypto.Cipher import DES
from Crypto import Random
import sys
import codecs
import time
     
def fulfill_file(name):
    patch = '\x00'
    block_size = 8
    
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
    des1 = DES.new(cbc_key, DES.MODE_CBC, iv)
    des2 = DES.new(cbc_key, DES.MODE_CBC, iv)

    encrypt_time = 0
    decrept_time = 0
    #encrypt file
    plain_text = fulfill_file(inputfile)

    start1 = time.time()
    cipher_text = encrypt(des1,plain_text)
            
    encrypt_time += time.time() - start1
    write_file(output,cipher_text)



    #decrept file 
    with open(output, "rb") as d:
        cipher = d.read()

        start2 = time.time()
        plain_text = decrept(des2,cipher)
            
        decrept_time = time.time() - start2
        write_file(inputfile + "decrept.txt",plain_text)
            

    print("encrypt time is: ",encrypt_time)
    print("decrept time is: ",decrept_time)

if __name__ == "__main__":
   
    decode_hex = codecs.getdecoder("hex_codec")
    cbc_key = decode_hex(sys.argv[1])[0]
    iv = decode_hex(sys.argv[2])[0]
    inputfile = sys.argv[3]
    output = sys.argv[4]

    main(cbc_key,iv,inputfile,output)    
   