import magic
import hashlib
import os
import glob

def calculate_checksum(filenames):
    for fn in filenames:
        with open(fn, 'rb') as inputfile:
            data = inputfile.read()
            print("-----" + fn + "-----")
            print(hashlib.sha1(data).hexdigest())
            print(hashlib.md5(data).hexdigest())

if __name__ == "__main__":
    files = glob.glob('./*')
    calculate_checksum(files)