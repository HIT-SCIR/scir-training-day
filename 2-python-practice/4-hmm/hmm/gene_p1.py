#!/usr/bin/env python
import sys
from math import log
ngram = {}
tags = set(["I-GENE", "O"])
if __name__=="__main__":
    try:
        fp=open(sys.argv[1], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    for line in fp:
        vol = line.strip().split()
        freq, type = vol[:2]
        freq = int(freq)
        if type == "WORDTAG" and freq < 5:
            gram = "$".join(vol[2:-1] + ["_RARE_"])
        else:
            gram = "$".join(vol[2:])

        #print vol[2]
        if gram not in ngram:
            ngram[gram] = 0
        ngram[gram] += freq

    fp.close()
    try:
        fp=open(sys.argv[2], "r")
    except:
        print >> sys.stderr, "failed to open file"
        sys.exit(1)

    def score(word, tag):
        gram = "$".join([tag, word])
        if gram not in ngram:
            return -99.
        return log(ngram[gram]) - log(ngram[tag])

    for line in fp:
        word = line.strip()
        if len(word) == 0:
            print
        else:
            print word, max(tags, key=lambda t: score(word, t))
        #print tags[max([score(word, t) for t in tags])[0]]
