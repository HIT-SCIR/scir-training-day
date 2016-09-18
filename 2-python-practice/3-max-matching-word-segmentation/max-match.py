#!/usr/bin/env python
import cPickle as pickle
import sys

def max_match_segment( line, dic ):
    # write your code here

if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        dic = pickle.load(open(sys.argv[2]))
    except:
        print >> sys.stderr, "failed to load dict"
        sys.exit(1)

    for line in fpi:
        print "\t".join( max_match_segment(line.strip(), dic) )

