import magic
import hashlib
import os
import glob

def find_extension(filename):
    print(filename + "----->" + magic.from_buffer(open(filename, "rb").read(2048)))

def calculate_checksum(filenames, checksum):
    for fn in filenames:
        with open(fn, 'rb') as inputfile:
            data = inputfile.read()
            if(checksum in hashlib.sha256(data).hexdigest()):
                return(fn)
            elif(checksum in hashlib.sha1(data).hexdigest()):
                return(fn)
            elif(checksum in hashlib.md5(data).hexdigest()):
                return(fn)

if __name__ == "__main__":
    checksum = 'c15e32d27635f248c1c8b66bb012850e5b342119'
    files = glob.glob('./*')
    filename = calculate_checksum(files,checksum)
    find_extension(filename)