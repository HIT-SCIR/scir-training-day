from __future__ import print_function
import gzip
import sys

def read_dataset(filename='./penn.train.pos.gz'):
    try:
        fp=gzip.open(filename, 'r')
    except:
        print("Failed to open file.", file=sys.stderr)
        return
    
    dataset = []
    for line in fp:
        tokens = line.strip().split()
        dataset.append(([t.rsplit('/', 1)[0] for t in tokens], [t.rsplit('/', 1)[1] for t in tokens]))
    return dataset