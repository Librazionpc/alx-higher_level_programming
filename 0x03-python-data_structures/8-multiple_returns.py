#!/usr/bin/python3

def multiple_returns(sentence):

    if (sentence == ""):
        return (None)
    lent = len(sentence)
    done = (lent, sentence[0])
    return (done)
