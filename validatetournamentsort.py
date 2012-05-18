# Copyright 2012 Madhusudan C.S.
#
# This work is copyrighted under Creative Commons Attribute Share-Alike 3.0
# License (CC BY-SA 3.0)
#
# A portion of this work was inspired by the code in Hyracks project available at:
# http://code.google.com/p/hyracks/
#
# The particular source files from which this code was inspired were:
# http://code.google.com/p/hyracks/source/browse/branches/hyracks_asterix_stabilization/hyracks-dataflow-std/src/main/java/edu/uci/ics/hyracks/dataflow/std/util/SelectionTree.java
# and http://code.google.com/p/hyracks/source/browse/branches/hyracks_asterix_stabilization/hyracks-dataflow-std/src/main/java/edu/uci/ics/hyracks/dataflow/std/util/ReferencedPriorityQueue.java
#
# So those works are attributed to the authors of Hyracks.


import sys

class ValidateLosersTree(object):
    def __init__(self):
        self.data = {}

        self.fp = open('~/selectiontreeview.log')
        self.prev_tree = self.get_datastructures(self.fp.next())
        self.size = (len(self.data) + 1) & 0xfffffffe

        self.pass_counter = 0

    def rebuild_tree(self, curr_tree):
        curr = self.prev_tree[0]
        slot = (self.size + curr) >> 1

        while (slot > 0):
            c = 0
            if (self.data[self.prev_tree[slot]] == None):
                c = 1
            elif (self.data[curr] != None):
                c = cmp(self.data[self.prev_tree[slot]], self.data[curr])

            if (c <= 0):
                self.prev_tree[slot], curr = curr, self.prev_tree[slot]

            slot >>= 1

        self.prev_tree[0] = curr

        if self.prev_tree == curr_tree:
            self.pass_counter += 1
        else:
            print "Losers tree failed at: ", self.pass_counter
            sys.exit(1)


    def get_datastructures(self, line):
        elements = line.strip(' ,').split(',')
        tree = []
        for element in elements:
            value, index = element.strip().split(':')
            value = value.strip()
            index = int(index.strip())
            self.data[index] = value
            tree.append(index)
        return tree


    def validate(self):
        for line in self.fp:
            curr_tree = self.get_datastructures(line)
            self.rebuild_tree(curr_tree)


lt = ValidateLosersTree()
lt.validate()


# 4, 1, 3, 6, 0, 2, 5, 7
