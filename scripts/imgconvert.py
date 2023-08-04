#!python3

from PIL import Image, ImageOps
from argparse import ArgumentParser
import sys
import math

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

if SCREEN_WIDTH % 2:
    print("image width must be even!", file=sys.stderr)
    sys.exit(1)

parser = ArgumentParser()
parser.add_argument('-i', action="store", dest="inputfile")
parser.add_argument('-n', action="store", dest="name")
parser.add_argument('-o', action="store", dest="outputfile")

args = parser.parse_args()

im = Image.open(args.inputfile)
# convert to grayscale
im = im.convert(mode='L')
im.thumbnail((SCREEN_WIDTH, SCREEN_HEIGHT), Image.ANTIALIAS)

print("New image size: " + str(im.size[0]) + "x" + str(im.size[1]))

# Write out the output file.
with open(args.outputfile, 'wb') as f:
    for y in range(0, im.size[1]):
        byte = 0
        done = True
        for x in range(0, im.size[0]):
            l = im.getpixel((x, y))
            if x % 2 == 0:
                byte = l >> 4
                done = False;
            else:
                byte |= l & 0xF0
                f.write(byte.to_bytes(1, byteorder='big'))
                done = True
        if not done:
            f.write(byte.to_bytes(1, byteorder='big'))
