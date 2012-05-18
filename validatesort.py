# Copyright 2012 Madhusudan C.S.
#
# This work is copyrighted under Creative Commons Attribute Share-Alike 3.0
# License (CC BY-SA 3.0)


def func1():
    fp = open('~/sortedfile')
    prevKeys = fp.next().split(',')[1::-1]
    for i, line in enumerate(fp):
        keys = line.split(',')[1::-1]
        if prevKeys >= keys:
            print prevKeys, keys, i
            return
        prevKeys = keys

def func2():
    errors = []
    fp = open('~/sortedfile')
    prevKeys = fp.next().split(',')[0]
    for i, line in enumerate(fp):
        keys = line.split(',')[0]
        if prevKeys >= keys:
            errors.append((prevKeys, keys, i))
        prevKeys = keys
    print len(errors)
    print errors

func2()
