#Following code reads its source file and computes an HMAC signature for it:
import hmac
import time
import sys

def run(name):
    secret_key = 'secret-shared-key-goes-here'
    digest_maker = hmac.new(secret_key)#in your code replace key
    f = open(name, 'rb')
    try:
        while True:
            block = f.read(1024)
            if not block:
                break
            digest_maker.update(block)
    finally:
        f.close()
    start = time.time()
    digest = digest_maker.hexdigest()
    digest_time = time.time() - start
    print "digest_time:", digest_time

if __name__ == "__main__":
    filename = sys.argv[1]
    run(filename)    