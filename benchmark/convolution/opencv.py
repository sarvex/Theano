from __future__ import print_function
import sys, timeit
import numpy
import scikits.image.opencv

try:
    img_shape =  int(sys.argv[1]), int(sys.argv[2])
    ker_shape =  int(sys.argv[3]), int(sys.argv[4])
    dtype = sys.argv[5]
except:
    print(
        f"Usage: {sys.argv[0]} <img rows> <img cols> <ker rows> <ker cols> <dtype> [nb_call]",
        file=sys.stderr,
    )
    sys.exit(-1)

nb_call = int(sys.argv[6]) if len(sys.argv)>6 else 1
T = timeit.Timer("f()","""
import scikits.image.opencv, sys, numpy
img_shape =  int(sys.argv[1]), int(sys.argv[2])
ker_shape =  int(sys.argv[3]), int(sys.argv[4])
dtype = sys.argv[5]

img = numpy.ones(img_shape, dtype=dtype)
ker = numpy.ones(ker_shape, dtype=dtype)

def f():
    scikits.image.opencv.cvFilter2D(img, ker)
""")
time = T.repeat(repeat=3, number=nb_call)
print(min(time), "opencv")

