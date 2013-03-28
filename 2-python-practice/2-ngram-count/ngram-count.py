#!/usr/bin/env python

class NGram(object):

    def __init__(self, n):
        # n is the order of n-gram language model
        self.n = n

    # scan a sentence, extract the ngram and update their
    # frequence.
    #
    # @param    sentence    list{str}
    # @return   none
    def scan(self, sentence):
        # file your code here

    # caluclate the ngram of the words
    #
    # @param    words       list{str}
    # @return   int         count of the ngram
    def ngram(self, words):
        # file your code here


if __name__=="__main__":
    import sys
    print >> sys.stderr, "library is not runnable"
