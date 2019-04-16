import hashlib
import itertools
import string


saltPrefix = "FCC"
saltSuffix = "Cyber"
hashedPass = "1a37687f02790ebd6e1be5b211afdf67"

chars = string.ascii_letters + string.digits
for password_length in range(1,6):
    for iteration in itertools.product(chars, repeat=password_length):
        iteration = ''.join(iteration)
        fullHash = hashlib.md5(saltPrefix+iteration+saltSuffix).hexdigest()
        print fullHash ,iteration
        if fullHash.lower() == hashedPass:
            print "The password is: " + iteration
            exit(0)
