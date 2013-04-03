#!/usr/bin/env python
import sys
from math import log
ngram = {}
tags = set(["I-GENE", "O"])
vocabulary=set()
debug_mode = False 
class State(object):
    def __init__(self, score=-float("inf"), word="", tag="", prev=None):
        self.score = score
        self.tag  = tag
        self.word = word
        self.prev = prev

    def __lt__(self, other): return self.score <  other.score
    def __le__(self, other): return self.score <= other.score
    def __gt__(self, other): return self.score >  other.score
    def __ge__(self, other): return self.score >= other.score
    def __eq__(self, other): return self.score == other.score
    def __ne__(self, other): return self.score != other.score

    def __str__(self):
        ret =  "(word:\"%s\"|tag:\"%s\",\tscore: \"%.2f\"," % (self.word, self.tag, self.score)
        ret += "now: \"%s\",\tprev: \"%s\")" % (str(id(self)), str(id(self.prev)))
        return ret


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
            vocabulary.add(vol[-1])

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

    def weight(t, word):
        gram1 = "$".join(t)
        gram2 = "$".join(t[:-1])
        if gram1 not in ngram or gram2 not in ngram:
            ret = -99.
        ret = log(ngram[gram1]) - log(ngram[gram2])

        gram = "$".join([t[-1], word])
        if gram not in ngram:
            #print >> sys.stderr, word, gram
            #raw_input()
            if word not in vocabulary:
                ret += (log(ngram["$".join([t[-1], "_RARE_"])])-log(ngram[t[-1]]))
            else:
                ret += -99. - log(ngram[t[-1]])
        else:
            ret += (log(ngram[gram])-log(ngram[t[-1]]))

        return ret

    ext_tags = ["$".join([x,y]) for x in tags for y in tags]

    for sent in fp.read().split("\n\n"):
        res = []
        words = sent.split("\n")
        L = len(words)
        lattice = [[State()]*(len(tags)**2) for _ in xrange(L+1)]
        # print lattice
        for idx, word in enumerate(words):
            prev = []
            if idx == 0:
                for i, t in enumerate(tags):
                    lattice[0][i] = State(
                            score = weight(["*", "*", t], word), 
                            word = word,
                            tag = t,
                            prev = None)
            elif idx == 1:
                for i, t in enumerate(ext_tags):
                    for j, pt in enumerate(tags):
                        # illegal transfer
                        if pt != t.split("$")[0]:
                            continue

                        tlist = ["*"] + t.split("$")
                        stat = State(
                                score = weight(tlist, word) + lattice[0][j].score,
                                word = word,
                                tag  = t.split("$")[1],
                                prev = lattice[0][j])

                        if stat > lattice[1][i]:
                            lattice[1][i] = stat
            else:
                for i, t in enumerate(ext_tags):
                    for j, pt in enumerate(ext_tags):
                        # illegal transfor
                        if pt.split("$")[1] != t.split("$")[0]:
                            continue

                        tlist = pt.split("$") + [t.split("$")[1]]
                        stat = State(
                                score = weight(tlist, word) + lattice[idx-1][j].score,
                                word = word,
                                tag = t.split("$")[1],
                                prev = lattice[idx-1][j])

                        if stat > lattice[idx][i]:
                            lattice[idx][i] = stat

            if debug_mode:
                for i in xrange(idx):
                    for j in xrange(4):
                        print >> sys.stderr, lattice[i][j]
                raw_input()

        best_stat = State()
        for stat in lattice[L-1]:
            if stat > best_stat:
                best_stat = stat

        stat = best_stat
        que = []
        while stat is not None:
            que.append( stat )
            stat = stat.prev
        que.reverse()

        print "\n".join(["%s %s" % (s.word, s.tag) for s in que])
        print ""
