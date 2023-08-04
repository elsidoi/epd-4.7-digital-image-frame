#!python3

from PIL import Image, ImageOps
from argparse import ArgumentParser
import sys
import math

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540

GRADIENT_STEP = SCREEN_WIDTH // 16

print("Gradient step = " + str(GRADIENT_STEP))

if SCREEN_WIDTH % 2:
    print("image width must be even!", file=sys.stderr)
    sys.exit(1)

parser = ArgumentParser()
parser.add_argument('-n', action="store", dest="name")
parser.add_argument('-o', action="store", dest="outputfile")

args = parser.parse_args()

# im = Image.open(args.inputfile)
# convert to grayscale
# im = im.convert(mode='L')
# im.thumbnail((SCREEN_WIDTH, SCREEN_HEIGHT), Image.ANTIALIAS)

# Write out the output file.
with open(args.outputfile, 'wb') as f:
    # f.write("const uint32_t {}_width = {};\n".format(args.name, SCREEN_WIDTH))
    # f.write("const uint32_t {}_height = {};\n".format(args.name, SCREEN_HEIGHT))
    # f.write(
    #     "const uint8_t {}_data[({}*{})/2] = {{\n".format(args.name, math.ceil(SCREEN_WIDTH / 2) * 2, SCREEN_HEIGHT)
    # )
    for y in range(0, SCREEN_HEIGHT):
        byte = 0
        done = True
        for x in range(0, SCREEN_WIDTH):

            l = x // GRADIENT_STEP

            if x % 2 == 0:
                byte = l & 0x0F
                done = False;
            else:
                byte |= l << 4
                f.write(byte.to_bytes(1, 'big'))
                done = True
        if not done:
            f.write(byte.to_bytes(1, 'big'))
