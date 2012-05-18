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


class LosersTree(object):
    def __init__(self, data):
        self.data = data
        self.size = (len(self.data) + 1) & 0xfffffffe
        self.entries = [0] * self.size
        self.losers = [None] * self.size

    def build_tree(self):
        for i, queue in enumerate(self.entries):
            slot = (self.size + i ) >> 1

            curr = i
            while (slot > 0):
                c = 0
                if self.losers[slot] == None or curr == None:
                    c = -1 if self.losers[slot] == None else 1 
                else:
                    c = cmp(self.data[self.losers[slot]][0], self.data[curr][0])

                if c <= 0:
                    self.losers[slot], curr = curr, self.losers[slot]
                slot >>= 1

            self.losers[0] = curr


    def update_tree(self):
        winner = self.losers[0]
        slot = (self.size + winner) >> 1

        min_elem = self.data[winner][self.entries[winner]]
        self.entries[winner] += 1

        curr = winner
        while (slot > 0):
            c = 0
            if (self.entries[self.losers[slot]] >= len(self.data[self.losers[slot]])):
                c = 1
            elif (self.entries[curr] < len(self.data[curr])):
                c = cmp(self.data[self.losers[slot]][self.entries[self.losers[slot]]], self.data[curr][self.entries[curr]]) 

            if (c <= 0):
                self.losers[slot], curr = curr, self.losers[slot]

            slot >>= 1

        self.losers[0] = curr

        return min_elem


if __name__ == '__main__':
    data = [
         [87, 89, 104, 119],
         [48, 56, 88, 97],
         [98, 104, 128, 151],
         [58, 70, 76, 100],
         [33, 91, 156, 205],
         [48, 55, 60, 68],
         [44, 55, 66, 77],
         [80, 96, 106, 113]
        ]

    lt = LosersTree(data)
    lt.build_tree()
    for i in range(12):
        print lt.update_tree

