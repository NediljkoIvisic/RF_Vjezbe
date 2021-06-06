import magic
import os
import glob

def find_extension(files):
    for fn in files:
        print(fn + "--->" + magic.from_buffer(open(fn, "rb").read(2048)))

if __name__ == "__main__":
        files = glob.glob('./*')
        find_extension(files)