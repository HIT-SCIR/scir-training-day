#!/usr/bin/env python
import sys
import cPickle as pickle
wordcount={}

if __name__=="__main__":
    try:
        fp=open(sys.argv[1],"r")
    except:
        print>>sys.stderr,"Failed to open file"
        sys.exit(1)

    for line in fp:
        for word in line.strip().split():
            if word not in wordcount:
                wordcount[word]=0
            wordcount[word]+=1

    vocab = set([k for k in wordcount if wordcount[k]>2])
    pickle.dump(vocab, open(sys.argv[2], "w"))
