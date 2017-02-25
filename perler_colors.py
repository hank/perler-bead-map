# Calculates the number of beads of all colors needed to compose a given image
import sys
from PIL import Image

try:
    imagefile = sys.argv[1]
except:
    print "Usage: {} IMAGEFILE".format(sys.argv[0])
    sys.exit(1)

# List of Lists
lol = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

beads = {}
with open('beads.hex.txt', 'r') as f:
    for bead in f.read().split("\n"):
        bead = bead.split("\t")
        if len(bead) == 3:
            val = "{} {}".format(bead[1], bead[0].title())
            key = bead[2]
            beads[key] = val

# Read in image
try:
    im = Image.open(imagefile)
except IOError:
    print "Failed to open image"
    sys.exit(1)
pixels = im.convert('RGB').load()
width, height = im.size

counts = {}

for x in range(width):
    for y in range(height):
        # Derive hex value
        r, g, b = pixels[x, y]
        hexval = "%02X%02X%02X" % (r, g, b)
        if hexval in beads.keys():
            if beads[hexval] in counts:
                counts[beads[hexval]] += 1
            else:
                counts[beads[hexval]] = 1
        else:
            print hexval, "not found"

for count in counts.keys():
    print "{}: {}".format(count, counts[count])
