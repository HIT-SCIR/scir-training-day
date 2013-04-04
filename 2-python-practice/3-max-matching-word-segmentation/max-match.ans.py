#!/usr/bin/env python
import cPickle as pickle
import sys

window_size=5

def max_match_segment(line, dic):
    # write your code here
    chars = line.decode("utf8")
    words = []
    idx = 0
    while idx < len(chars):
        matched = False
        for i in xrange(window_size, 0, -1):
            cand=chars[idx:idx+i].encode("utf8")
            if cand in dic:
                words.append(cand)
                matched = True
                break
        if not matched: 
            i = 1
            words.append(chars[idx].encode("utf8"))
        idx += i

    return words

if __name__=="__main__":

    try:
        fpi=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    try:
        dic = pickle.load(open(sys.argv[2], "r"))
    except:
        print >> sys.stderr, "failed to load dict %s" % sys.argv[2]
        sys.exit(1)

    for line in fpi:
        print "\t".join( max_match_segment(line.strip(), dic) )

