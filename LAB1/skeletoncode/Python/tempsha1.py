import hashlib
import sys
import time


def run(inputfile):
    print '='*100
    f = open(inputfile, 'r')
    plain_text = f.read() 
    plain_text = plain_text.encode()
    
    start = time.time()
   
    result = hashlib.sha1(plain_text) 
    hash_time = time.time() - start

    # printing the equivalent hexadecimal value. 
    print("The hexadecimal equivalent of SHA1 digest is : ") 
    print(result.hexdigest())
    print "Time taken: ",hash_time
    print '='*100 

if __name__ == "__main__":
    inputfile = sys.argv[1]
    run(inputfile)